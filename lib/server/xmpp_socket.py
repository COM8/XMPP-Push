import ssl
import socket


class xmpp_socket(object):

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.sock = socket(socket.AF_INET)
        self.context = ssl.create_default_context()

    @staticmethod
    def sendMessage(self, message):
        self.sock.send(message.encode())

    @staticmethod
    def recvMessage(self):
        temp = self.sock.recv(4096).decode()
        print(temp)
        return temp

    @staticmethod
    def upgradetoTLS(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.context.check_hostname = True
        self.context.load_verify_locations("/etc/pki/tls/certs/ca-bundle.crt")
        self.sock = self.context.wrap_socket(self.sock, self.hostname)
        return self.sock


if __name__ == '__main__':
    pass