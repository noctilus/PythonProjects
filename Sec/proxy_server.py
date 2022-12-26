"""Python Proxy Server."""

import select
import socket
import sys
import time

# Changing the buffer_size and delay, you can improve the speed and bandwidth.
# But when buffer get to high or delay go too down, you can broke things

BUFFER_SIZE = 4096
DELAY = 0.0001
forward_to = ('ncbi.nlm.nih.gov', 80)


class Forward:
    """Forward Class."""

    def __init__(self):
        """Forward class instance initialization."""
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        """Start function."""
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception as e:
            print(e)
            return False


class TheServer:
    """Server Class."""

    input_list = []
    channel = {}

    def __init__(self, host, port):
        """Server instance initialisation."""
        self.s = None
        print('TheServer, __init__')
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(200)

    def main_loop(self):
        """Server Class loop."""
        print('Server Starting')
        self.input_list.append(self.server)
        while 1:
            time.sleep(DELAY)
            sel_sel = select.select
            inputready, outputready, exceptready = sel_sel(
                self.input_list, [], [])
            for self.s in inputready:
                if self.s == self.server:
                    self.on_accept()
                    break

                self.data = self.s.recv(BUFFER_SIZE)
                if len(self.data) == 0:
                    self.on_close()
                    break
                else:
                    self.on_recv()

    def on_accept(self):
        """Server on_accept function."""
        forward = Forward().start(forward_to[0], forward_to[1])
        clientsock, clientaddr = self.server.accept()
        if forward:
            print(clientaddr, "has connected")
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print("Can't establish connection with remote server.", end=' ')
            print("Closing connection with client side", clientaddr)
            clientsock.close()

    def on_close(self):
        """Server on_close function."""
        print(self.s.getpeername(), "has disconnected")
        # remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]

    def on_recv(self):
        """
        Server on_receive function.
        We can modify data before sending further.
        """

        data = self.data
        # here we can parse and/or modify the data before send forward
        print(data)
        self.channel[self.s].send(data)


if __name__ == '__main__':
    server = TheServer('localhost', 33333)
    try:
        server.main_loop()
    except KeyboardInterrupt:
        print("Ctrl C - Stopping server")
        sys.exit(1)
