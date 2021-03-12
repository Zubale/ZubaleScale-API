import serial
from serial.tools.list_ports import comports
import re

class scale:

    FINALCHAR = chr(3)
    REQUEST_WEIGHT = "W\r"
    REQUEST_STATUS = "S\r"

    def __init__(self, port="COM5", timeout=10):
        self.PORT = port
        self.TIMEOUT = timeout
        self.WTcom = serial.Serial(port=self.PORT, timeout=self.TIMEOUT)



    def getWeight(self):
        self.sendData(self.REQUEST_WEIGHT)
        fullInfo = self.getData()
        if "kg" in fullInfo:
            pattern = r'[-]?\d*[.]\d*'
            match = re.search(pattern, fullInfo)
            weight = float(match.group())
            if weight > 0:
                return weight
            else:
                raise FloatingPointError("Scale is not zeroed properly: remove all weight and press tare")
        else:
            raise TypeError("Scale is not set properly to kg: Press the unit key to change")


    def getData(self):
        data = self.WTcom.read_until(self.FINALCHAR.encode())
        print(data)
        return data.decode()

    def getStatus(self):
        self.sendData(self.REQUEST_STATUS)
        data = self.getData()
        print (data)
        #todo analyse data
        return data

    def isZeroed(self):
        pass

    @staticmethod
    def checkPorts():
        ports = comports()
        if len(ports) != 0:
            print(ports)
            print(ports[0].name)
            return comports()
        else:
            raise IOError("No ports found")

    def sendData(self, data):
        self.WTcom.write(data.encode())

    def setPort(self):
        #todo add port search and change
        pass

