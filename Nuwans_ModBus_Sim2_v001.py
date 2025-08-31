import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow,QDialog,QTreeWidgetItem,QTableWidgetItem,QMessageBox,QListWidgetItem,QInputDialog,QLineEdit
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QBrush, QColor
from pymodbus.server import StartTcpServer, ServerStop
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusDeviceContext, ModbusServerContext
from UI import Ui_MainWindow
from ConfigDialog import Ui_ConfigDialog
import threading
import socket
import os
import json
import jsbeautifier
import math
import numpy as np
from time import sleep
import asyncio
import random
from pympler import asizeof
from SimObjects import *



# Initialize your data store
store = ModbusDeviceContext(hr=ModbusSequentialDataBlock(0, [0]*50000))
context = ModbusServerContext(devices=store, single=True)


class ServerThread:
    def __init__(self):
        self.server_process = None
        self._is_running = False
        self.server_task = None
        self.loop = None
    
    @property
    def is_running(self):
        return self._is_running

    def start_server(self):
        if not self.is_running:
            self.server_process = threading.Thread(target=self.run_server)
            self.server_process.daemon = True
            self.server_process.start()
            self._is_running = True
        
    def stop_server(self):
        if self.server_process is not None:
            try:
                if self.loop and self.server_task:
                    self.loop.call_soon_threadsafe(self.server_task.cancel)
                if self.loop:
                    self.loop.call_soon_threadsafe(self.loop.stop)
            except:
                pass
            self.server_process.join(timeout=1)  # Wait for the process to terminate
            self.server_process = None
            self._is_running = False
            
    def run_server(self):
        # Create a new event loop for this thread
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        
        try:
            # Start the TCP server - in pymodbus 3.x this is synchronous
            StartTcpServer(context=context, address=("", 502))
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            if self.loop and not self.loop.is_closed():
                self.loop.close()
        

class Register:
    def __init__(self, address:int, value:int):
        self.addr = address
        self.val = value
        store.setValues(3, self.addr, [self.val])
    
    @property
    def Address(self):
        return self.addr

    @Address.setter
    def Address(self, address:int):
        self.addr = address
        
    @property
    def Value(self):
        result = store.getValues(3, self.addr, count=1)
        if isinstance(result, list) or isinstance(result, tuple):
            self.val = result[0]
        else:
            # If result is an exception code, handle gracefully
            self.val = 0
        return self.val
    
    @Value.setter
    def Value(self, value:int):
        self.val = value
        store.setValues(3, self.addr, [self.val])


class Vector:
    def __init__(self,address:int, value:int):
        self.register = Register(address, value)

    def SetBit(self, position: int, status: int):
        if status:
            self.register.Value = self.register.Value | (1 << position)
        else:
            self.register.Value = self.register.Value & ~(1 << position)
    
    def GetBit(self, position: int):
        return (self.register.Value >> position) & 1
    
    def SetArray(self, start: int, end: int, value: int):
        length = end - start + 1  # Length of the cleared slot
        if value.bit_length() > length:
            print(f"Error: The bit-length of the value is larger than the cleared slot.")
            return
        mask = ((1 << (end - start + 1)) - 1) << start
        self.register.Value = (self.register.Value & ~mask) | (value << start) 
        
    def SetArrayForce(self, start: int, value: int):
        length = value.bit_length()  # Length of the value in bits
        mask = ((1 << length) - 1) << start  # Create a mask with 1s from start to start+length
        self.register.Value = (self.register.Value & ~mask) | (value << start)

    def GetArray(self, start: int, end: int):
        length = end - start + 1  # Length of the range in bits
        mask = ((1 << length) - 1) << start  # Create a mask with 1s from start to end
        return (self.register.Value & mask) >> start

    @property
    def Value(self):
        return self.register.Value
    
    @Value.setter
    def Value(self, value: int):
        self.register.Value = value
    
    @property
    def Address(self):
        return self.register.Address
    
    @Address.setter
    def Address(self, address: int):
        self.register.Address = address

class IntTag:
    def __init__(self, address:int, value:float, decimalPoints:int):
        self.decimalPoints = decimalPoints
        self.register = Register(address, int(round(value*10**self.decimalPoints)))
    
    def SetDecimalPoints(self, decimalPoints:int):
        value = self.Value
        self.decimalPoints = decimalPoints
        self.register.Value = int(round(value*10**self.decimalPoints))
        
    @property
    def Value(self):
        return float(self.register.Value/10**self.decimalPoints)
         
    @Value.setter
    def Value(self, value: float):
        self.register.Value = int(round(value*10**self.decimalPoints))
        
    @property
    def Address(self):
        return self.register.Address
    
    @Address.setter
    def Address(self, address: int):
        self.register.Address = address

class SignedIntTag:
    def __init__(self, address:int, value:float, decimalPoints:int):
        self.decimalPoints = decimalPoints
        self.register = Register(address, int(round(value*10**self.decimalPoints)))
    
    def SetDecimalPoints(self, decimalPoints:int):
        value = self.Value
        self.decimalPoints = decimalPoints
        self.register.Value = int(round(value*10**self.decimalPoints))
        
    @property
    def Value(self):
        if self.register.Value > 0x7FFF:
            return float((-1*(0xFFFF - self.register.Value + 1))/10**self.decimalPoints)
        else:
            return float(self.register.Value/10**self.decimalPoints)
         
    @Value.setter
    def Value(self, value: float):
        self.register.Value = int(round(value*10**self.decimalPoints)) & 0xFFFF
        
    @property
    def Address(self):
        return self.register.Address
    
    @Address.setter
    def Address(self, address: int):
        self.register.Address = address

class LongTag:
    def __init__(self, address:int, value:int, inverse:bool=False):
        self.inverse = inverse
        self.register1 = Register(address, 0)
        self.register2 = Register(address+1, 0)
        self.Value = value
    
    @property
    def Value(self):
        if self.inverse:
            return (self.register1.Value << 16) | self.register2.Value  
        else:
            return (self.register2.Value << 16) | self.register1.Value 
         
    @Value.setter
    def Value(self, value: int):
        if self.inverse:
            self.register2.Value = value & 0xFFFF  # Lower 16 bits
            self.register1.Value = (value >> 16) & 0xFFFF  # Upper 16 bits
        else:
            self.register2.Value = (value >> 16) & 0xFFFF  # Upper 16 bits
            self.register1.Value = value & 0xFFFF  # Lower 16 bits
        
    @property
    def Address(self):
        return self.register1.Address
    
    @Address.setter
    def Address(self, address: int):
        self.register1.Address = address
        self.register2.Address = address+1
        
    def SetInverse(self, inverse: bool):
        value = self.Value
        self.inverse = inverse
        self.Value = value
        
        
class FloatTag:
    def __init__(self, address:int, value:float,inverse:bool=False):
        self.inverse = inverse
        self.register1 = Register(address, 0)
        self.register2 = Register(address+1, 0)
        self.Value = value
    
    @property
    def Value(self):
        if self.inverse:
            return np.float32(np.uint32((self.register1.Value << 16) | self.register2.Value).view('float32'))
        else:
            return np.float32(np.uint32((self.register2.Value << 16) | self.register1.Value).view('float32'))
         
    @Value.setter
    def Value(self, value: float):
        value_int = int(np.uint32(np.float32(value).view('uint32')))
        if self.inverse:
            self.register2.Value = value_int & 0xFFFF
            self.register1.Value = (value_int >> 16) & 0xFFFF
        else:
            self.register2.Value = (value_int >> 16) & 0xFFFF
            self.register1.Value = value_int & 0xFFFF
    
    @property
    def Address(self):
        return self.register1.Address
    
    @Address.setter
    def Address(self, address: int):
        self.register1.Address = address
        self.register2.Address = address + 1
        
    def SetInverse(self, inverse: bool):
        value = self.Value
        self.inverse = inverse
        self.Value = float(value)

        
