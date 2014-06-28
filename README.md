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

[Camera](http://www.arducam.com/arducam-bluetooth-module-wireless-image-system/)

[Ultrasounds](http://www.adafruit.com/products/1137)

This [ultrasound](http://www.fasttech.com/products/0/10000007/1012007-arduino-compatible-hc-sr04-ultrasonic-sonar) sensor is extremely cheap and works together with arduino.

A specific [implementation](http://www.instructables.com/id/Arduino-dual-ultrasonic-liquid-level-meter-with-in/) is using an ultrasonic sensor together with an arduino and Xbee in order to measure the liquid level in containers.

### Measuring with ultrasonic sensors

Here is a list of links where people have realized a system to measure the water level in bins.

[Arduino Uno + URM37 + Xbee](http://www.instructables.com/id/Arduino-dual-ultrasonic-liquid-level-meter-with-in/)

[Arduino + SRF05](http://www.makechronicles.com/2012/03/13/arduino-project-6-measuring-a-water-tank-level-srf05-ultrasonic-rangefinderarduino-mega-2560arduino-uno1-0/)

[Arduino Uno + Ethernet + URM37](http://www.jo3ri.be/arduino/projects/tank-level-measuring-basic)

[This example uses a display and also contains some code](http://www.open-electronics.org/water-tank-level-display-with-arduino/)

### Wireless options

In the following there is a loose list of links about wireless transmission methods (RF, IR, Bluetooth, Wifi, ...) to be examined more closely. Most of the devices seem to work well on Arduino, but what about Raspberry Pi? Some of the shields are to be connected to a full Arduino, some wireless adapters might just work with the core microcontroller. It should also be mentioned, that in the case of Bluetooth, the [Bluetooth Low Energy](http://en.wikipedia.org/wiki/Bluetooth_low_energy) standard is particulary interesting.

[RF transmitter](http://ninjablocks.com/blogs/how-to/7501042-adding-rf-433mhz-to-your-arduino) and [this](http://conoroneill.net/arduino-and-raspberry-pi-communicating-over-2-4ghz-with-cheap-nrf24l01-modules/)

The Zigbee protokoll seems to be very interesting, as, citing from the [wikipedia article](http://en.wikipedia.org/wiki/ZigBee), it is specifically designed to be much simpler and less expensive than for example Wifi and Bluetooth. It aims especially at scenarios where battery life time is an issue. Xbee Series 2 seems to implement the Zigbee standard, as [this article](http://tutorial.cytron.com.my/2011/03/06/is-xbee-zigbee/) explains.

[Xbee](http://www.digi.com/fr/products/wireless/point-multipoint/xbee-series1-module) and [this](http://forum.arduino.cc/index.php?topic=59082.0;wap2), an example of which can be found [here](http://jeromeabel.net/fr/ressources/xbee-arduino). This sensor fits perfectly on the arduino nano.

[IR LED](http://www.adafruit.com/products/387) + [IR Sensor](http://www.adafruit.com/products/157)

[Bluetooth transceiver](http://www.instructables.com/id/Cheap-2-Way-Bluetooth-Connection-Between-Arduino-a/step3/Wiring-the-Arduino-Bluetooth-transceiver/)

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

The following [solar module](http://www.amazon.fr/Chargeur-Portable-téléphone-appareil-numérique/dp/B00378SRDY/ref=sr_1_19?ie=UTF8&qid=1403195735&sr=8-19&keywords=chargeur+solaire) also contains a battery which delivers 5.5V and contains 1350mAh. This should be enough to power an arduino with some sensors and communication dongles.

[Battery](http://cybergibbons.com/uncategorized/arduino-misconceptions-6-a-9v-battery-is-a-good-power-source/)

In order to render the whole waterproof, some specific [power gel](http://electricalproducts.cellpack.com/fileadmin/user_upload/bbcgroup.biz/news/eproducts/Drucksachen/Drucksachen_en/powergel_flyer_uk.pdf) may be of use. This gel does not conduct electricity, but seems to conduct heat.

### Different Arduino models

The [Arduino Uno](http://arduino.cc/en/Main/arduinoBoardUno) is certainly one of the most accessable models for beginners. This board provides 14 digital pins that operate at 5V each. It also provides a 3V3 power supply for connectors such as xbee and other add-on boards that operate at lower voltages. On the other side, the onboard voltage regulators draw [10mA of quiescent current](http://playground.arduino.cc/Learning/ArduinoSleepCode) even while in sleeping mode. This will dry a usual battery in 1-2 weeks, just for feeding the voltage regulator. This will only make sense if we use solar panels to recharge the batteries.

The [Arduino Nano](http://arduino.cc/en/Main/arduinoBoardNano) uses the same microcontroller as the Arduino Uno, and therefore has in principle the same functionalities. The main difference is the much smaller size and the lacking DC power jack. The onboard voltage regulator seems to draw slightly less current.

The [Arduino Fio](http://arduino.cc/en/Main/ArduinoBoardFio) contains a socket for directly connecting an xbee series 1 module, for communication and even for programming the Arduino wirelessly. It also contains a charging circuit for Lithuim Polymer batteries and a corresponding connector. However, this board operates at 3V3, requiring additional elements in order to connect 5V sensors. This board is produced and distributed by [sparkfun](https://www.sparkfun.com/).

Sparkfun also produces the [Arduino Pro Mini](http://arduino.cc/en/Main/ArduinoBoardProMini) in two different versions, one at 3V3, the other at 5V. Both boards are particularly small and seem to use a more efficient voltage regulator. Notice, that these boards are reduced to the strict minimum and lack a USB connection, which is particularly interesting for energy efficiency in the production period. However, for programming the Arduino Pro Mini a suitable [breakout board](https://www.sparkfun.com/products/9716) is required, depending on the underlying voltage. Also notice, that the microcontroller of the Arduino Pro Mini is the ATMega168. There is also the [Arduino Pro Mini 328](https://www.sparkfun.com/products/11113), which exists in a 3V3 and a 5V variant and which uses the ATMega328, the same microcontroller as the Arduino Uno.



### Interesting Single Board Computers

The [Raspberry Pi Compute Module](http://www.raspberrypi.org/raspberry-pi-compute-module-new-product/) just contains the basic ingredients of the Raspberry Pi (the Broadcom CPU / GPU with 512MB of RAM) and 4GB of Flash Memory.

The [Cubieboard](http://cubieboard.org/) seems to have several advantages compared to the Raspberry Pi, most importantly a separate SATA port for efficiently accessing a local hard drive.

The [Parallella](http://www.parallella.org/) supercomputer claims to deliver 90GFlops of computing power, supposedly the most efficient supercomputer once it will be available for shipping again.
