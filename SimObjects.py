import asyncio
import random
import math
import sys

class SimObj_MotorVSD:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.running_status = None
        self.update_values_task = None
        self.update_busV_task = None
        self.ref_Values = [0]*len(self.device.Analog)
        for i in range(1,len(self.device.Analog)):
            self.ref_Values[i] = self.device.Analog[i].Value

    async def simulate(self):
        # Run Command
        if self.device.Control01.GetBit(0) == 1:
            self.ref_Values[1] = self.device.Analog[1].Value
            self.device.Status01.SetBit(0,1)
            self.running_status = True
        # Stop Command
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status01.SetBit(0,0)
        # Reset Fault
        if self.device.Control01.GetBit(2) == 1:
            self.device.Status01.SetArray(0,2,0b000)
        # Set Speed
        if self.device.Control01.GetBit(3) == 1:
            self.ref_Values[1] = self.device.Analog[1].Value
        # PID Control ON
        if self.device.Control01.GetBit(5) == 1:
            self.device.Status02.SetArray(8,10,0b001)
        # PID Control OFF
        if self.device.Control01.GetBit(6) == 1:
            self.device.Status02.SetArray(8,10,0b100)
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
        # Set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        # Set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #Scheduler Run
        if self.device.Control01.GetBit(14) == 1:
            self.ref_Values[1] = self.device.Analog[1].Value
            self.device.Status01.SetBit(0,1)
            self.running_status = True
        #Scheduler Stop
        if self.device.Control01.GetBit(15) == 1:
            self.device.Status01.SetBit(0,0)
            self.running_status = False
        # Simulate Running Status
        if self.device.Status01.GetBit(0) == 1 and self.ref_Values[1] > 0:
            if self.update_values_task is None or self.update_values_task.done():
                self.update_values_task = asyncio.create_task(self.update_values())
        # Simulate Stopped Status
        if self.device.Status01.GetBit(0) == 0 and self.running_status == True:
            self.device.Analog[0].Value = 0
            self.Restore()
            self.running_status = False
        #Simulate Bus Voltage
        if self.update_busV_task is None or self.update_busV_task.done():
            self.update_busV_task = asyncio.create_task(self.update_busV())
        
    def Restore(self):
        for i in range(2,len(self.device.Analog)):
            self.device.Analog[i].Value = self.ref_Values[i]

    async def update_values(self):
        self.device.Analog[0].Value = self.ref_Values[1] + random.uniform(-0.1,0.1)
        for i in range(2,len(self.device.Analog)-1):
            if self.ref_Values[i] > 0:
                self.device.Analog[i].Value = self.ref_Values[i] + self.ref_Values[i]*random.uniform(-self.simScale,self.simScale)
        await asyncio.sleep(2)
        
    async def update_busV(self):
        if self.ref_Values[len(self.device.Analog)-1] > 0:
            self.device.Analog[len(self.device.Analog)-1].Value = self.ref_Values[len(self.device.Analog)-1] + self.ref_Values[len(self.device.Analog)-1]*random.uniform(-self.simScale,self.simScale)
        await asyncio.sleep(2)
        

class SimObj_MotorNormal:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale

    async def simulate(self):
        # Run Command
        if self.device.Control01.GetBit(0) == 1:
            self.device.Status01.SetBit(0,1)
        # Stop Command
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status01.SetBit(0,0)
        # Reset Fault
        if self.device.Control01.GetBit(2) == 1:
            self.device.Status01.SetArray(0,2,0b000)
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
        # Set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        # Set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #Scheduler Run
        if self.device.Control01.GetBit(14) == 1:
            self.device.Status01.SetBit(0,1)
        #Scheduler Stop
        if self.device.Control01.GetBit(15) == 1:
            self.device.Status01.SetBit(0,0)
            self.running_status = False
            
    def Restore(self):
        pass
    
    
