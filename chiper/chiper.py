# -*- coding: utf-8 -*-


class Component(object):

    def __init__(self, name, current_active, current_standby, price, size):
        """
        The basic class that all other components should extend
        """
        self.name = name # give a literal name
        self.current_active = current_active # the current in mA drawn in active mode
        self.current_standby = current_standby # the current in mA drawn in standby or power down mode 
        self.price = price # price in euros
        self.size = size # size in volume cm3


class Board(Component):

    def __init__(self, component, memory):
        super(Board, self).__init__(component.name, component.current_active, component.current_standby, component.price, component.size)
        """
        A board is an object with basically some system memory for programm code and some data
        """
        self.memory = memory # system memory in MB


class Sensor(Component):

    def __init__(self, component, max_rate, max_range, size_output):
        super(Sensor, self).__init__(component.name + ' (' + str(max_range) + 'm)', component.current_active, component.current_standby, component.price, component.size)
        """
        A sensor has :
        """
        self.max_rate = max_rate # measurement max_rate per second
        self.measurement_time = 1/max_rate
        self.max_range = max_range # max_range in m
        self.size_output = size_output # size in MB of the output of one measurment

    def getConsumptionPerHour(self, measuresPerHour, driver_current_active, driver_current_standby):
        """
        Given a measurement rate per hour, how much charge in mAs is consumed in one hour
        """
        measure_time = measuresPerHour * self.measurement_time
        idle_time = 3600 - measure_time
        current_active = self.current_active + driver_current_active - driver_current_standby
        current_standby = self.current_standby 
        return measure_time * current_active + idle_time * current_standby


class Communicator(Component):

    def __init__(self, component, upload, download, max_range):
        super(Communicator, self).__init__(component.name + ' (' + str(max_range) + 'm)', component.current_active, component.current_standby, component.price, component.size)
        """
        A communication chip has :
        """
        self.upload = upload # upload in MB/s
        self.download = download # upload in MB/s
        self.max_range = max_range # max_range in m

    def getConsumptionPerHour(self, measuresPerHour, driver_current_active, driver_current_standby, size_file):
        """
        Given a measurement rate per hour and a transfer file size, how much charge in mAs is consumed in one hour
        """
        transfer_time = measuresPerHour * size_file / self.upload
        idle_time = 3600 - transfer_time
        current_active = self.current_active + driver_current_active - driver_current_standby
        current_standby = self.current_standby
        return transfer_time * current_active + idle_time * current_standby


class Battery(Component):

    def __init__(self, component, voltage, amperage, charge):
        super(Battery, self).__init__(component.name + ' (' + str(voltage) + 'V, ' + str(charge) + 'mAh)', 0, 0, component.price, component.size)
        """
        A simple Battery
        """
        self.voltage = voltage # voltage in volts
        self.amperage = amperage # amperage in mA
        self.charge = charge # charge in mAh


class SeriesBatteries(Battery):

    def __init__(self, battery, number):
        super(SeriesBatteries, self).__init__(Component(str(number) + 'x [ ' + battery.name + ' ]', 0, 0, number * battery.price, number * battery.size),
                                              number * battery.voltage, battery.amperage, battery.charge)
        """
        Put several batteries in series, all quantities are extensive, except the current and the charge
        """


class ParallelBatteries(Battery):

    def __init__(self, battery, number):
        super(ParallelBatteries, self).__init__(Component(str(number) + 'x [ ' + battery.name + ' ]', 0, 0, number * battery.price, number * battery.size),
                                                battery.voltage, number * battery.amperage, number * battery.charge)
        """
        Put several batteries in parallel, all quantities are extensive, except the voltage
        """


