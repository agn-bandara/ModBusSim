# ModBusSim

A graphical Modbus TCP simulator and device configuration tool built with PySide6 and pymodbus 3.x.

## Features

- **Modbus TCP Server**
  - Simulates a Modbus TCP server with configurable registers.
  - Supports large register blocks (up to 50,000 registers).
  - Asynchronous server thread management.

- **Device Simulation**
  - Simulate various device types (motors, valves, sensors, PID controllers, power systems, etc.).
  - Realistic analog, status, and control register behavior.
  - Device linking and hierarchical relationships.

- **Graphical User Interface**
  - Built with PySide6 (Qt for Python).
  - Tree-based device and place management.
  - Table-based analog and settings editing.
  - Checkbox controls for status and control bits.
  - Real-time value updates and simulation toggling.

- **Project & Device Configuration**
  - Load/save project, device, and place definitions as JSON.
  - Add, remove, rename, and reorder places and devices.
  - Configure device types, parents, links, and addresses.
  - Preload analog, settings, and status values.

- **Advanced Register Types**
  - Support for Int, Signed Int, Long, Float, and their inverse variants.
  - Bitwise operations and array manipulation.

- **Helper Utilities**
  - IP address detection.
  - JSON beautification and backup.
  - Mathematical rounding helpers.

- **Extensible Simulation Objects**
  - Easily add new device simulation logic via the `SimObjects` module.

## Requirements

- Python 3.8+
- PySide6 >= 6.0.0
- pymodbus >= 3.0.0
- numpy
- jsbeautifier
- pympler

## Getting Started

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the simulator**
   ```bash
   python Nuwans_ModBus_Sim2_v001.py
   ```

## Project Structure

- `Nuwans_ModBus_Sim2_v001.py` — Main application code
- `UI.py` — PySide6 UI definitions
- `ConfigDialog.py` — Configuration dialog UI
- `SimObjects.py` — Device simulation logic
- `project.json`, `devices.json`, `places.json` — Configuration files

## Usage

- Start the application and configure your devices and places.
- Use the GUI to simulate device behavior and interact with Modbus registers.
- Connect external Modbus clients to `localhost:502` to read/write simulated data.

## Extending

- Add new device types and simulation logic in `SimObjects.py`.
- Customize device definitions in `devices.json`.

## License

This project is open source.
You are free to use, modify, and distribute it under the terms of the [MIT License](LICENSE).