class SimObj_ValveMOV:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.valve_open_task = None
        self.valve_close_task = None

    async def simulate(self):
        # Open Command
        if self.device.Control01.GetBit(0) == 1 and self.device.Status01.GetBit(1) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.open_command()
        # Close Command
        if self.device.Control01.GetBit(1) == 1 and self.device.Status01.GetBit(0) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.close_command()
        # Stop Command
        if self.device.Control01.GetBit(2) == 1 and self.device.Status01.GetArray(2,3) != 0b00:
            self.device.Status01.SetArray(2,3,0b00)
            if self.valve_open_task:
                self.valve_open_task.cancel()
                self.valve_open_task = None
            if self.valve_close_task:
                self.valve_close_task.cancel()
                self.valve_close_task = None
        # Reset Fault
        if self.device.Control01.GetBit(3) == 1:
            self.device.Status01.SetArray(4,5,0b00)
            if self.device.Status01.GetBit(0) == 0:
                self.close_command()
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
        # Set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        # Set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #Scheduler Open
        if self.device.Control01.GetBit(14) == 1 and self.device.Status01.GetBit(1) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.open_command()
        #Scheduler Close
        if self.device.Control01.GetBit(15) == 1 and self.device.Status01.GetBit(0) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.close_command()
            
    def Restore(self):
        pass
    
    def open_command(self):
        if self.valve_open_task is None or self.valve_open_task.done():
            self.valve_open_task = asyncio.create_task(self.valve_open())
            
    def close_command(self):
        if self.valve_close_task is None or self.valve_close_task.done():
            self.valve_close_task = asyncio.create_task(self.valve_close())
    
    async def valve_open(self):
        self.device.Status01.SetBit(0,0)
        self.device.Status01.SetArray(2,3,0b10)
        await asyncio.sleep(5)
        self.device.Status01.SetBit(3,0)
        self.device.Status01.SetArray(0,1,0b10)
    
    async def valve_close(self):
        self.device.Status01.SetBit(1,0)
        self.device.Status01.SetArray(2,3,0b01)
        await asyncio.sleep(5)
        self.device.Status01.SetBit(2,0)
        self.device.Status01.SetArray(0,1,0b01)
        
class SimObj_ValveModulating:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.valve_set_angle_task = None

    async def simulate(self):
        # Open Command
        if self.device.Control01.GetBit(0) == 1 and self.device.Status01.GetBit(1) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.device.Analog[0].Value = 100
            self.set_angle_command()
        # Close Command
        if self.device.Control01.GetBit(1) == 1 and self.device.Status01.GetBit(0) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.device.Analog[0].Value = 0
            self.set_angle_command()
        # Fully Open Signal
        if self.device.Analog[1].Value == 100:
            self.device.Status01.SetBit(1,1)
        else:
            self.device.Status01.SetBit(1,0)
        # Fully Close Signal
        if self.device.Analog[1].Value == 0:
            self.device.Status01.SetBit(0,1)
        else:
            self.device.Status01.SetBit(0,0)
        # Stop Command
        if self.device.Control01.GetBit(2) == 1 and self.device.Status01.GetArray(2,3) != 0b00:
            self.device.Status01.SetBit(3,0)
            if self.valve_set_angle_task:
                self.valve_set_angle_task.cancel()
                self.valve_set_angle_task = None
        # Reset Fault
        if self.device.Control01.GetBit(3) == 1:
            self.device.Status01.SetBit(4,0)
            if self.valve_set_angle_task:
                self.valve_set_angle_task.cancel()
                self.valve_set_angle_task = None
            self.device.Analog[0].Value = 0
            self.set_angle_command()
        # Set Ref Angle
        if self.device.Control01.GetBit(4) == 1:
            self.set_angle_command()
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
        # Set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        # Set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #Scheduler Open
        if self.device.Control01.GetBit(14) == 1 and self.device.Status01.GetBit(1) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.device.Analog[0].Value = 100
            self.set_angle_command()
        #Scheduler Close
        if self.device.Control01.GetBit(15) == 1 and self.device.Status01.GetBit(0) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.device.Analog[0].Value = 0
            self.set_angle_command()
            
    def Restore(self):
        pass
            
    def set_angle_command(self):
        if self.valve_set_angle_task is None or self.valve_set_angle_task.done():
            self.valve_set_angle_task = asyncio.create_task(self.valve_set_angle())
        
    async def valve_set_angle(self):
        end_angle = int(self.device.Analog[0].Value*10)
        start_angle = int(self.device.Analog[1].Value*10)
        self.device.Status01.SetBit(3,1)
        if start_angle > end_angle:
            step = -10
        else:
            step = 10
        for i in range(start_angle, end_angle, step):
            self.device.Analog[1].Value = i/10.0
            await asyncio.sleep(1)
        self.device.Analog[1].Value = end_angle/10.0
        self.device.Status01.SetBit(3,0)
        