class Device:
    def __init__(self,deviceDecl:dict,definitions:dict):
        #Basic Parameters
        self.Name = deviceDecl['name']
        self.StartAddress = deviceDecl['address']
        self.Type = deviceDecl['type']
        self.ParentKey = deviceDecl['parent']
        self.EnableSimulate = definitions[self.Type]['EnableSimulate']
        #Control Parameters
        self.Status01 = None
        self.Status02 = None
        self.Control01 = None
        self.Analog = []
        self.Settings = []
        #Simulation Parameters
        self.Simulate = False
        self.SimScale = deviceDecl['simscale']
        self.Simulator = None
        self.SettingsLoad = True
        self.AnalogLoad = False
        self.StatusLoad = False
        #Create Device
        self.CreateDevice(deviceDecl,definitions)
        self.Preload(deviceDecl)
        
    def CreateDevice(self,deviceDecl:dict,definitions:dict):
        counter = 3  
        if definitions[self.Type]['Status01']:
            self.Status01 = Vector(self.StartAddress,0)
        if definitions[self.Type]['Status02']:
            self.Status02 = Vector(self.StartAddress+1,0)    
        if definitions[self.Type]['Control01']:
            self.Control01 = Vector(self.StartAddress+2,0)
        if definitions[self.Type]['Analog']:
            for analogTag in definitions[self.Type]['Analog']:
                if analogTag['type'] == 'int':
                    self.Analog.append(IntTag(self.StartAddress + counter,0,analogTag['dp']))
                    counter += 1
                elif analogTag['type'] == 'Sint':
                    self.Analog.append(SignedIntTag(self.StartAddress + counter,0,analogTag['dp']))
                    counter += 1
                elif analogTag['type'] == 'long':
                    self.Analog.append(LongTag(self.StartAddress + counter,0))
                    counter += 2
                elif analogTag['type'] == 'float':
                    self.Analog.append(FloatTag(self.StartAddress + counter,0))
                    counter += 2
                elif analogTag['type'] == 'longInv':
                    self.Analog.append(LongTag(self.StartAddress + counter,0,True))
                    counter += 2
                elif analogTag['type'] == 'floatInv':
                    self.Analog.append(FloatTag(self.StartAddress + counter,0,True))
                    counter += 2
        if definitions[self.Type]['Settings']:
            for settingTag in definitions[self.Type]['Settings']:
                if settingTag['type'] == 'int':
                    self.Settings.append(IntTag(self.StartAddress + counter,0,settingTag['dp']))
                    counter += 1
                elif settingTag['type'] == 'long':
                    self.Settings.append(LongTag(self.StartAddress + counter,0))
                    counter += 2
                elif settingTag['type'] == 'float':
                    self.Settings.append(FloatTag(self.StartAddress + counter,0))
                    counter += 2
                elif settingTag['type'] == 'longInv':
                    self.Settings.append(LongTag(self.StartAddress + counter,0,True))
                    counter += 2
                elif settingTag['type'] == 'floatInv':
                    self.Settings.append(FloatTag(self.StartAddress + counter,0,True))
                    counter += 2
                    
    def Preload(self,deviceDecl:dict):
        if self.SettingsLoad:
            self.LoadSettings(deviceDecl)
        if self.AnalogLoad:
            self.LoadAnalog(deviceDecl)
        if self.StatusLoad:
            self.LoadStatus(deviceDecl)
    
    def LoadSettings(self,deviceDecl:dict):
        if self.Settings and deviceDecl['settings']:
            for i in range(len(self.Settings)):
                self.Settings[i].Value = deviceDecl['settings'][i]
                
    def LoadAnalog(self,deviceDecl:dict):
        if self.Analog and deviceDecl['analog']:
            for i in range(len(self.Analog)):
                self.Analog[i].Value = deviceDecl['analog'][i]
                
    def LoadStatus(self,deviceDecl:dict):
        if self.Status01 and deviceDecl['status01']:
            self.Status01.Value = deviceDecl['status01']
        if self.Status02 and deviceDecl['status02']:
            self.Status02.Value = deviceDecl['status02']
                    
    def AddSimulator(self):
        if self.Simulator is None:
            self.Simulate = True
            self.Simulator = Simulator(self)
            return self.Simulator

    def RemoveSimulator(self):
        if self.Simulator:
            self.Simulate = False
            self.Simulator.Restore()
            self.Simulator = None 
        
        
class Place:
    def __init__(self,name:str,devicesDecl:dict,definitions:dict):
        self.Name = name
        self.Devices = {}
        self.AddDevices(devicesDecl,definitions)
        
    def AddDevices(self,devicesDecl:dict,definitions:dict):
        #check if the self.Devices is empty
        if self.Devices:
            self.Devices = {}
        for device in devicesDecl:
            self.Devices[device] = Device(devicesDecl[device],definitions)
    
    def LinkDevices(self,devicesDecl:dict):
        if self.Devices:
            for device in devicesDecl:
                if devicesDecl[device]['link'] != None:
                    print(f"Linking    {devicesDecl[device]['name']} --> {devicesDecl[devicesDecl[device]['link']]['name']}")
                    self.Devices[device].Status02.Address = self.Devices[devicesDecl[device]['link']].Status02.Address    
        else:
            print("Devices are not created !")
    
class Plant:
    def __init__(self,placesDecl:dict,definitions:dict):
        self.Places = {}
        self.PlacesDecl = placesDecl
        self.CreatePlant(placesDecl,definitions)
        
    def CreatePlant(self,placesDecl:dict,definitions:dict):
        counter = 0
        for place in placesDecl:
            self.Places[place] = Place(placesDecl[place][place]['name'],placesDecl[place],definitions)
            
    def LinkDevices(self):
        if self.Places:
            for place in self.PlacesDecl:
                self.Places[place].LinkDevices(self.PlacesDecl[place])
        else:
            print("Places are not created !")
 
class Simulator:
    def __init__(self, device: Device):
        self.device = device
        self.simObj = None
        if self.device.Type == 'Motor-VSD':
            self.simObj = SimObj_MotorVSD(device)
        elif self.device.Type == 'Motor-Normal':
            self.simObj = SimObj_MotorNormal(device)
        elif self.device.Type == 'Valve-MOV':
            self.simObj = SimObj_ValveMOV(device)
        elif self.device.Type == 'Valve-Modulating':
            self.simObj = SimObj_ValveModulating(device)
        elif self.device.Type == 'Valve-Solenoid':
            self.simObj = SimObj_ValveSolenoid(device)
        elif self.device.Type == 'Sensor-Level':
            self.simObj = SimObj_SensorLevel(device)
        elif self.device.Type == 'Sensor-Totalizing':
            self.simObj = SimObj_SensorTotalizing(device)
        elif self.device.Type == 'Sensor-Analog':
            self.simObj = SimObj_SensorAnalog(device)
        elif self.device.Type == 'PID Control':
            self.simObj = SimObj_PIDControl(device)
        elif self.device.Type == 'DPA':
            self.simObj = SimObj_DPA(device)
        elif self.device.Type == 'GEN Power':
            self.simObj = SimObj_Generator(device)
        elif self.device.Type == 'RSF':
            self.simObj = SimObj_RSF(device)
        elif self.device.Type == 'UPS Power':
            self.simObj = SimObj_UPS(device)
        elif self.device.Type == 'Screen Package':
            self.simObj = SimObj_ScreenPackage(device)
        elif self.device.Type == 'Root':
            self.simObj = SimObj_Root(device)
        elif self.device.Type == 'Ventilation Fans':
            self.simObj = SimObj_VentilationFans(device)
        
    async def Simulate(self):
        if self.simObj:
            await self.simObj.simulate()
            
    def Restore(self):
        if self.simObj:
            self.simObj.Restore()
            self.simObj = None
                  
   
