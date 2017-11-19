import ssl
import socket
from lib.log import log


class xmpp_socket(object):

    def __init__(self, hostname, port, log):
        self.hostname = hostname
        self.port = port
        self.sock = socket.socket(socket.AF_INET)
        self.context = ssl.create_default_context()
        self.log = log
        self.connect()

    def connect(self):
        try:
            self.sock.connect((self.hostname, self.port))
        except OSError:
            self.log.printError("xmpp_socket couldn connect!")
            exit(-1)            

    def close(self):
        self.sock.close()

    def sendMessage(self, message):
        self.sock.send(message.encode())

    def recvMessage(self):
        temp = self.sock.recv(4096).decode()
        print(temp)
        return temp

    def upgradetoTLS(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.context.check_hostname = True
        self.context.load_verify_locations("/etc/pki/tls/certs/ca-bundle.crt")
        self.sock = self.context.wrap_socket(self.sock, server_hostname=self.hostname)
        return self.sock


if __name__ == '__main__':
    pass