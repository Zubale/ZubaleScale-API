from socketserver import BaseRequestHandler, TCPServer
import xml.dom.minidom as xml





class ScaleHandler(BaseRequestHandler):
    """
    Server handler is required to handle tcp request.
    See examples: https://www.programcreek.com/python/example/73643/SocketServer.BaseRequestHandler
    """
    XML_TAG = "Weight"

    BUFFER_SIZE = 1024
    TCP_PORT = 3001
    IP_AD = "192.168.0.110"
    FILES_DIR = "files/"
    RESPONSE_DIR = FILES_DIR + "receive_ticket.xml"
    CURRENT_WEIGHT_DIR = FILES_DIR + "current_weight.txt"

    def handle(self):
        #get data and send generic response
        print("Receiving data")
        data = self.request.recv(self.BUFFER_SIZE)
        print(f"{self.client_address[0]}: {data.decode()}")
        response = self.openFile(self.RESPONSE_DIR).encode()
        self.request.sendall(response)

        #save data to file
        print("Saving data")
        weight  = self.getWeight(data.decode())
        self.writeFile(self.CURRENT_WEIGHT_DIR,weight)




    def openFile(self, file_dir):
        file = open(file_dir, "r")
        legend = file.read()
        file.close()
        return legend

    def writeFile(self, file_dir, message):
        f = open(file_dir, "w")
        f.write(message)
        f.close()

    def getWeight(self, raw_xml):
        domtree = xml.parseString(raw_xml).documentElement
        node = domtree.getElementsByTagName(XML_TAG)[0]
        elem = node.childNodes[0]
        return elem.nodeValue


if __name__ == "__main__":
    try:
        syslog = TCPServer((IP_AD, TCP_PORT), ScaleHandler)
        print("EZ syslog starts, CTRL-C to stop...")
        syslog.serve_forever(poll_interval=1)


    except KeyboardInterrupt:
        print("Ctrl-C detected, exit.")