class Solution(object):

    def __init__(self, board, sensor, communicator, battery):
        """
        A complete solution consists of a baord, driving the sensor and the communicator and being powered by a set of batteries
        """
        self.board = board
        self.sensor = sensor
        self.communicator = communicator
        self.powersupply = battery

    def getLifetime(self, measuresPerHour):
        """
        Get lifetime of complete solution in hours
        The driving board will be active while mesuring and transfering the data, but in standby when neither of those actions is done
        """
        sensor_consumption = self.sensor.getConsumptionPerHour(measuresPerHour, self.board.current_active, self.board.current_standby)
        communicator_consumption = self.communicator.getConsumptionPerHour(measuresPerHour, self.board.current_active, self.board.current_standby, self.sensor.size_output)
        return 3600 * self.powersupply.charge / (sensor_consumption + communicator_consumption + 3600*self.board.current_standby)

    def getPrice(self):
        return self.board.price + self.sensor.price + self.communicator.price + self.powersupply.price

    def getSize(self):
        return self.board.size + self.sensor.size + self.communicator.size + self.powersupply.size

    def getMemoryFilltime(self, measuresPerHour):
        """
        Experimental function which calculates the time to fill the memory, provided the available memory was only used to store data
        => this is the latest possible moment of a data transfer before no space in memory is left anymore
        """
        return self.board.memory / (measuresPerHour * self.sensor.size_output)

    def print_summary(self, measuresPerHour):
        """
        This functions prints all above information 
        """
        print self.board.name + ', ' + self.sensor.name + ', ' + self.communicator.name + ', ' + self.powersupply.name
        print 'Life time in hours        : ' + str(int(round(self.getLifetime(measuresPerHour),0))) + '  [ ' + str(round(self.getLifetime(measuresPerHour)/24,1)) + ' days ]'
        print 'Price in euros            : ' + str(round(self.getPrice(),2))
        print 'Volume in ccm             : ' + str(int(round(self.getSize(),0)))
        #print 'Memory fill time in hours : ' + str(int(round(self.getMemoryFilltime(measuresPerHour),0)))
        print ''
        print ''
  

### Sensors

# http://www.arducam.com/camera-modules/2mp-ov2640/
cameraOV2640 = Sensor(Component('Camera OV2640', 125, 0.6, 7*0.75, 2*2*1), 15, 10, 0.13)

# http://www.adafruit.com/products/1137
ultrasoundLVEZ0 = Sensor(Component('Ultrasound LVEZ0', 17, 0.5, 85*0.75, 7*5*4.5), 10, 7, 1e-6)

# found on www.fasttech.com
ultrasonic_HC_SR04 = Sensor(Component('Ultrasonic HC SR04', 15, 2, 1.96 * 0.75, 1.6*5*1.4), (60e-3)**(-1), 4.5, 1e-5)
ultrasonic_HY_SRF05 = Sensor(Component('Ultrasonic HY SRF05', 15, 2, 2.28 * 0.75, 1.9*4.5*2.1), (60e-3)**(-1), 4.5, 1e-5)



### Communicators

# http://en.wikipedia.org/wiki/Bluetooth_low_energy
# http://www.makershed.com/BLE_Mini_Bluetooth_4_0_Interface_p/mkrbl2.htm
#Bluetooth_low_energy = Communicator(Component(100,1e-3,70*0.75, 2*2*1), 1,1, 100)
#Bluetooth_low_energy = Communicator(Component(100,0,70*0.75, 2*2*1), 1,1, 100)
# http://www.adafruit.com/products/1697
# the consumption data is not quite clear yet, let's assume the following values
Bluefruit_LE = Communicator(Component('Bluefruit Low Energy', 100, 0, 19.95 * 0.75, 2.9*2.8*0.1), 1, 1, 100)


# http://jeromeabel.net/files/ressources/xbee-arduino/xbee-arduino.pdf
xBee_series2 = Communicator(Component('xBee series 2', 40, 0.01, 23 * 0.75, 2.5*2.8*0.3), 0.25, 0.25, 100)


# https://www.sparkfun.com/products/10534
# http://www.robotshop.com/en/seeedstudio-433mhz-low-cost-transmitter-receiver-pair.html
# RF 433MHz Transmitter
# the comsumption in idle mode is speculation
RF433 = Communicator(Component('RF 433 transmitter', 8, 8, 3.95 * 0.75, 1*2.5*0.2), 8e-3, 0, 150)



### Arduinos

