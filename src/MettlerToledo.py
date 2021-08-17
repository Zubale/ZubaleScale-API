import serial
from serial.tools.list_ports import comports
import re

class scale:

    FINALCHAR = chr(13)
    REQUEST_WEIGHT = "W"
    REQUEST_STATUS = "S\r"
    ECHOTEST = "E"
    RANDOMCHAR = "J"
    ECHOOFF = "F"

    def __init__(self, port="COM5", timeout=10):
        self.PORT = port
        self.TIMEOUT = timeout
        self.MettlerToledo = serial.Serial(port=self.PORT, timeout=self.TIMEOUT)



    def getWeight(self):
        self.sendData(self.REQUEST_WEIGHT)
        fullInfo = self.getData()
        '''if "kg" in fullInfo:
            pattern = r'[-]?\d*[.]\d*'
            match = re.search(pattern, fullInfo)
            weight = float(match.group())
            if weight > 0:
                return weight
            else:
                raise FloatingPointError("Scale is not zeroed properly: remove all weight and press tare")
        else:
            raise TypeError("Scale is not set properly to kg: Press the unit key to change")
        '''
        print(fullInfo)

    def echoTest(self):
        self.sendData(self.ECHOTEST)
        print(self.getData())
        self.sendData(self.RANDOMCHAR)
        print(self.getData())
        self.sendData(self.ECHOOFF)
        print(self.getData())


    def getData(self):
        data = self.MettlerToledo.read_until(self.FINALCHAR.encode())
        print(data)
        print("return")
        return data.decode()

    def getStatus(self):
        self.sendData(self.REQUEST_STATUS)
        data = self.getData()
        print (data)
        return data

    def isZeroed(self):
        pass

    @staticmethod
    def checkPorts():
        ports = comports()
        if len(ports) != 0:

            print(ports[0].name)
            return comports()
        else:
            raise IOError("No ports found")

    def sendData(self, data):
        print('data')
        print(data.encode())
        self.MettlerToledo.write(data.encode())

    def setPort(self, port):
        try:
            self.closePort()
        except Exception as e:
            print(e)
        finally:
            self.PORT = port
            self.MettlerToledo = serial.Serial(port=self.PORT, timeout=self.TIMEOUT)
            return self.getStatus()

    def closePort(self):
        self.MettlerToledo.close()


print(scale.FINALCHAR)
port = scale.checkPorts()[0]
scaley = scale(port=port.name)
#scaley.echoTest()
scaley.sendData("2666666")
scaley.getData()
scaley.closePort()