class SimObj_ValveSolenoid:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        
    async def simulate(self):
        # Open Command
        if self.device.Control01.GetBit(0) == 1 and self.device.Status01.GetBit(1) == 0:
            self.device.Status01.SetArray(0,1,0b10)
        # Close Command
        if self.device.Control01.GetBit(1) == 1 and self.device.Status01.GetBit(0) == 0:
            self.device.Status01.SetArray(0,1,0b01)
        # Reset Fault
        if self.device.Control01.GetBit(3) == 1:
            self.device.Status01.SetArray(4,5,0b00)
            self.device.Status01.SetArray(0,1,0b01)
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
        # Set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        # Set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #Scheduler Open
        if self.device.Control01.GetBit(14) == 1 and self.device.Status01.GetBit(1) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.device.Status01.SetArray(0,1,0b10)
        #Scheduler Close
        if self.device.Control01.GetBit(15) == 1 and self.device.Status01.GetBit(0) == 0 and self.device.Status01.GetArray(2,3) == 0b00:
            self.device.Status01.SetArray(0,1,0b01)
            
    def Restore(self):
        pass
    

class SimObj_SensorLevel:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.LevelRef = device.Analog[0].Value
        self.scale = 25
        self.counter = 0
        self.countForward = True
        self.update_values_task = None
    
    async def simulate(self):
        # Set Level
        if self.update_values_task is None or self.update_values_task.done():
            self.update_values_task = asyncio.create_task(self.update_values())
        # Set LL
        if self.device.Analog[0].Value > self.device.Settings[0].Value:
            self.device.Status01.SetBit(0,1)
        else:
            self.device.Status01.SetBit(0,0)
        # Set LH
        if self.device.Analog[0].Value > self.device.Settings[1].Value:
            self.device.Status01.SetBit(1,1)
        else:
            self.device.Status01.SetBit(1,0)
        # Set HL
        if self.device.Analog[0].Value > self.device.Settings[2].Value:
            self.device.Status01.SetBit(2,1)
        else:
            self.device.Status01.SetBit(2,0)
        # Set HH
        if self.device.Analog[0].Value > self.device.Settings[3].Value:
            self.device.Status01.SetBit(3,1)
        else:
            self.device.Status01.SetBit(3,0)
    
    def Restore(self):
        self.device.Analog[0].Value = self.LevelRef
            
    async def update_values(self):
        if self.countForward:
            self.counter += 1
        else:
            self.counter -= 1
            
        if self.counter >= self.scale:
            self.countForward = False
        if self.counter <= -self.scale:
            self.countForward = True
            
        self.device.Analog[0].Value = self.LevelRef + self.LevelRef*self.simScale * float(self.counter/self.scale)
        await asyncio.sleep(2)
        
        
class SimObj_SensorTotalizing:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.valueRef = device.Analog[0].Value
        self.totRef = device.Analog[1].Value
        self.update_values_task = None
        
    async def simulate(self):
        # Set Value
        if self.update_values_task is None or self.update_values_task.done():
            self.update_values_task = asyncio.create_task(self.update_values())
            
    def Restore(self):
        self.device.Analog[0].Value = self.valueRef
        self.device.Analog[1].Value = self.totRef
    
    async def update_values(self): 
        self.device.Analog[0].Value = self.valueRef + self.valueRef*self.simScale * random.uniform(-self.simScale,self.simScale)
        self.device.Analog[1].Value = self.device.Analog[1].Value + int(self.device.Analog[0].Value/36)
        await asyncio.sleep(2)
        
        
