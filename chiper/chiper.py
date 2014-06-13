# -*- coding: utf-8 -*-


class Component(object):

    def __init__(self, power_active, power_standby, price, size):
        """
        The basic class that all other component should extend
        """
        self.power_active = power_active # the power_active consumtion in mW
        self.power_standby = power_standby # the power_standby consumtion in mW 
        self.price = price # price in euros
        self.size = size # size in volume cm3


class Sensor(Component):

    def __init__(self, power_active, power_standby, price, size, max_rate, max_range, size_output):
        super(Sensor, self).__init__(power_active, power_standby, price, size)
        """
        A sensor has :
        """
        self.max_rate = max_rate # measurement max_rate per second
        self.measurement_time = 1/max_rate
        self.max_range = max_range # max_range in m
        self.size_output = size_output # size in Mb of the output of one measurment

    @classmethod
    def fromComponent(cls, c, max_rate, max_range, size_output):
        return cls(c.power_active, c.power_standby, c.price, c.size, max_rate, max_range, size_output)

    def getConsoHour(self, rate):
        """
        Given a measurement rate per hour, how much energy in mWs
        """
        return (rate * self.measurement_time * self.power_active) + (3600 - (rate * self.measurement_time)) * self.power_standby

class Communicator(Component):

    def __init__(self, power_active, power_standby, price, size, upload, download, max_range):
        super(Communicator, self).__init__(power_active, power_standby, price, size)
        """
        A communication chip has :
        """
        self.upload = upload # upload in Mb/s
        self.download = download # upload in Mb/s
        self.max_range = max_range # max_range in m

    @classmethod
    def fromComponent(cls, c, upload, download, max_range):
        return cls(c.power_active, c.power_standby, c.price, c.size, upload, download, max_range)

    def getConso(self, size_file):
        """
        get the energy needed to transfer a file of size_file
        """
        return (size_file / self.upload) * self.power_active

class Battery(Component):

    def __init__(self, power_active, power_standby, price, size, voltage, amperage, energy):
        super(Battery, self).__init__(power_active, power_standby, price, size)
        """
        A simple Battery
        """
        self.voltage = voltage # voltage in volts
        self.amperage = amperage # amperage in mA
        self.energy = energy # energy in mWh

    @classmethod
    def fromComponent(cls, c, voltage, amperage, energy):
        return cls(c.power_active, c.power_standby, c.price, c.size, voltage, amperage, energy)


# http://www.arducam.com/camera-modules/2mp-ov2640/
cameraOV2640 = Sensor.fromComponent(Component(125, 0.6, 7*0.75, 2*2*1), 15, 10, 0.13)

# http://www.adafruit.com/products/1137
ultrasoundLVEZ0 = Sensor.fromComponent(Component(17, 0.5, 85*0.75, 7*5*4.5), 10, 7, 1e-6)

# http://en.wikipedia.org/wiki/Bluetooth_low_energy
# http://www.makershed.com/BLE_Mini_Bluetooth_4_0_Interface_p/mkrbl2.htm
Bluetooth_low_energy = Communicator.fromComponent(Component(100,1e-3,70*0.75, 2*2*1), 1,1, 100)

# battery AA (two of them)
# http://en.wikipedia.org/wiki/AA_battery
batteryAA = Battery.fromComponent(Component(100,0,1, 5*2*1), 3, 50, 3.9e3)


# how long can a battery hold a camera that takes a photo each half-hour and trasmit it via BLE ?
nb_per_hour = 2
a = cameraOV2640.getConsoHour(nb_per_hour)
print a
b = nb_per_hour*Bluetooth_low_energy.getConso(cameraOV2640.size_output)
print b

print batteryAA.energy/(a+b)

# how long can a battery hold a ultrasound sensor that takes a measurment each half-hour and trasmit it via BLE ?
nb_per_hour = 2
a = ultrasoundLVEZ0.getConsoHour(nb_per_hour)
print a
b = nb_per_hour*Bluetooth_low_energy.getConso(ultrasoundLVEZ0.size_output)
print b

print batteryAA.energy/(a+b)