# found on www.fasttech.com
arduino_uno_rev3 = Board(Component('Arduino Uno', 50, 35, 11.62 * 0.75, 7.5*5.3*1.5), 0.032)

arduino_nano_V3_0 = Board(Component('Arduino Nano', 25 , 19, 8.07 * 0.75, 4.4*1.9*2), 0.032)

# https://www.sparkfun.com/products/11113
# two models are available, one with 3.3V and one with 5V voltage regulator, both powered by Atmega328 microprocessor
# http://s6z.de/cms/index.php/arduino/nuetzliches/9-winterschlaf-fuer-arduino
arduino_pro_mini_328 = Board(Component('Arduino Pro Mini 328', 19, 3.3, 9.95 * 0.75, 1.8*3.3*0.5), 0.032)


# Bare ATmega328, the price will not be correct, as we will need several extra equipment
bare_328 = Board(Component(' Bare ATmega328 (additional components needed)', 15.15, 0.36, 10, 3*1*1), 0.032)



### Batteries

# solar panel
solar_panel_battery = Battery(Component('Solar panel with battery', 0, 0, 9.38, 4*10*1), 5.5, 1000, 1350)


# battery AA (two of them)
# http://en.wikipedia.org/wiki/AA_battery
#batteryAA = Battery(Component(100,0,1, 5*2*1), 3, 50, 3.9e3)
# http://www.amazon.fr/Duracell-Pile-Rechargeable-Duralock-Charged/dp/B00E5YSXPQ/ref=pd_rhf_dp_p_img_7
batteryAA = Battery(Component('Rechargeable AA battery', 0, 0, 8.69/4, 5*1*1), 1.2, 0, 2400)







### assemble different solutions

cameraOV2640_BLE = Solution(arduino_uno_rev3, cameraOV2640, Bluefruit_LE, SeriesBatteries(batteryAA,4))

ultrasoundLVEZ0_BLE = Solution(arduino_uno_rev3, ultrasoundLVEZ0, Bluefruit_LE, SeriesBatteries(batteryAA,4))

pro328_srf05_RF433 = Solution(arduino_pro_mini_328, ultrasonic_HY_SRF05, RF433, SeriesBatteries(batteryAA,4))

pro328_srf05_RF433_solar = Solution(arduino_pro_mini_328, ultrasonic_HY_SRF05, RF433, solar_panel_battery)

pro328_srf05_xbee_solar = Solution(arduino_pro_mini_328, ultrasonic_HY_SRF05, xBee_series2, solar_panel_battery)

bare_srf05_xbee_battery = Solution(bare_328, ultrasonic_HY_SRF05, xBee_series2, SeriesBatteries(batteryAA,4))






### output lifetimes and prices
# notice, that the energy consumption is in principle dictated by the idle period, as the arduinos essentially have nothing to do



<<<<<<< HEAD
print "how long can a battery hold a camera that takes a photo each half-hour and transmit it via BLE ?"
cameraOV2640_BLE = Solution(arduino_uno, cameraOV2640, Bluetooth_low_energy, PowerSupply(batteryAA,2))
print "%s hours" % cameraOV2640_BLE.getLifetime(nb_per_hour)


print "how long can a battery hold a ultrasound sensor that takes a measurment each half-hour and transmit it via BLE ?"
ultrasoundLVEZ0_BLE = Solution(arduino_uno, ultrasoundLVEZ0, Bluetooth_low_energy, PowerSupply(batteryAA,2))
print "%s hours" %  ultrasoundLVEZ0_BLE.getLifetime(nb_per_hour)
=======
print '  measure every 30 minutes '
print '============================'
print ''
measurements_per_hour = 2

cameraOV2640_BLE.print_summary(measurements_per_hour)
ultrasoundLVEZ0_BLE.print_summary(measurements_per_hour)
pro328_srf05_RF433.print_summary(measurements_per_hour)
pro328_srf05_RF433_solar.print_summary(measurements_per_hour)
pro328_srf05_xbee_solar.print_summary(measurements_per_hour)
bare_srf05_xbee_battery.print_summary(measurements_per_hour)
>>>>>>> 746c7179f6044be6b4bd9c5c762d1089ebe484b6