class SimObj_SensorAnalog:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.valueRef = device.Analog[0].Value
        self.update_values_task = None
        
    async def simulate(self):
        # Set Value
        if self.update_values_task is None or self.update_values_task.done():
            self.update_values_task = asyncio.create_task(self.update_values())
            
    def Restore(self):
        self.device.Analog[0].Value = self.valueRef
    
    async def update_values(self):
        self.device.Analog[0].Value = self.valueRef + self.valueRef*self.simScale * random.uniform(-self.simScale,self.simScale)
        await asyncio.sleep(2)
        

class SimObj_PIDControl:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.pv = device.Analog[0].Value
        self.sp = device.Analog[1].Value
        self.out = device.Analog[2].Value
        self.update_values_task = None
        
    async def simulate(self):
        # Set Active Setpoint
        if self.device.Status01.GetBit(13) == 1:
            self.device.Analog[1].Value = self.device.Settings[0].Value
        elif self.device.Status01.GetBit(14) == 1:
            self.device.Analog[1].Value = self.device.Settings[1].Value
        elif self.device.Status01.GetBit(15) == 1:
            self.device.Analog[1].Value = self.device.Settings[2].Value

        # Set Value
        if self.device.Status01.GetBit(0) == 1:
            if self.update_values_task is None or self.update_values_task.done():
                self.update_values_task = asyncio.create_task(self.update_values())
        else:
            self.device.Analog[0].Value = 0
            self.device.Analog[2].Value = 0
            await asyncio.sleep(1)
                
    def Restore(self):
        self.device.Analog[0].Value = self.pv
        self.device.Analog[1].Value = self.sp
        self.device.Analog[2].Value = self.out

    async def update_values(self):
        self.device.Analog[0].Value = self.device.Analog[1].Value + self.device.Analog[1].Value * random.uniform(-0.1,0.1)
        self.device.Analog[2].Value = random.uniform(25,75)
        await asyncio.sleep(2)
        
        
class SimObj_DPA:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.values = [0]*len(self.device.Analog)
        for i in range(len(self.device.Analog)):
            self.values[i] = self.device.Analog[i].Value
        self.update_values_task = None
        
    async def simulate(self):
        # Set Value
        if self.update_values_task is None or self.update_values_task.done():
            self.update_values_task = asyncio.create_task(self.update_values())
            
    def Restore(self):
        for i in range(len(self.device.Analog)):
            self.device.Analog[i].Value = self.values[i]
    
    async def update_values(self):
        for i in range(len(self.device.Analog)):
            if self.values[i] > 0:
                if i == 18 or i == 19:
                    self.device.Analog[i].Value = self.device.Analog[i].Value + 1
                else:
                    self.device.Analog[i].Value = self.values[i] + self.values[i]*random.uniform(-self.simScale,self.simScale)
        await asyncio.sleep(2)
        
class SimObj_Generator:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.startSimAt = 3
        self.values = [0]*(len(self.device.Analog))
        for i in range(len(self.device.Analog)):
            self.values[i] = self.device.Analog[i].Value
        self.update_values_task = None
        
    async def simulate(self):
        # Set Gen Values
        if self.update_values_task is None or self.update_values_task.done():
            self.update_values_task = asyncio.create_task(self.update_values())
        # Run Command
        if self.device.Control01.GetBit(0) == 1:
            self.device.Status01.SetBit(6,1)
        # Stop Command
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status01.SetBit(6,0)
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
            
    def Restore(self):
        for i in range(self.startSimAt,len(self.device.Analog)):
            self.device.Analog[i].Value = self.values[i]
    
    async def update_values(self):
        for i in range(self.startSimAt,len(self.device.Analog)):
            if self.values[i] > 0:
                if i == 9:
                    self.device.Analog[i].Value = self.device.Analog[i].Value + 1
                else:
                    self.device.Analog[i].Value = self.values[i] + self.values[i]*random.uniform(-self.simScale,self.simScale)
        await asyncio.sleep(2)
        
