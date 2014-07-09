HumanConnectors
===============

The idea of human connector is to be able to crowd-connect remote devices by the use of a community. Each sensor or group of sensors is able to connect to a nearby smart-phone user and dump a little chunk of the data he wants to transmit. Then it is the smart-phone, via the 3G that pushes the data to the internet/server. The smart-phone must be equiped with an application where the user can enable the services he believes in.

### Why ?

Because this is the best way to put back human beings in the middle of what is now called the connected world. Instead of just being particles that are monitored, citizens become enablers. If the service serves the common good or at least the good of a given community, then it can offer a free asynchronous connection (which is enough for most cases). If a service becomes crappy, it loses its community and thus its connection. 

Yes, there is deep belief in collective intelligence here.

### How ?

Lets take an example. A bunch of hackers calling themselves ANTS, designed a sensor that monitors the filling of bins in recycle centers. The reasons for that can be found [here](http://anthill.github.io/6element/presentation/).

#### Example: 6element (connecting remote recycling centers)

Here is the basic schema of how it works:

![Alt text](https://rawgit.com/anthill/HumanConnectors/master/img/general_schema.svg "General schema of 6element")

Here `board B` is a small actuator (maybe a arduino nano) that has a `sensor` which measures the height of waste inside the bin and a `wireless B` solution to exchange information. It is autonomous and works on a `battery`. There are as many such devices as bins in the recycling center.

`board A` is unique per recycling center and has processing capabilities (maybe a Raspberry Pie or Beagle Bone Black). It demands/receives info from `board B`, processes them and send them by chunk to smart phones in the vicinity.

There are many possibilities for each component and the optimal solution is the result of a multidimensional optimisation problem. For each component, we need to figure out:

    - energy consumption
    - range
    - price
    - integration
    - size
    - ...

and then write a program that tests all different combinations.

## Links

### Possible sensors

#### Cameras

- [Pi camera](http://www.adafruit.com/products/1367)
- [Press and shoot](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam)
- [Jpeg for adafruit](https://www.adafruit.com/products/1386)
- [Iot Cam](http://www.ladyada.net/make/IoTcamera/)

- [ov7670](http://www.arducam.com/camera-modules/0-3mp-ov7670/), [more](https://github.com/ComputerNerd/arduino-camera-tft)

[Camera](http://www.arducam.com/arducam-bluetooth-module-wireless-image-system/)

[Ultrasounds](http://www.adafruit.com/products/1137)

This [ultrasound](http://www.fasttech.com/products/0/10000007/1012007-arduino-compatible-hc-sr04-ultrasonic-sonar) sensor is extremely cheap and works together with arduino.

A specific [implementation](http://www.instructables.com/id/Arduino-dual-ultrasonic-liquid-level-meter-with-in/) is using an ultrasonic sensor together with an arduino and Xbee in order to measure the liquid level in containers.

### Wireless options

In the following there is a loose list of links about wireless transmission methods (RF, IR, Bluetooth, Wifi, ...) to be examined more closely. Most of the devices seem to work well on Arduino, but what about Raspberry Pi? Some of the shields are to be connected to a full Arduino, some wireless adapters might just work with the core microcontroller. It should also be mentioned, that in the case of Bluetooth, the [Bluetooth Low Energy](http://en.wikipedia.org/wiki/Bluetooth_low_energy) standard is particulary interesting.

[RF transmitter](http://ninjablocks.com/blogs/how-to/7501042-adding-rf-433mhz-to-your-arduino) and [this](http://conoroneill.net/arduino-and-raspberry-pi-communicating-over-2-4ghz-with-cheap-nrf24l01-modules/)

The Zigbee protokoll seems to be very interesting, as, citing from the [wikipedia article](http://en.wikipedia.org/wiki/ZigBee), it is specifically designed to be much simpler and less expensive than for example Wifi and Bluetooth. It aims especially at scenarios where battery life time is an issue. Xbee Series 2 seems to implement the Zigbee standard, as [this article](http://tutorial.cytron.com.my/2011/03/06/is-xbee-zigbee/) explains.

[Xbee](http://www.digi.com/fr/products/wireless/point-multipoint/xbee-series1-module) and [this](http://forum.arduino.cc/index.php?topic=59082.0;wap2), an example of which can be found [here](http://jeromeabel.net/fr/ressources/xbee-arduino). This sensor fits perfectly on the arduino nano.

[Xbee tutorial](http://www.cooking-hacks.com/documentation/tutorials/raspberry-pi-xbee)

[IR LED](http://www.adafruit.com/products/387) + [IR Sensor](http://www.adafruit.com/products/157)

[Bluetooth transceiver](http://www.instructables.com/id/Cheap-2-Way-Bluetooth-Connection-Between-Arduino-a/step3/Wiring-the-Arduino-Bluetooth-transceiver/)

[Bluetooth turorial](http://www.cooking-hacks.com/documentation/tutorials/raspberry-pi-bluetooth)

[Bluefruit Bluetooth adapter](http://www.adafruit.com/product/1697)

[Seeed Bluetooth Shield](http://www.seeedstudio.com/depot/bluetooth-shield-p-866.html?cPath=132_134)

[Self-made Bluetooth Low Energy Shield](http://www.mkroll.mobi/?page_id=386)

[BLE](http://www.makershed.com/BLE_Mini_Bluetooth_4_0_Interface_p/mkrbl2.htm)

[Arduino Wifi Shield](http://arduino.cc/en/Main/ArduinoWiFiShield)

[Arduino BT](http://arduino.cc/en/Main/ArduinoBoardBT?from=Main.ArduinoBoardBluetooth)

Might [this article](http://plischka.at/Wi.232EUR-R.html) in german be of relevance? It seems to be used in model airplanes.

[Here](http://www.handysektor.de/geraete-technik/funktechnik.html) is an interesting speed comparison between different wireless protocols, which is also in german. The graph should be self-explaining.

[This wikipedia article](http://en.wikipedia.org/wiki/Short_Range_Devices) gives a nice overwiev over available frequency bands.

### Wired options

Instead of communicating with a wireless scheme, one could in principle also connect a sensor directly with a [single long wire](http://playground.arduino.cc/Learning/OneWire). This technolgy allows to connect up to 65536 sensors over a single usb dongle. The sensors are wired on a single line, the ground not being connected directly over the wire.

### Arduino power consumption links

[Run Arduino for years](http://www.openhomeautomation.net/arduino-battery/)

[Run Arduino for months](http://hwstartup.wordpress.com/2013/03/11/how-to-run-an-arduino-on-a-9v-battery-for-weeks-or-months/)

[Arduino with external power controler](http://alanbmitchell.wordpress.com/2011/10/02/operate-arduino-for-year-from-batteries/)

[Power saving techniques](http://www.gammon.com.au/forum/?id=11497)

[Arduino low power and RF transmitter with code](https://github.com/petervojtek/diy/wiki/Arduino-with-Very-Low-Power-Consumption)

[Solar module](http://www.voltaicsystems.com/solar-arduino-guide.shtml)

[Battery](http://cybergibbons.com/uncategorized/arduino-misconceptions-6-a-9v-battery-is-a-good-power-source/)

### Interesting Single Board Computers

The [Raspberry Pi Compute Module](http://www.raspberrypi.org/raspberry-pi-compute-module-new-product/) just contains the basic ingredients of the Raspberry Pi (the Broadcom CPU / GPU with 512MB of RAM) and 4GB of Flash Memory.

The [Cubieboard](http://cubieboard.org/) seems to have several advantages compared to the Raspberry Pi, most importantly a separate SATA port for efficiently accessing a local hard drive.

The [Parallella](http://www.parallella.org/) supercomputer claims to deliver 90GFlops of computing power, supposedly the most efficient supercomputer once it will be available for shipping again.