class Helper:
    @staticmethod
    def loadJson(filename):
        dirName = os.path.dirname(__file__)
        filePath = os.path.join(dirName, filename)
        with open(filePath) as fp:
            return json.load(fp)
        
    @staticmethod
    def saveJson(filename, data):
        json_data = jsbeautifier.beautify(json.dumps(data))
        options = jsbeautifier.default_options()
        options.indent_size = 4
        formatted_json = jsbeautifier.beautify(json_data, options)
        dirName = os.path.dirname(__file__)
        filePath = os.path.join(dirName, filename)
        backupPath = os.path.join(dirName, f"{filename}.bak")
        with open(filePath, 'w') as fp:
            fp.write(formatted_json)
        with open(backupPath, 'w') as fp:
            json.dump(data, fp, indent=4)

    @staticmethod
    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
    
    @staticmethod
    def round_n(x, n):
        if x == 0:
            return 0
        else:
            return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

# Assuming you have a MainWindow class that uses the ServerThread
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server_thread = ServerThread()
        self.InitPlant()

    def InitVar(self):
        self.simulatorList = []

    def showEvent(self, event):
        super().showEvent(event)
        self.server_thread.start_server()
        self.ui.lblServStatus.setText("RUNNING")
    
    def on_reload_button_clicked(self):
        QApplication.quit()
        sleep(1)
        subprocess.run([sys.executable, __file__])

    def closeEvent(self, event):
        self.stop_Threads()
        super().closeEvent(event)
        self.ui.lblServStatus.setText("STOPPED")
 
    def InitPlant(self):
        self.projDef = Helper.loadJson("project.json")
        self.devicesDef = Helper.loadJson("devices.json")
        self.Places = Helper.loadJson("places.json")
        self.Plant = Plant(self.Places,self.devicesDef)
        #self.Plant.LinkDevices()
        self.InitUi()
            
    def InitUi(self):
        self.InitVar()
        self.InitCheckBoxes()
        #Initiate Project Definition
        self.ui.lblProjectName.setText(self.projDef["Project Name"])
        self.ui.lblServIP.setText(Helper.get_ip_address())
        self.ui.lblServPort.setText("502")
        level2_keys_count = sum(len(self.Places[level1_key]) for level1_key in self.Places)
        self.ui.lblTotDev.setText(f"{level2_keys_count}")
        #Initiate Devices
        self.init_DevicesCMB()
        self.init_Tables()
        self.ui.cmbPlace.currentIndexChanged.connect(self.update_DevicesTree)
        self.update_DevicesTree()
        self.ui.treeDevices.itemClicked.connect(self.on_tree_item_clicked)
        self.select_first_TreeItem()
        self.ui.tblAnalog.itemChanged.connect(self.on_cell_changed)
        self.ui.tblSettings.itemChanged.connect(self.on_cell_changed)
        self.ui.chkSimulate.clicked.connect(self.on_chkSimulate_toggled)
        self.ui.spnSimScale.valueChanged.connect(self.on_spnSimScale_valueChanged)
        self.ui.chkPreloadSettings.clicked.connect(self.on_chkPreloadSettings_toggled)
        self.ui.chkPreloadAnalog.clicked.connect(self.on_chkPreloadAnalog_toggled)
        self.ui.chkPreloadStatus.clicked.connect(self.on_chkPreloadStatus_toggled)
        self.ui.btnReload.clicked.connect(self.on_reload_button_clicked)
        self.ui.btnConfigure.clicked.connect(self.on_configure_button_clicked)
        #Initiate Threads
        self.init_Threads()

    def init_Threads(self):
        self.device_lock = threading.Lock()
        self.read_thread = threading.Thread(target=self.read_values)
        self.read_thread.daemon = True
        self.read_thread.start()
        # Create a new event loop
        self.loop = asyncio.new_event_loop()
        # Set the event loop as the event loop for the current context
        asyncio.set_event_loop(self.loop)
        # Schedule simulate_objects to run on the event loop
        self.simulator_task = self.loop.create_task(self.simulate_objects())
        # Run the event loop in a new thread
        self.simulator_thread = threading.Thread(target=self.loop.run_forever)
        self.simulator_thread.daemon = True
        self.simulator_thread.start()
        
    def stop_Threads(self):
        if self.read_thread is not None:
            self.read_thread = None
        if self.simulator_thread is not None:
            self.simulator_thread = None
        self.loop.call_soon_threadsafe(self.loop.stop)
        if self.simulator_task is not None:
            self.simulator_task.cancel()
            self.simulator_task = None
        
    def read_values(self):
        while self.read_thread is not None:
            with self.device_lock:
                device = self.get_current_device()
                self.update_UiValues(device)
            sleep(0.25)
            
    async def simulate_objects(self):
        while self.simulator_thread is not None:
            with self.device_lock:
                if self.simulatorList:
                    tasks = [object.Simulate() for object in self.simulatorList]
                    try:
                        results = await asyncio.gather(*tasks, return_exceptions=True)
                        for result in results:
                            if isinstance(result, Exception):
                                print(f"Error of Object: {result}")
                    except Exception as e:
                        print(f"Error Desc: {e}")
            await asyncio.sleep(0.25)
    
    def InitCheckBoxes(self):
        self.status01 = [getattr(self.ui, f'chkStatus01_{i:02d}') for i in range(16)]
        self.status02 = [getattr(self.ui, f'chkStatus02_{i:02d}') for i in range(16)]
        self.control01 = [getattr(self.ui, f'chkControl01_{i:02d}') for i in range(16)]
        for checkbox in self.status01:
            checkbox.setCheckable(True)
            checkbox.clicked.connect(lambda _: self.Status01_toggled(self.status01))
        for checkbox in self.status02:
            checkbox.setCheckable(True)
            checkbox.clicked.connect(lambda _: self.Status02_toggled(self.status02))
        for checkbox in self.control01:
            checkbox.setCheckable(True)
            checkbox.clicked.connect(lambda _: self.Control01_toggled(self.control01))
    
    def Status01_toggled(self, checkboxes):
        value = self.calculate_checkboxes(checkboxes)
        device = self.get_current_device()
        if device.Status01.Value is not None:
            device.Status01.Value = value
            self.ui.lblStatus01Value.setText(f"{value}")
            self.ui.chkPreloadStatus.setChecked(False)
            device.StatusLoad = False

    def Status02_toggled(self, checkboxes):
        value = self.calculate_checkboxes(checkboxes)
        device = self.get_current_device()
        if device.Status02.Value is not None:
            device.Status02.Value = value
            self.ui.lblStatus02Value.setText(f"{value}")
            self.ui.chkPreloadStatus.setChecked(False)
            device.StatusLoad = False
        
    def Control01_toggled(self, checkboxes):
        value = self.calculate_checkboxes(checkboxes)
        device = self.get_current_device()
        if device.Control01.Value is not None:
            device.Control01.Value = value
            self.ui.lblControl01Value.setText(f"{value}")

    def calculate_checkboxes(self, checkboxes):
        value = 0
        for i, checkbox in enumerate(checkboxes):
            if checkbox.isChecked():
                value |= 1 << i
        return value
     
    def populate_checkboxes(self, checkboxes,value):
        for i, checkbox in enumerate(checkboxes):
            bit_status = (value >> i) & 1
            checkbox.setChecked(bit_status)
            
    def init_DevicesCMB(self):
        self.ui.cmbPlace.clear()
        for i,place in enumerate(self.Plant.Places):
            self.ui.cmbPlace.addItem(self.Plant.Places[place].Name)
            self.ui.cmbPlace.setItemData(i, place)

    def update_DevicesTree(self):
        place = self.Plant.Places[self.ui.cmbPlace.currentData()]
        treeDict = {}
        self.ui.treeDevices.clear()
        for device in place.Devices:
            treeDict[device] = QTreeWidgetItem([place.Devices[device].Name,device])
            if place.Devices[device].Simulate:
                treeDict[device].setForeground(0, QBrush(QColor(0, 200, 0)))
            if place.Devices[device].ParentKey == None:
                self.ui.treeDevices.addTopLevelItem(treeDict[device])
            else:
                treeDict[place.Devices[device].ParentKey].addChild(treeDict[device])
        self.ui.treeDevices.expandAll()
        self.select_first_TreeItem()
        
    def on_tree_item_clicked(self, item, column):
        device = self.get_current_device()
        self.update_UiLabels(device)
        self.update_UiValues(device)
    
    def get_current_device(self):
        place = self.Plant.Places[self.ui.cmbPlace.currentData()]
        device = place.Devices[self.ui.treeDevices.currentItem().text(1)]
        return device
    
    def get_current_device_decl(self):
        place = self.Places[self.ui.cmbPlace.currentData()]
        deviceDecl = place[self.ui.treeDevices.currentItem().text(1)]
        return deviceDecl
        
    def select_first_TreeItem(self):
        first_item = self.ui.treeDevices.topLevelItem(0)
        if first_item is not None:
            self.ui.treeDevices.setCurrentItem(first_item)
            self.on_tree_item_clicked(first_item, 0)
    
    def update_UiLabels(self,device):
        self.ui.lblDeviceType.setText(device.Type)
        self.ui.spnSimScale.setValue(device.SimScale*100)
        self.ui.chkSimulate.setChecked(device.Simulate)
        self.ui.chkSimulate.setDisabled(not device.EnableSimulate)
        self.set_disable_simcoltrols(device.Simulate)
        self.ui.chkPreloadSettings.setChecked(device.SettingsLoad)
        self.ui.chkPreloadAnalog.setChecked(device.AnalogLoad)
        self.ui.chkPreloadStatus.setChecked(device.StatusLoad)
        self.update_Ui_ChkLabels(device.Status01,'Status01', self.ui.lblStatus01Address, self.status01, device.Type)
        self.update_Ui_ChkLabels(device.Status02,'Status02', self.ui.lblStatus02Address, self.status02, device.Type)
        self.update_Ui_ChkLabels(device.Control01,'Control01', self.ui.lblControl01Address, self.control01, device.Type)
        self.update_Ui_Table(device,self.ui.tblAnalog,'Analog')
        self.update_Ui_Table(device,self.ui.tblSettings,'Settings')
            
    def update_Ui_Table(self,device,table,tableType):
        table.clearSelection()
        table.blockSignals(True)
        numRows = len(self.devicesDef[device.Type][tableType])
        table.setRowCount(numRows)
        for i, Tag in enumerate(self.devicesDef[device.Type][tableType]):
            item = QTableWidgetItem(Tag['name'])
            item.setFlags(item.flags() & ~Qt.ItemIsEditable) # type: ignore
            if tableType == 'Analog':
                item.setToolTip(f"Address: {400000 + device.Analog[i].Address}")
            elif tableType == 'Settings':
                item.setToolTip(f"Address: {400000 + device.Settings[i].Address}")
            table.setItem(i,0,item)
        table.blockSignals(False)        
    
    def update_Ui_TableValues(self,tagList,table):
        table.blockSignals(True)
        for i, Tag in enumerate(tagList):
            new_value = f"{tagList[i].Value}"
            current_item = table.item(i, 1)
            if current_item is None or current_item.text() != new_value:
                table.setItem(i, 1, QTableWidgetItem(new_value))
        table.blockSignals(False)

    def init_Tables(self):
        headers = ['Name','Value']
        self.ui.tblAnalog.setColumnWidth(0, 150)
        self.ui.tblAnalog.setColumnWidth(1, 62) 
        self.ui.tblAnalog.setColumnCount(len(headers))
        self.ui.tblAnalog.setHorizontalHeaderLabels(headers)
        self.ui.tblSettings.setColumnWidth(0, 150)
        self.ui.tblSettings.setColumnWidth(1, 62)
        self.ui.tblSettings.setColumnCount(len(headers))
        self.ui.tblSettings.setHorizontalHeaderLabels(headers)

    def update_Ui_ChkLabels(self, status,strStatus, label, checkboxes, device_type):
        if status:
            label.setText(f"{400000 + status.Address}")
            for i, status_name in enumerate(self.devicesDef[device_type][strStatus]):
                checkboxes[i].setText(status_name)
                checkboxes[i].setDisabled(False)
        else:
            label.setText("--")
            for checkbox in checkboxes:
                checkbox.setText("--")
                checkbox.setChecked(False)
                checkbox.setDisabled(True)          
             
    def update_UiValues(self,device):
        self.update_Ui_ChkValues(device.Status01,self.status01,self.ui.lblStatus01Value)
        self.update_Ui_ChkValues(device.Status02,self.status02,self.ui.lblStatus02Value)
        self.update_Ui_ChkValues(device.Control01,self.control01,self.ui.lblControl01Value)
        self.update_Ui_TableValues(device.Analog,self.ui.tblAnalog)
        self.update_Ui_TableValues(device.Settings,self.ui.tblSettings)
        
    def update_Ui_ChkValues(self, status, checkboxes,label):
        if status:
            self.populate_checkboxes(checkboxes,status.Value)
            label.setText(f"{status.Value}")
        else:
            label.setText("--")
            for checkbox in checkboxes:
                checkbox.setChecked(False)
                
    def on_cell_changed(self, item):
        if item.isSelected():
            device = self.get_current_device()
            if item.tableWidget() == self.ui.tblAnalog:
                if (type(device.Analog[item.row()]) == LongTag) and (device.Analog[item.row()].Value != int(item.text())):
                    device.Analog[item.row()].Value = int(item.text())
                elif device.Analog[item.row()].Value != float(item.text()):
                    device.Analog[item.row()].Value = float(item.text())
                self.ui.chkPreloadAnalog.setChecked(False)
                device.AnalogLoad = False
            elif item.tableWidget() == self.ui.tblSettings:
                if (type(device.Settings[item.row()]) == LongTag) and (device.Settings[item.row()].Value != int(item.text())):
                    device.Settings[item.row()].Value = int(item.text())
                elif device.Settings[item.row()].Value != float(item.text()):
                    device.Settings[item.row()].Value = float(item.text())
                self.ui.chkPreloadSettings.setChecked(False)
                device.SettingsLoad = False

    
    def on_chkSimulate_toggled(self, state):
        device = self.get_current_device()
        value = self.ui.chkSimulate.isChecked()
        if value:
            if device.Simulator is None:
                print(f"Simulating --- {self.ui.cmbPlace.currentText()} --- {device.Name}")
                device.AddSimulator()
                self.simulatorList.append(device.Simulator)
                self.set_disable_simcoltrols(True)
                self.ui.treeDevices.currentItem().setForeground(0, QBrush(QColor(0, 200, 0)))
                #size = asizeof.asizeof(self.simulatorList)
                #print(f"Size of simulatorList: {size} bytes")
        else:
            if device.Simulator:
                print(f"Stop simulating --- {self.ui.cmbPlace.currentText()} --- {device.Name}")
                self.simulatorList.remove(device.Simulator)
                device.RemoveSimulator()
                self.set_disable_simcoltrols(False)
                self.ui.treeDevices.currentItem().setForeground(0, QBrush(QColor(0, 0, 0)))
        self.ui.lblSimDev.setText(f"{len(self.simulatorList)}")
    
    def set_disable_simcoltrols(self, state):
        self.ui.chkPreloadSettings.setDisabled(state)
        self.ui.chkPreloadAnalog.setDisabled(state)
        self.ui.chkPreloadStatus.setDisabled(state)
        self.ui.spnSimScale.setDisabled(state)
    
    def on_spnSimScale_valueChanged(self, value):
        device = self.get_current_device()
        device.SimScale = value/100
        if device.Simulator:
            device.Simulator.SimScale = value/100
    
    def on_chkPreloadSettings_toggled(self, state):
        device = self.get_current_device()
        device.SettingsLoad = self.ui.chkPreloadSettings.isChecked()
        if device.SettingsLoad:
            deviceDecl = self.get_current_device_decl()
            device.LoadSettings(deviceDecl)
        else:
            for setting in device.Settings:
                setting.Value = 0
            
    def on_chkPreloadAnalog_toggled(self, state):
        device = self.get_current_device()
        device.AnalogLoad = self.ui.chkPreloadAnalog.isChecked()
        if device.AnalogLoad:
            deviceDecl = self.get_current_device_decl()
            device.LoadAnalog(deviceDecl)
        else:
            for analog in device.Analog:
                analog.Value = 0

    def on_chkPreloadStatus_toggled(self, state):
        device = self.get_current_device()
        device.StatusLoad = self.ui.chkPreloadStatus.isChecked()
        if device.StatusLoad:
            deviceDecl = self.get_current_device_decl()
            device.LoadStatus(deviceDecl)
        else:
            if device.Status01:
                device.Status01.Value = 0
            if device.Status02:
                device.Status02.Value = 0

    def on_configure_button_clicked(self):
        self.dialog = ConfigDialog()
        self.dialog.show()
        #self.dialog.exec()

class ConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfigDialog()
        self.ui.setupUi(self)
        self.connect_signals()
        
    def connect_signals(self):
       self.ui.btnOpen.clicked.connect(self.on_open_button_clicked)
       self.ui.btnSave.clicked.connect(self.on_save_button_clicked)
       self.ui.btnSave.setDisabled(True)
       self.disbale_place_controls(True)
       self.ui.btnClose.clicked.connect(self.close)
       self.ui.lstPlaces.itemClicked.connect(self.on_place_item_clicked)
       self.ui.treeDevices.itemClicked.connect(self.on_device_item_clicked)
       self.ui.tblAnalogPreload.setHorizontalHeaderLabels(['Name','Value'])
       self.ui.tblAnalogPreload.setColumnWidth(0, 150)
       self.ui.tblAnalogPreload.setColumnWidth(1, 62)
       self.ui.tblAnalogPreload.verticalHeader().setVisible(False)
       self.ui.tblSettingsPreload.setHorizontalHeaderLabels(['Name','Value'])
       self.ui.tblSettingsPreload.setColumnWidth(0, 150)
       self.ui.tblSettingsPreload.setColumnWidth(1, 62)
       self.ui.tblSettingsPreload.verticalHeader().setVisible(False)
       self.ui.btnAddPlace.clicked.connect(self.on_add_place_button_clicked)
       self.ui.btnRemovePlace.clicked.connect(self.on_remove_place_button_clicked)
       self.ui.btnRenamePlace.clicked.connect(self.on_rename_place_button_clicked)
       self.ui.btnPlaceUp.clicked.connect(self.on_place_up_button_clicked)
       self.ui.btnPlaceDn.clicked.connect(self.on_place_down_button_clicked)
       self.ui.btnAddDevice.clicked.connect(self.on_add_device_button_clicked)
       self.ui.btnRemoveDevice.clicked.connect(self.on_remove_device_button_clicked)
       self.ui.btnRenameDevice.clicked.connect(self.on_rename_device_button_clicked)
       self.ui.btnDeviceUp.clicked.connect(self.on_device_up_button_clicked)
       self.ui.btnDeviceDn.clicked.connect(self.on_device_down_button_clicked)
       self.ui.btnUpdateAnalog.clicked.connect(self.on_update_analog_button_clicked)
       self.ui.btnUpdateSettings.clicked.connect(self.on_update_settings_button_clicked)
       self.ui.btnUpdateOthers.clicked.connect(self.on_update_others_button_clicked)
       self.ui.btnReSeqAddress.clicked.connect(self.on_reseq_address_button_clicked)
       self.ui.btnReSeqAddress.setDisabled(True)
                  
    def on_open_button_clicked(self):
        self.PlantDef = Helper.loadJson("project.json")
        self.PlacesDecl = Helper.loadJson("places.json")
        self.DevicesDef = Helper.loadJson("devices.json")
        self.ui.lblAvilableAddress.setText(f"{self.PlantDef['AddressCount']+400000}")
        self.load_Places(self.PlacesDecl)
        self.load_device_def(self.DevicesDef)
        self.ui.btnSave.setDisabled(False)
        self.disbale_place_controls(False)
        self.ui.btnReSeqAddress.setDisabled(False)
        self.clear_place_controls()

    def on_save_button_clicked(self):
        response = QMessageBox.question(self, 'Save', "Do you want to save the changes?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)# type: ignore
        if response == QMessageBox.Yes: # type: ignore
            Helper.saveJson("places.json",self.PlacesDecl)
            Helper.saveJson("project.json",self.PlantDef)
    
    def load_Places(self,placesDecl):
        self.ui.lstPlaces.clear()
        self.ui.treeDevices.clear()
        self.clear_definitions()
        for place in placesDecl:
            item = QListWidgetItem(placesDecl[place][place]['name'])
            item.setData(Qt.UserRole, place) # type: ignore
            self.ui.lstPlaces.addItem(item)
            
    def load_device_def(self,deviceType):
        self.ui.cmbDevTypeConfig.clear()
        for type in deviceType:
            self.ui.cmbDevTypeConfig.addItem(type)
    
    def on_place_item_clicked(self, item):
        treeDict = {}
        self.ui.treeDevices.clear()
        self.clear_definitions()
        for device in self.PlacesDecl[item.data(Qt.UserRole)]: # type: ignore
            treeDict[device] = QTreeWidgetItem([self.PlacesDecl[item.data(Qt.UserRole)][device]['name'],device]) # type: ignore
            if self.PlacesDecl[item.data(Qt.UserRole)][device]['parent'] == None: # type: ignore
                self.ui.treeDevices.addTopLevelItem(treeDict[device])
            else:
                treeDict[self.PlacesDecl[item.data(Qt.UserRole)][device]['parent']].addChild(treeDict[device]) # type: ignore
        self.ui.treeDevices.expandAll()
        self.ui.txtNewPlace.setText(item.text())
        self.ui.txtPlaceAlias.setText(item.data(Qt.UserRole)) # type: ignore
        self.clear_device_controls()
        self.ui.cmbParent.addItem("--None--")
        for device in treeDict:
            self.ui.cmbParent.addItem(device)
        self.ui.cmbDevTypeConfig.setCurrentText("Default")
        self.ui.lblCurrentAddress.setText("--")
        
    def get_current_device_def(self):
        return self.DevicesDef[self.get_current_device_decl()['type']]
    
    def get_current_device_decl(self):
        return self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)][self.ui.treeDevices.currentItem().text(1)] # type: ignore   
    
    def get_all_tree_items(self,tree_widget):
        items = []
        for i in range(tree_widget.topLevelItemCount()):
            parent = tree_widget.topLevelItem(i)
            items.append(parent)
            for j in range(parent.childCount()):
                child = parent.child(j)
                items.append(child)
        return items
    
    def clear_definitions(self):
        self.ui.tblAnalogPreload.setRowCount(0)
        self.ui.tblSettingsPreload.setRowCount(0)
        self.ui.spnSimScale.setValue(0)
        self.ui.spnStatus01.setValue(0)
        self.ui.spnStatus02.setValue(0)
        self.ui.cmbLink.clear()
    
    def on_device_item_clicked(self, item):
        #self.ui.tblAnalogPreload.clear()
        current_device_def = self.get_current_device_def()
        current_device_decl = self.get_current_device_decl()
        self.ui.tblAnalogPreload.setRowCount(len(current_device_def['Analog']))
        for i, Tag in enumerate(current_device_def['Analog']):
            Tagitem = QTableWidgetItem(Tag['name'])
            Tagitem.setFlags(Tagitem.flags() & ~Qt.ItemIsEditable) # type: ignore
            self.ui.tblAnalogPreload.setItem(i,0,Tagitem)
            if current_device_decl['analog']:
                value = current_device_decl['analog'][i]
                self.ui.tblAnalogPreload.setItem(i,1,QTableWidgetItem(f"{value}"))
            else:
                self.ui.tblAnalogPreload.setItem(i,1,QTableWidgetItem("0"))
        self.ui.tblSettingsPreload.setRowCount(len(current_device_def['Settings']))
        for i, Setting in enumerate(current_device_def['Settings']):
            Settingitem = QTableWidgetItem(Setting['name'])
            Settingitem.setFlags(Settingitem.flags() & ~Qt.ItemIsEditable) # type: ignore
            self.ui.tblSettingsPreload.setItem(i,0,Settingitem)
            if current_device_decl['settings']:
                value = current_device_decl['settings'][i]
                self.ui.tblSettingsPreload.setItem(i,1,QTableWidgetItem(f"{value}"))
            else:
                self.ui.tblSettingsPreload.setItem(i,1,QTableWidgetItem("0"))
        if current_device_decl['simscale']:
            self.ui.spnSimScale.setValue(current_device_decl['simscale']*100)
        else:
            self.ui.spnSimScale.setValue(0)
        if current_device_decl['status01']:
            self.ui.spnStatus01.setValue(current_device_decl['status01'])
        else:
            self.ui.spnStatus01.setValue(0)
        if current_device_decl['status02']:
            self.ui.spnStatus02.setValue(current_device_decl['status02'])
        else:
            self.ui.spnStatus02.setValue(0)
        self.ui.spnStatus01.setDisabled(current_device_def['Status01']==[])
        self.ui.spnStatus02.setDisabled(current_device_def['Status02']==[])
        self.ui.cmbLink.clear()
        self.ui.cmbLink.addItem("--None--")
        self.ui.cmbLink.setItemData(0, None)
        for i,DevItem in enumerate(self.get_all_tree_items(self.ui.treeDevices)):
            self.ui.cmbLink.addItem(DevItem.text(0))
            self.ui.cmbLink.setItemData(i+1, DevItem.text(1))
        if current_device_decl['link']:
            self.ui.cmbLink.setCurrentText(current_device_decl['link'])
        else:
            self.ui.cmbLink.setCurrentText("--None--")
        self.ui.txtNewDevice.setText(item.text(0))
        self.ui.cmbDevTypeConfig.setCurrentText(current_device_decl['type'])
        if current_device_decl['parent']:
            self.ui.cmbParent.setCurrentText(current_device_decl['parent'])
        else:
            self.ui.cmbParent.setCurrentText("--None--")
        self.ui.lblCurrentAddress.setText(f"{current_device_decl['address']+400000}")
        self.ui.lblAddrLength.setText(f"{current_device_def['Registers']}")
    
    def disbale_place_controls(self, state):
        self.ui.txtNewPlace.setDisabled(state)
        self.ui.txtPlaceAlias.setDisabled(state)
        self.ui.btnAddPlace.setDisabled(state)
        self.ui.btnRemovePlace.setDisabled(state)
        self.ui.btnRenamePlace.setDisabled(state)
        self.ui.btnPlaceDn.setDisabled(state)
        self.ui.btnPlaceUp.setDisabled(state)
        
    def disable_device_controls(self, state):
        self.ui.txtNewDevice.setDisabled(state)
        self.ui.cmbDevTypeConfig.setDisabled(state)
        self.ui.cmbParent.setDisabled(state)
        self.ui.btnAddDevice.setDisabled(state)
        self.ui.btnRemoveDevice.setDisabled(state)
        self.ui.btnRenameDevice.setDisabled(state)
        self.ui.btnDeviceDn.setDisabled(state)
        self.ui.btnDeviceUp.setDisabled(state)
        
    def clear_place_controls(self):
        self.ui.txtNewPlace.clear()
        self.ui.txtPlaceAlias.clear()
        
    def clear_device_controls(self):
        self.ui.txtNewDevice.clear()
        #self.ui.cmbDevTypeConfig.clear()
        self.ui.cmbParent.clear()
    
    def on_add_place_button_clicked(self):
        if (self.ui.txtNewPlace.text() != "") and (self.ui.txtPlaceAlias.text() != ""):
            new_place = self.ui.txtNewPlace.text()
            new_place_alias = self.ui.txtPlaceAlias.text()
            if new_place_alias in self.PlacesDecl:
                QMessageBox.warning(self, "Warning", "Place Alias already exists !")
            else:
                place_address = self.PlantDef['AddressCount']
                place_registers = self.DevicesDef['Root']['Registers']
                self.PlacesDecl[new_place_alias] = {new_place_alias:{"name":new_place,"address":place_address,"parent":None,"type":"Root","link":None,"status01":None,"status02":None,"analog":None,"settings":None,"simscale":0.75}}
                self.PlantDef['AddressCount'] += place_registers
                self.ui.lblAvilableAddress.setText(f"{self.PlantDef['AddressCount']+400000}")
                self.load_Places(self.PlacesDecl)
                self.ui.txtNewPlace.clear()
                self.ui.txtPlaceAlias.clear()
        else:
           QMessageBox.warning(self, "Warning", "Please enter the Place Name and Alias !")
            
    
    def on_remove_place_button_clicked(self):
        if self.ui.lstPlaces.currentItem():
            response = QMessageBox.warning(self, "Warning", "Are you sure you want to remove this Place ?",QMessageBox.Yes | QMessageBox.No)# type: ignore
            if response == QMessageBox.Yes:# type: ignore
                place = self.ui.lstPlaces.currentItem().data(Qt.UserRole) # type: ignore
                del self.PlacesDecl[place]
                self.load_Places(self.PlacesDecl)
                self.ui.treeDevices.clear()
                self.clear_definitions()
                self.clear_place_controls()
    
    def replace_key(self,dict, old_key, new_key):
        new_dict = {}
        for key, value in dict.items():
            if key == old_key:
                new_dict[new_key] = value
            else:
                new_dict[key] = value
        return new_dict
    
    def move_key(self,input_dict, key, position):
        value = input_dict.pop(key)
        items = list(input_dict.items())
        items.insert(position, (key, value))
        new_dict = dict(items)
        return new_dict
    
    def swap_keys(self,input_dict, key1, key2):
        keys = list(input_dict.keys())
        index1, index2 = keys.index(key1), keys.index(key2)
        keys[index1], keys[index2] = keys[index2], keys[index1]
        return {key: input_dict[key] for key in keys}
    
    def reconfigure(self,source_dict):
        new_dict = {}
        added_keys = set()
        # First add all the objects which parent = None
        for key, value in source_dict.items():
            if value.get('parent') is None:
                new_dict[key] = value
                added_keys.add(key)
        # Then add the objects whose parent exists in the new_dict
        while len(added_keys) < len(source_dict):
            for key, value in source_dict.items():
                if key not in added_keys and value.get('parent') in new_dict:
                    new_dict[key] = value
                    added_keys.add(key)
        return new_dict
    
    def on_rename_place_button_clicked(self):
        if self.ui.lstPlaces.currentItem():
            place_alias = self.ui.lstPlaces.currentItem().data(Qt.UserRole) # type: ignore
            new_place = self.ui.txtNewPlace.text()
            new_place_alias = self.ui.txtPlaceAlias.text()
            if new_place == "":
                QMessageBox.warning(self, "Warning", "Please enter the Place Name !")
            else:
                if new_place_alias == "":
                    new_place_alias = place_alias
                if new_place_alias == place_alias:
                    self.PlacesDecl[place_alias][place_alias]['name'] = new_place
                    self.load_Places(self.PlacesDecl)
                    self.clear_place_controls()
                else:
                    self.PlacesDecl = self.replace_key(self.PlacesDecl,place_alias,new_place_alias)
                    self.PlacesDecl[new_place_alias] = self.replace_key(self.PlacesDecl[new_place_alias],place_alias,new_place_alias)
                    self.PlacesDecl[new_place_alias][new_place_alias]['name'] = new_place
                    self.load_Places(self.PlacesDecl)
                    self.clear_place_controls()
                
    def on_place_up_button_clicked(self):
        if self.ui.lstPlaces.currentItem():
            place = self.ui.lstPlaces.currentItem().data(Qt.UserRole) # type: ignore
            index = self.ui.lstPlaces.currentRow()
            if index > 0:
                self.PlacesDecl = self.move_key(self.PlacesDecl,place,index-1)
                self.load_Places(self.PlacesDecl)
                self.ui.lstPlaces.setCurrentRow(index-1)
    
    def on_place_down_button_clicked(self):
        if self.ui.lstPlaces.currentItem():
            place = self.ui.lstPlaces.currentItem().data(Qt.UserRole) # type: ignore
            index = self.ui.lstPlaces.currentRow()
            if index < self.ui.lstPlaces.count()-1:
                self.PlacesDecl = self.move_key(self.PlacesDecl,place,index+1)
                self.load_Places(self.PlacesDecl)
                self.ui.lstPlaces.setCurrentRow(index+1)
                
    def on_add_device_button_clicked(self):
        device_name = self.ui.txtNewDevice.text()
        if device_name == "":
            QMessageBox.warning(self, "Warning", "Please enter the Device Name !")
            return
        device_type = self.ui.cmbDevTypeConfig.currentText()
        if device_type == "Root":
            QMessageBox.warning(self, "Warning", "Cannot add another Root Device !")
            return
        device_parent = self.ui.cmbParent.currentText()
        if device_parent == "--None--":
            device_parent = None
        device_place_alias = self.ui.lstPlaces.currentItem().data(Qt.UserRole)# type: ignore
        if device_parent:
            device_alias = device_parent + "_" + device_name
        else:
            device_alias = device_name
        device_alias = device_alias.replace(" ","_")
        if device_alias in self.PlacesDecl[device_place_alias]:
            QMessageBox.warning(self, "Warning", "Device Alias already exists !")
            return
        device_address = self.PlantDef['AddressCount']
        device_registers = self.DevicesDef[device_type]['Registers']
        self.PlacesDecl[device_place_alias][device_alias] = {"name":device_name,"address":device_address,"parent":device_parent,"type":device_type,"link":None,"status01":None,"status02":None,"analog":None,"settings":None,"simscale":0.75}
        self.PlantDef['AddressCount'] += device_registers
        self.ui.lblAvilableAddress.setText(f"{self.PlantDef['AddressCount']+400000}")
        self.PlacesDecl[device_place_alias] = self.reconfigure(self.PlacesDecl[device_place_alias])
        self.on_place_item_clicked(self.ui.lstPlaces.currentItem())
    
    def on_remove_device_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            response = QMessageBox.warning(self, "Warning", "Are you sure you want to remove this Device ?",QMessageBox.Yes | QMessageBox.No)# type: ignore
            if response == QMessageBox.Yes:# type: ignore
                device_alias = self.ui.treeDevices.currentItem().text(1)
                place_alias = self.ui.lstPlaces.currentItem().data(Qt.UserRole)# type: ignore
                if device_alias == place_alias:
                    QMessageBox.warning(self, "Warning", "Cannot remove the Root Device !")
                    return
                if self.ui.treeDevices.currentItem().childCount() > 0:
                    for i in range(self.ui.treeDevices.currentItem().childCount()):
                        child_alias = self.ui.treeDevices.currentItem().child(i).text(1)
                        del self.PlacesDecl[place_alias][child_alias]
                del self.PlacesDecl[place_alias][device_alias] # type: ignore
                self.PlacesDecl[place_alias] = self.reconfigure(self.PlacesDecl[place_alias]) # type: ignore
                self.on_place_item_clicked(self.ui.lstPlaces.currentItem())
                
    def on_rename_device_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            #Gather Data
            device_alias = self.ui.treeDevices.currentItem().text(1)
            device_type = self.get_current_device_decl()['type']
            new_device_name = self.ui.txtNewDevice.text()
            if new_device_name == "":
                QMessageBox.warning(self, "Warning", "Please enter the Device Name !")
                return
            new_device_type = self.ui.cmbDevTypeConfig.currentText()
            new_device_parent = self.ui.cmbParent.currentText()
            if new_device_parent == "--None--":
                new_device_parent = None
            device_place_alias = self.ui.lstPlaces.currentItem().data(Qt.UserRole)# type: ignore
            if device_alias == device_place_alias:
                QMessageBox.warning(self, "Warning", "Cannot change the Root Device !")
                return
            if new_device_parent:
                new_device_alias = new_device_parent + "_" + new_device_name
            else:
                new_device_alias = new_device_name
            new_device_alias = new_device_alias.replace(" ","_")
            old_addr_length = self.DevicesDef[device_type]['Registers']
            new_addr_length = self.DevicesDef[new_device_type]['Registers']
            #Process Data
            #Block changing the device type with different lengths to get rid of address conflicts
            if old_addr_length != new_addr_length:
                QMessageBox.warning(self, "Warning", "Device Type of different lengths cannot be changed !")
                return
            if new_device_alias in self.PlacesDecl[device_place_alias]:
                QMessageBox.warning(self, "Warning", "Device Alias already exists !\nPlease change name.")
                return
            #This will not run
            if new_device_alias == device_alias:
                self.PlacesDecl[device_place_alias][device_alias]['name'] = new_device_name
                self.PlacesDecl[device_place_alias][device_alias]['type'] = new_device_type
                self.PlacesDecl[device_place_alias][device_alias]['parent'] = new_device_parent
            else:
                #Only This Will run
                if self.ui.treeDevices.currentItem().childCount() > 0:
                    for i in range(self.ui.treeDevices.currentItem().childCount()):
                        child_alias = self.ui.treeDevices.currentItem().child(i).text(1)
                        new_child_alias = child_alias.replace(device_alias,new_device_alias)
                        self.PlacesDecl[device_place_alias] = self.replace_key(self.PlacesDecl[device_place_alias],child_alias,new_child_alias)
                        self.PlacesDecl[device_place_alias][new_child_alias]['parent'] = new_device_alias
                self.PlacesDecl[device_place_alias] = self.replace_key(self.PlacesDecl[device_place_alias],device_alias,new_device_alias)
                self.PlacesDecl[device_place_alias][new_device_alias]['name'] = new_device_name
                self.PlacesDecl[device_place_alias][new_device_alias]['type'] = new_device_type
                self.PlacesDecl[device_place_alias][new_device_alias]['parent'] = new_device_parent
            if device_type != new_device_type:
                #This Will run only if the address length is equal
                self.PlacesDecl[device_place_alias][new_device_alias]['link'] = None
                self.PlacesDecl[device_place_alias][new_device_alias]['status01'] = None
                self.PlacesDecl[device_place_alias][new_device_alias]['status02'] = None
                self.PlacesDecl[device_place_alias][new_device_alias]['analog'] = None
                self.PlacesDecl[device_place_alias][new_device_alias]['settings'] = None
                self.PlacesDecl[device_place_alias][new_device_alias]['simscale'] = 0.75
            self.PlacesDecl[device_place_alias] = self.reconfigure(self.PlacesDecl[device_place_alias])
            self.on_place_item_clicked(self.ui.lstPlaces.currentItem())
    
    def on_device_up_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            #check if the device is a top level item
            if self.ui.treeDevices.currentItem().parent() == None:
                device = self.ui.treeDevices.currentItem().text(1)
                index = self.ui.treeDevices.currentIndex().row()
                if index > 0:
                    self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)] = self.move_key(self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)],device,index-1) # type: ignore
            else:
                #check if there is a child item before the selected item
                childIndex = self.ui.treeDevices.currentItem().parent().indexOfChild(self.ui.treeDevices.currentItem())
                if childIndex > 0:
                    #move the child item up
                    current_device = self.ui.treeDevices.currentItem().text(1)
                    prev_device = self.ui.treeDevices.currentItem().parent().child(childIndex-1).text(1)
                    #swap the keys
                    self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)] = self.swap_keys(self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)],current_device,prev_device) # type: ignore
            self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)] = self.reconfigure(self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)]) # type: ignore
            self.on_place_item_clicked(self.ui.lstPlaces.currentItem())
            
    def on_device_down_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            #check if the device is a top level item
            if self.ui.treeDevices.currentItem().parent() == None:
                device = self.ui.treeDevices.currentItem().text(1)
                index = self.ui.treeDevices.currentIndex().row()
                if index < self.ui.treeDevices.topLevelItemCount()-1:
                    self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)] = self.move_key(self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)],device,index+1) # type: ignore
            else:
                #check if there is a child item after the selected item
                childCount = self.ui.treeDevices.currentItem().parent().childCount()
                childIndex = self.ui.treeDevices.currentItem().parent().indexOfChild(self.ui.treeDevices.currentItem())
                if childIndex < childCount-1:
                    #move the child item down
                    current_device = self.ui.treeDevices.currentItem().text(1)
                    next_device = self.ui.treeDevices.currentItem().parent().child(childIndex+1).text(1)
                    #swap the keys
                    self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)] = self.swap_keys(self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)],current_device,next_device) # type: ignore
            self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)] = self.reconfigure(self.PlacesDecl[self.ui.lstPlaces.currentItem().data(Qt.UserRole)]) # type: ignore
            self.on_place_item_clicked(self.ui.lstPlaces.currentItem())
        
    def on_update_analog_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            if self.ui.tblAnalogPreload.rowCount() > 0:
                analog_values = []
                for i in range(self.ui.tblAnalogPreload.rowCount()):
                    item = self.ui.tblAnalogPreload.item(i, 1)
                    if item is not None:
                        analog_values.append(item.text())
                    else:
                        analog_values.append('0')
                if analog_values != ['0']*self.ui.tblAnalogPreload.rowCount():
                    self.get_current_device_decl()['analog'] = [float(value) for value in analog_values]
                else:
                    self.get_current_device_decl()['analog'] = None

    def on_update_settings_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            if self.ui.tblSettingsPreload.rowCount() > 0:
                settings_values = []
                for i in range(self.ui.tblSettingsPreload.rowCount()):
                    item = self.ui.tblSettingsPreload.item(i, 1)
                    if item is not None:
                        settings_values.append(item.text())
                    else:
                        settings_values.append('0')
                if settings_values != ['0']*self.ui.tblSettingsPreload.rowCount():
                    self.get_current_device_decl()['settings'] = [float(value) for value in settings_values]
                else:
                    self.get_current_device_decl()['settings'] = None
    
    def on_update_others_button_clicked(self):
        if self.ui.treeDevices.currentItem():
            self.get_current_device_decl()['simscale'] = self.ui.spnSimScale.value()/100
            if self.ui.spnStatus01.value() > 0:
                self.get_current_device_decl()['status01'] = self.ui.spnStatus01.value()
            else:
                self.get_current_device_decl()['status01'] = None 
            if self.ui.spnStatus02.value() > 0:
                self.get_current_device_decl()['status02'] = self.ui.spnStatus02.value()
            else:
                self.get_current_device_decl()['status02'] = None
            if self.ui.cmbLink.currentText() == "--None--":
                self.get_current_device_decl()['link'] = None
            else:
                self.get_current_device_decl()['link'] = self.ui.cmbLink.currentText()
    
    def on_reseq_address_button_clicked(self):
        passwd = QInputDialog.getText(self, 'Password', 'Please Enter the password:', QLineEdit.Password)# type: ignore
        if passwd == ('1111', True):
            if self.ui.lstPlaces.count() > 0:
                addressCount:int = 0
                for place in self.PlacesDecl:
                    for device in self.PlacesDecl[place]:
                        devType = self.PlacesDecl[place][device]['type']
                        addressLen = self.DevicesDef[devType]['Registers']
                        self.PlacesDecl[place][device]['address'] = addressCount
                        addressCount += addressLen
                self.ui.lblAvilableAddress.setText(f"{addressCount + 400000}")
                self.PlantDef['AddressCount'] = addressCount
                
    def closeEvent(self, event):
        if self.ui.btnSave.isEnabled():
            response = QMessageBox.question(self, 'Exit', "Do you want to save the changes?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)# type: ignore
            if response == QMessageBox.Yes:# type: ignore
                Helper.saveJson("places.json",self.PlacesDecl)
                Helper.saveJson("project.json",self.PlantDef)
                        
  
if __name__ == '__main__': 
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()