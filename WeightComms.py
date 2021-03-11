import serial
import re

class scale:

    FINALCHAR = chr(3)
    REQUEST_WEIGHT = "W\r"
    REQUEST_STATUS = "S\r"

    def __init__(self, port="COM5", timeout=10):
        self.PORT = port
        self.TIMEOUT = timeout
        self.com = serial.Serial(port=self.PORT, timeout=self.TIMEOUT)



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
                raise Exception("Scale is not zeroed properly: remove all weight and press tare")
        else:
            raise Exception("Scale is not set properly to kg: Press the unit key to change")


    def getData(self):
        data = self.com.read_until(self.FINALCHAR.encode())
        print(data)
        return data.decode()

    def getStatus(self):
        self.sendData(self.REQUEST_STATUS)
        data = self.getData()
        print (data)
        return data

    def isZeroed(self):
        pass

    def setPort(self, port):
        #todo scan for correct port
        self.PORT = port

    def sendData(self, data):
        self.com.write(data.encode())