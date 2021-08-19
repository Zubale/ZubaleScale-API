import socket
import xml.dom.minidom
import re

class Scale:

    XML_PATH = "src/xml/"
    RESPONSE_PATH = XML_PATH + "receive_ticket.xml"
    PLU_PATH = XML_PATH + "create_plu.xml"
    REMOVE_PLU_PATH = XML_PATH + "remove_plu.xml"
    NET_EXPLORE_PATH = XML_PATH + "net_explore.xml"

    BUFFER_SIZE = 1024
    TCP_PORT = 3001
    SERVER_IP_AD = "192.168.0.110"
    CLIENT_IP_AD = "192.168.0.155"
    BROADCAST_IP = "255.255.255.250"

    def __init__(self, port="COM5", timeout=10):
        self.PORT = port
        self.TIMEOUT = timeout

    def sendMessage(self, file_path, client_ip=CLIENT_IP_AD):
        print('message en route')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.SERVER_IP_AD, 0))
        s.connect((client_ip, self.TCP_PORT))

        MESSAGE = self.openFile(file_path)
        s.send(MESSAGE.encode())
        data = s.recv(self.BUFFER_SIZE)
        s.close()
        return data

    def openXml(self, xmlPathName):
        DOMTree = xml.dom.minidom.parse(xmlPathName)
        collection = DOMTree.documentElement
        return collection

    def getAttribute(tag, attribute, collection):
        elementTag = collection.getElementsByTagName(tag)[-1]
        if (elementTag.hasAttribute(attribute)):
            return float(elementTag.getAttribute(attribute))

    def openFile(self, file_path):
        file = open(file_path, "r")
        legend = file.read()
        file.close()
        return legend

    def addPlu(self):
        self.sendMessage(self.PLU_PATH)

    def removePlu(self):
        self.sendMessage(self.REMOVE_PLU_PATH)

    def exploreForScale(self):
        scale = self.sendMessage(self.NET_EXPLORE_PATH, self.BROADCAST_IP)
        print(scale)
        #TODO fix errors for broadcast

if __name__ == '__main__':
    scale = Scale()
    scale.exploreForScale()


