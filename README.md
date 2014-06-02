HumanConnectors
===============

The idea of human connector is to be able to crowd-connect remote devices by the use of a community. Each sensor or group of sensor is able to connect to a nearby smart-phone user and dump a little chunk of the data he wants to transmit. Then it is the smart-phone, via the 3G that pushes the data to the internet/server. The smart-phone must be equiped with an application where the user can enable the services he believes in.

### Why ?

Because this is the best way to put back human being in the middle of what is now called the connected world. Instead of just being particles that are monitored, citizens become enablers. If the service serves the common good or at least the good of a given community, then it can offers a free asynchronous connection (which is enough for most cases). If a service becomes crappy, it loses its community and thus it connection. 

Yes, there is deep belief in collective intelligence here.

### How ?

Lets take an example. A bunch of hackers calling themselves ANTS, designed a sensor that monitor the filling of bins in recycle centers. The reasons for that can be found [here](http://anthill.github.io/6element/presentation/).

#### Example: 6element (connecting remote recycling centers)

Here is the basic schema of how it works:

![Alt text](https://rawgit.com/anthill/HumanConnectors/master/img/general_schema.svg "General schema of 6element")

Here `board B` is a small actuator (maybe a arduino nano) that has a `sensor` which measures the height of waste inside the bin and a `wireless B` solution to exchange information. It is autonomous and works on a `battery`. There are as many such device as bin in the recycling center.

`board A` is unique per recycling center and has processing capabilities (maybe a Raspberry Pie or Beagle Bone Black). It demands/receive info from `board B`, processes them and send them by chunk to smart phones in the vicinity.

There are many possibilities for each component and the optimal solution is the result of a multidimenstional optimisation problem. For each component, we need to figure out:
    - energy consumption
    - range
    - price
    - integration
    - size
    - ...

and then write a programs that tests all different combinations.

## Links

### Wireless options

In the following there is a loose list of links about wireless transmission methods (RF, IR, Bluetooth, Wifi, ...) to be examined more closely. Most of the devices seem to work well on Arduino, but what about Raspberry Pi? Some of the shields are to be connected to a full Arduino, some wireless adapters might just work with the core microcontroller.

Are there any law restrictions for using this [RF transmitter](http://ninjablocks.com/blogs/how-to/7501042-adding-rf-433mhz-to-your-arduino) in europe?

[IR LED](http://www.adafruit.com/products/387) + [IR Sensor](http://www.adafruit.com/products/157)

[Bluetooth transceiver](http://www.instructables.com/id/Cheap-2-Way-Bluetooth-Connection-Between-Arduino-a/step3/Wiring-the-Arduino-Bluetooth-transceiver/)

[Bluefruit Bluetooth adapter](http://www.adafruit.com/product/1697)

[Seeed Bluetooth Shield](http://www.seeedstudio.com/depot/bluetooth-shield-p-866.html?cPath=132_134)

[Self-made Bluetooth Low Energy Shield](http://www.mkroll.mobi/?page_id=386)

[Arduino Wifi Shield](http://arduino.cc/en/Main/ArduinoWiFiShield)

[Arduino BT](http://arduino.cc/en/Main/ArduinoBoardBT?from=Main.ArduinoBoardBluetooth)

### Arduino power consumption links

[Run Arduino for years](http://www.openhomeautomation.net/arduino-battery/)

[Run Arduino for months](http://hwstartup.wordpress.com/2013/03/11/how-to-run-an-arduino-on-a-9v-battery-for-weeks-or-months/)

[Arduino with external power controler](http://alanbmitchell.wordpress.com/2011/10/02/operate-arduino-for-year-from-batteries/)

[Power saving techniques](http://www.gammon.com.au/forum/?id=11497)

[Arduino low power and RF transmitter with code](https://github.com/petervojtek/diy/wiki/Arduino-with-Very-Low-Power-Consumption)

[Solar module](http://www.voltaicsystems.com/solar-arduino-guide.shtml)
