# obd-subaru

live obd2 data

# ELM327 Emulation for local testing

https://github.com/Ircama/ELM327-emulator

D. Cashon



~~~
python -m venv ./env
source ./env/bin/activate
pip install -r requirements.txt
~~~


<details>

<summary> python-odb </summary>

python-OBD
==========

A python module for handling realtime sensor data from OBD-II vehicle
ports. Works with ELM327 OBD-II adapters, and is fit for the Raspberry
Pi.

Installation
------------

```Shell
$ pip install obd
```

Basic Usage
-----------

```Python
import obd

connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.SPEED # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
print(response.value.to("mph")) # user-friendly unit conversions
```

Documentation
-------------

Available at [python-obd.readthedocs.org](http://python-obd.readthedocs.org/en/latest/)

Commands
--------

Here are a handful of the supported commands (sensors). For a full list, see [the docs](http://python-obd.readthedocs.io/en/latest/Command%20Tables/)

*note: support for these commands will vary from car to car*

-   Calculated Engine Load
-   Engine Coolant Temperature
-   Fuel Pressure
-   Intake Manifold Pressure
-   Engine RPM
-   Vehicle Speed
-   Timing Advance
-   Intake Air Temp
-   Air Flow Rate (MAF)
-   Throttle Position
-   Engine Run Time
-   Fuel Level Input
-   Number of warm-ups since codes cleared
-   Barometric Pressure
-   Ambient air temperature
-   Commanded throttle actuator
-   Time run with MIL on
-   Time since trouble codes cleared
-   Hybrid battery pack remaining life
-   Engine fuel rate
-   Vehicle Identification Number (VIN)

Common Issues
-------------

### Bluetooth OBD-II Adapters

There are sometimes connection issues when using a Bluetooth OBD-II adapter with some devices (the Raspberry Pi is a common problem). This can be fixed by setting the following arguments when setting up the connection:

```Python
fast=False, timeout=30
```

License
-------

GNU GPL v2

This library is forked from:

-   <https://github.com/peterh/pyobd>
-   <https://github.com/Pbartek/pyobd-pi>

Enjoy and drive safe!
</details>
