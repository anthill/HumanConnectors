# -*- coding: utf-8 -*-


class Component(object):

    def __init__(self, power_active, power_standby, price, size):
        """
        The basic class that all other components should extend
        """
        self.power_active = power_active # the power_active consumption in mW
        self.power_standby = power_standby # the power_standby consumption in mW 
        self.price = price # price in euros
        self.size = size # size in volume cm3


class Board(Component):

    def __init__(self, component, memory):
        super(Board, self).__init__(component.power_active, component.power_standby, component.price, component.size)
        """
        A board is an object with basically some system memory for programm code and some data
        """
        self.memory = memory # system memory in MB


class Sensor(Component):

    def __init__(self, component, max_rate, max_range, size_output):
        super(Sensor, self).__init__(component.power_active, component.power_standby, component.price, component.size)
        """
        A sensor has :
        """
        self.max_rate = max_rate # measurement max_rate per second
        self.measurement_time = 1/max_rate
        self.max_range = max_range # max_range in m
        self.size_output = size_output # size in Mb of the output of one measurment

    def getConsumptionPerHour(self, measuresPerHour, driver_power_active, driver_power_standby):
        """
        Given a measurement rate per hour, how much energy in mWs
        """
        measure_time = measuresPerHour * self.measurement_time
        idle_time = 3600 - measure_time
        power_active = self.power_active + driver_power_active
        power_standby = self.power_standby + driver_power_standby
        return measure_time * power_active + idle_time * power_standby


class Communicator(Component):

    def __init__(self, component, upload, download, max_range):
        super(Communicator, self).__init__(component.power_active, component.power_standby, component.price, component.size)
        """
        A communication chip has :
        """
        self.upload = upload # upload in Mb/s
        self.download = download # upload in Mb/s
        self.max_range = max_range # max_range in m

    def getConsumptionPerHour(self, measuresPerHour, driver_power_active, driver_power_standby, size_file):
        """
        get the energy needed to transfer a file of size_file
        """
        transfer_time = measuresPerHour * size_file / self.upload
        idle_time = 3600 - transfer_time
        power_active = self.power_active + driver_power_active
        power_standby = self.power_standby + driver_power_standby
        return transfer_time * power_active + idle_time * power_standby


class Battery(Component):

    def __init__(self, component, voltage, amperage, energy):
        super(Battery, self).__init__(component.power_active, component.power_standby, component.price, component.size)
        """
        A simple Battery
        """
        self.voltage = voltage # voltage in volts
        self.amperage = amperage # amperage in mA
        self.energy = energy # energy in mWh


class PowerSupply(Battery):

    def __init__(self, battery, number):
        super(PowerSupply, self).__init__(Component(number * battery.power_active, number * battery.power_standby, number * battery.price,
                                                    number * battery.size), number * battery.voltage, battery.amperage, number * battery.energy)
        """
        A power supply consists of several batteries
        """


class Solution(object):

    def __init__(self, board, sensor, communicator, powersupply):
        """
        A complete solution consists of a baord, driving the sensor and the communicator and being powered by a set of batteries
        """
        self.board = board
        self.sensor = sensor
        self.communicator = communicator
        self.powersupply = powersupply

    def getLifetime(self, measuresPerHour):
        """
        Get lifetime of complete solution in hours
        The driving board will be active while mesuring and transfering the data, but in standby when neither of those actions is done
        """
        sensor_consumption = self.sensor.getConsumptionPerHour(measuresPerHour, self.board.power_active, self.board.power_standby)
        communicator_consumption = self.communicator.getConsumptionPerHour(measuresPerHour, self.board.power_active, self.board.power_standby, self.sensor.size_output)
        return 3600 * self.powersupply.energy / (sensor_consumption + communicator_consumption)

    def getPrize(self):
        return self.board.price + self.sensor.price + self.communicator.price + self.powersupply.price

    def getSize(self):
        return self.board.size + self.sensor.size + self.communicator.size + self.powersupply.size

    def getMemoryFilltime(self, measuresPerHour):
        """
        Experimental function which calculates the time to fill the memory, provided the available memory was only used to store data
        => this is the latest possible moment of a data transfer before no space in memory is left anymore
        """
        return self.board.memory / (measuresPerHour * self.sensor.size_output)
  


# http://www.arducam.com/camera-modules/2mp-ov2640/
cameraOV2640 = Sensor(Component(125, 0.6, 7*0.75, 2*2*1), 15, 10, 0.13)

# http://www.adafruit.com/products/1137
ultrasoundLVEZ0 = Sensor(Component(17, 0.5, 85*0.75, 7*5*4.5), 10, 7, 1e-6)

# http://en.wikipedia.org/wiki/Bluetooth_low_energy
# http://www.makershed.com/BLE_Mini_Bluetooth_4_0_Interface_p/mkrbl2.htm
#Bluetooth_low_energy = Communicator(Component(100,1e-3,70*0.75, 2*2*1), 1,1, 100)
Bluetooth_low_energy = Communicator(Component(100,0,70*0.75, 2*2*1), 1,1, 100)

# battery AA (two of them)
# http://en.wikipedia.org/wiki/AA_battery
#batteryAA = Battery(Component(100,0,1, 5*2*1), 3, 50, 3.9e3)
batteryAA = Battery(Component(50,0,1, 5*1*1), 3, 50, 1.9e3)


arduino_uno = Board(Component(0,0,0,0),0)


nb_per_hour = 2

print "how long can a battery hold a camera that takes a photo each half-hour and transmit it via BLE ?"
cameraOV2640_BLE = Solution(arduino_uno, cameraOV2640, Bluetooth_low_energy, PowerSupply(batteryAA,2))
print "%s hours" % cameraOV2640_BLE.getLifetime(nb_per_hour)


print "how long can a battery hold a ultrasound sensor that takes a measurment each half-hour and transmit it via BLE ?"
ultrasoundLVEZ0_BLE = Solution(arduino_uno, ultrasoundLVEZ0, Bluetooth_low_energy, PowerSupply(batteryAA,2))
print "%s hours" %  ultrasoundLVEZ0_BLE.getLifetime(nb_per_hour)
