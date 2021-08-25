import socket
from socketserver import BaseRequestHandler, UDPServer
import xml.dom.minidom
import re

class Scale:

    FILES_DIR = "src/files/"
    RESPONSE_PATH = FILES_DIR + "receive_ticket.xml"
    PLU_PATH = FILES_DIR + "create_plu.xml"
    REMOVE_PLU_PATH = FILES_DIR + "remove_plu.xml"
    NET_EXPLORE_PATH = FILES_DIR + "net_explore.xml"
    CURRENT_WEIGHT_DIR = FILES_DIR + "current_weight.txt"

    BUFFER_SIZE = 1024
    TCP_PORT = 3001
    SERVER_IP_AD = "192.168.0.110"
    CLIENT_IP_AD = "192.168.0.155"
    BROADCAST_IP = "255.255.255.255"

    def __init__(self):
        self.reset()


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

    def getAttribute(self, tag, attribute, collection):
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

    def pingScale(self):
        self.sendMessage(self.NET_EXPLORE_PATH)
        #todo return data

    def exploreForScale(self):
        #recieve ip from udp broadcast
        print('waiting for message')
        syslog = UDPServer((self.SERVER_IP_AD, 2305), BaseRequestHandler)
        syslog.handle_request()
        request = syslog.get_request()
        print(request[1][0])
        self.CLIENT_IP_AD = request[1][0]
        syslog.server_close()

    def reset(self):
        self.exploreForScale()
        self.removePlu()
        self.addPlu()

    @property
    def getWeight(self):
        return  float(self.openFile(self.CURRENT_WEIGHT_DIR))

if __name__ == '__main__':
    scale = Scale()