class SimObj_UPS:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.values = [0]*len(self.device.Analog)
        for i in range(len(self.device.Analog)):
            self.values[i] = self.device.Analog[i].Value
        self.update_values_task = None
        
    async def simulate(self):
        # Set Value
        if self.update_values_task is None or self.update_values_task.done():
            self.update_values_task = asyncio.create_task(self.update_values())
            
    def Restore(self):
        for i in range(len(self.device.Analog)):
            self.device.Analog[i].Value = self.values[i]
    
    async def update_values(self):
        for i in range(len(self.device.Analog)):
            if self.values[i] > 0:
                self.device.Analog[i].Value = self.values[i] + self.values[i]*random.uniform(-self.simScale,self.simScale)
        await asyncio.sleep(2)
        
class SimObj_RSF:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        self.backwash_task = None
        self.filtering_task = None
        self.standby_task = None
        self.filteringCounter = 0
        self.standbyCounter = 0
        self.backwashCounter = 0
        self.pauseBackwash = False
        self.drawdownTime = self.device.Settings[0].Value
        self.airTime = self.device.Settings[1].Value
        self.airWaterTime = self.device.Settings[2].Value
        self.waterTime = self.device.Settings[3].Value
        self.standbyTime = self.device.Settings[4].Value
        self.waitTime = self.device.Settings[5]
        self.totalBackwashTime = self.drawdownTime + self.airTime + self.airWaterTime + self.waterTime
        
    async def simulate(self):
        #Startup
        if self.device.Control01.GetBit(0) == 1:
            self.device.Status01.SetArray(0,1,0b01)
            self.device.Status01.SetBit(6,0)
        #Shutdown
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status01.SetArray(0,1,0b00)
            self.device.Status01.SetBit(6,1)
        #Start Backwash
        if self.device.Control01.GetBit(2) == 1:
            if self.backwash_task is None or self.backwash_task.done():
                self.backwash_task = asyncio.create_task(self.backwash())
        #Pause Backwash
        if self.device.Control01.GetBit(3) == 1 and self.device.Status01.GetBit(1) == 1:
            self.pauseBackwash = True
            self.device.Status01.SetBit(7,1)
        #Resume Backwash
        if self.device.Control01.GetBit(4) == 1 and self.device.Status01.GetBit(1) == 1:
            self.pauseBackwash = False
            self.device.Status01.SetBit(7,0)
        #Reset Backwash
        if self.device.Control01.GetBit(5) == 1 and self.device.Status01.GetBit(1) == 1:
            self.pauseBackwash = False
            self.device.Status01.SetBit(7,0)
            self.backwashCounter = 0
            self.device.Status01.SetArray(2,6,0b00000)
        #Set Auto
        if self.device.Control01.GetBit(6) == 1:
            self.device.Status02.SetArray(0,2,0b001)
            self.device.Status02.SetArray(5,6,0b00)
        #Set SCADA Semi Auto
        if (self.device.Control01.GetBit(7) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b000)
            self.device.Status02.SetArray(5,6,0b01)
        #Set HMI Semi Auto
        if (self.device.Control01.GetBit(7) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b000)
            self.device.Status02.SetArray(5,6,0b10)
        #Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
            self.device.Status02.SetArray(5,6,0b00)
        #Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
            self.device.Status02.SetArray(5,6,0b00)
        #set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        #set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #Set Time Mode
        if self.device.Control01.GetBit(11) == 1:
            self.device.Status02.SetArray(8,10,0b001)
        #Set Level Mode
        if self.device.Control01.GetBit(12) == 1:
            self.device.Status02.SetArray(8,10,0b010)
        #Set Pressure Mode
        if self.device.Control01.GetBit(13) == 1:
            self.device.Status02.SetArray(8,10,0b100)
        #Filtering Mode
        if self.device.Status01.GetBit(0) == 1:
            if self.filtering_task is None or self.filtering_task.done():
                self.filtering_task = asyncio.create_task(self.filtering())
        #Standby Mode
        if self.device.Status01.GetArray(0,1) == 0 and self.device.Status01.GetBit(6) == 1:
            if self.standby_task is None or self.standby_task.done():
                self.standby_task = asyncio.create_task(self.standby())
        #Reset Standby
        if self.device.Status01.GetBit(6) == 0:
            self.standbyCounter = 0
            self.device.Analog[6].Value = 0
        
                
    async def backwash(self):
        self.device.Status01.SetArray(0,1,0b10)
        self.drawdownTime = self.device.Settings[0].Value
        self.airTime = self.device.Settings[1].Value
        self.airWaterTime = self.device.Settings[2].Value
        self.waterTime = self.device.Settings[3].Value
        self.standbyTime = self.device.Settings[4].Value
        self.totalBackwashTime = self.drawdownTime + self.airTime + self.airWaterTime + self.waterTime
        while self.backwashCounter <= self.totalBackwashTime:
            if self.backwashCounter <= self.drawdownTime:
                self.device.Status01.SetArray(2,6,0b00001)
                self.device.Analog[2].Value = self.backwashCounter
            elif self.backwashCounter <= self.drawdownTime + self.airTime:
                self.device.Status01.SetArray(2,6,0b00010)
                self.device.Analog[2].Value = 0
                self.device.Analog[3].Value = self.backwashCounter - self.drawdownTime
            elif self.backwashCounter <= self.drawdownTime + self.airTime + self.airWaterTime:
                self.device.Status01.SetArray(2,6,0b00100)
                self.device.Analog[3].Value = 0
                self.device.Analog[4].Value = self.backwashCounter - self.drawdownTime - self.airTime
            elif self.backwashCounter <= self.drawdownTime + self.airTime + self.airWaterTime + self.waterTime:
                self.device.Analog[4].Value = 0
                self.device.Analog[5].Value = self.backwashCounter - self.drawdownTime - self.airTime - self.airWaterTime
                self.device.Status01.SetArray(2,6,0b01000)
            if self.pauseBackwash == False:
                self.backwashCounter += 1
            await asyncio.sleep(1)
        while self.backwashCounter <= self.totalBackwashTime + self.standbyTime:
            self.device.Status01.SetArray(2,6,0b10000)
            self.device.Analog[5].Value = 0
            self.device.Analog[6].Value = self.backwashCounter - self.totalBackwashTime
            self.backwashCounter += 1
            await asyncio.sleep(1)
        self.device.Analog[6].Value = 0
        self.backwashCounter = 0
        self.filteringCounter = 0
        self.device.Status01.SetArray(0,1,0b01)
        self.device.Status01.SetBit(6,0)
        
    async def filtering(self):
        self.device.Analog[7].Value = self.filteringCounter
        self.device.Analog[8].Value = self.waitTime.Value - self.filteringCounter
        if self.filteringCounter < self.waitTime.Value:
            self.filteringCounter += 1
        await asyncio.sleep(1)
        
    async def standby(self):
        self.device.Analog[6].Value = self.standbyCounter
        if self.standbyCounter < 65000:
            self.standbyCounter += 1
        await asyncio.sleep(1)
        
    def Restore(self):
        for i in range(len(self.device.Analog)):
            self.device.Analog[i].Value = 0
            
