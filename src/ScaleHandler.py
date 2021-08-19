from socketserver import BaseRequestHandler, TCPServer
import datetime, socket

BUFFER_SIZE = 1024
TCP_PORT = 3001
BUFFER_SIZE = 1024
IP_AD = "192.168.0.110"
XML_DIR = "src/xml/"
RESPONSE_DIR = XML_DIR + "receive_ticket.xml"
PLU_DIR = XML_DIR + "create_plu.xml"



class ScaleHandler(BaseRequestHandler):
    """
    Server handler is required to handle tcp request.
    See examples: https://www.programcreek.com/python/example/73643/SocketServer.BaseRequestHandler
    """

    LAST_WIEGHT = 0.0
    LAST_TIME = datetime.MINYEAR


    def handle(self):
        data = self.request.recv(BUFFER_SIZE)
        print(f"{self.client_address[0]}: {str(data)}")
        response = self.openFile(RESPONSE_DIR).encode()
        self.request.sendall(response)
        #TODO add compare values
        #TODO save last value


    def openFile(self, file_dir):
        file = open(file_dir, "r")
        legend = file.read()
        file.close()

        return legend


if __name__ == "__main__":
    try:
        syslog = TCPServer((IP_AD, TCP_PORT), ScaleHandler)
        print("EZ syslog starts, CTRL-C to stop...")
        syslog.serve_forever(poll_interval=1)


    except KeyboardInterrupt:
        print("Ctrl-C detected, exit.")