class SimObj_ScreenPackage:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        
    async def simulate(self):
        # SV 1 Open Command
        if self.device.Control01.GetBit(0) == 1:
            self.device.Status01.SetArray(3,4,0b01)
        # SV 1 Close Command
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status01.SetArray(3,4,0b10)
        # SV 2 Open Command
        if self.device.Control01.GetBit(2) == 1:
            self.device.Status01.SetArray(9,10,0b01)
        # SV 2 Close Command
        if self.device.Control01.GetBit(3) == 1:
            self.device.Status01.SetArray(9,10,0b10)
        # Reset Fault
        if self.device.Control01.GetBit(4) == 1:
            self.device.Status01.SetBit(2,0)
            self.device.Status01.SetBit(5,0)
            self.device.Status01.SetBit(8,0)
            self.device.Status01.SetBit(11,0)
            self.device.Status01.SetArray(3,4,0b10)
            self.device.Status01.SetArray(9,10,0b10)
        # Set Auto
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(8) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
        # Set Out of Service
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetBit(15,1)
        # Set In Service
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status01.SetBit(15,0)
        #SV 1 Scheduler Open
        if self.device.Control01.GetBit(14) == 1 and self.device.Status02.GetBit(0) == 1:
            self.device.Status01.SetArray(3,4,0b01)
        #SV 1 Scheduler Open
        if self.device.Control01.GetBit(14) == 0 and self.device.Status02.GetBit(0) == 1:
            self.device.Status01.SetArray(3,4,0b10)
        #SV 2 Scheduler Open
        if self.device.Control01.GetBit(15) == 1 and self.device.Status02.GetBit(0) == 1:
            self.device.Status01.SetArray(9,10,0b01)
        #SV 2 Scheduler Open
        if self.device.Control01.GetBit(15) == 0 and self.device.Status02.GetBit(0) == 1:
            self.device.Status01.SetArray(9,10,0b10)
            
    def Restore(self):
        pass
    
class SimObj_Root:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
    
    async def simulate(self):
        # Set SCADA Active
        if self.device.Control01.GetBit(0) == 1:
            self.device.Status02.SetBit(1,1)
            self.device.Status02.SetBit(6,0)
        # Set HMI Active
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status02.SetBit(1,0)
            self.device.Status02.SetBit(6,1)
        
    def Restore(self):
        pass
    
class SimObj_VentilationFans:
    def __init__(self, device):
        self.device = device
        self.simScale = device.SimScale
        
    async def simulate(self):
        # Fan12 Run Command
        if self.device.Control01.GetBit(0) == 1:
            self.device.Status01.SetBit(0,1)
            self.device.Status01.SetBit(2,1)
        # Fan12 Stop Command
        if self.device.Control01.GetBit(1) == 1:
            self.device.Status01.SetBit(0,0)
            self.device.Status01.SetBit(2,0)
        # Fan34 Run Command
        if self.device.Control01.GetBit(2) == 1:
            self.device.Status01.SetBit(4,1)
            self.device.Status01.SetBit(6,1)
        # Fan34 Stop Command
        if self.device.Control01.GetBit(3) == 1:
            self.device.Status01.SetBit(4,0)
            self.device.Status01.SetBit(6,0)
        # Fan56 Run Command
        if self.device.Control01.GetBit(4) == 1:
            self.device.Status01.SetBit(8,1)
            self.device.Status01.SetBit(10,1)
        # Fan56 Stop Command
        if self.device.Control01.GetBit(5) == 1:
            self.device.Status01.SetBit(8,0)
            self.device.Status01.SetBit(10,0)
        # Fan78 Run Command
        if self.device.Control01.GetBit(6) == 1:
            self.device.Status01.SetBit(12,1)
            self.device.Status01.SetBit(14,1)
        # Fan78 Stop Command
        if self.device.Control01.GetBit(7) == 1:
            self.device.Status01.SetBit(12,0)
            self.device.Status01.SetBit(14,0)
        # Reset Fault
        if self.device.Control01.GetBit(9) == 1:
            self.device.Status01.SetArray(0,11,0b000000000000)
        # Set Auto
        if self.device.Control01.GetBit(10) == 1:
            self.device.Status02.SetArray(0,2,0b001)
        # Set SCADA Manual
        if (self.device.Control01.GetBit(11) == 1) and (self.device.Status02.GetBit(11) == 1):
            self.device.Status02.SetArray(0,2,0b010)
        # Set HMI Manual
        if (self.device.Control01.GetBit(11) == 1) and (self.device.Status02.GetBit(11) == 0):
            self.device.Status02.SetArray(0,2,0b100)
            
    def Restore(self):
        pass