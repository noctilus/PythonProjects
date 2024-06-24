import socket
import threading
from abc import ABC, abstractmethod
from sys import platform

import paramiko


class ServerBase(ABC):
    """
    Let's create the __init__() function and initialize some properties for later use:

    """

    def __init__(self):

        # _is_running 	a multithreaded event, which is basically a thread-safe boolean
        self._is_running = threading.Event()

        # _socket 	this socket will be used to listen to incoming connections
        self._socket = None

        # client_shell 	this will contain the shell for the connected client.
        # We don't yet initialize it, since we need to get the stdin
        # and stdout objects after the connection is made.
        self.client_shell = None

        # _listen_thread 	this will contain the thread that will listen
        # for incoming connections and data.
        self._listen_thread = None

    def start(self, address="127.0.0.1", port=22, timeout=1):
        """
        Next we create the start() and stop() functions. These are relatively simple,
        but here's a quick explanation of both. start() will create the socket and
        setup the socket options. It's important to note that the socket option SO_REUSEPORT
        is not available on Windows platforms, so we wrap it with a platform check. start()
        also creates the listen thread and starts it, which will run the listen() function
        that we will tackle next. stop() is even easier,
        as it simply joins the listen thread and closes the socket.
        """

        # If I'm not running:
        if not self._is_running.is_set():

            self._is_running.set()

            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)

            self._socket.settimeout(timeout)

            self._socket.bind((address, port))

            self._listen_thread = threading.Thread(target=self._listen)

            self._listen_thread.start()

    def stop(self):

        if self._is_running.is_set():
            self._is_running.clear()
            self._listen_thread.join()
            self._socket.close()

    def _listen(self):
        """
        The listen() function will constantly run if the server is running.
        We wait for a connection, if a connection is made, we will call our
        abstract connection_function() function, which will be implemented inside of
        our specific server class, described later on. Note that we wrap the code in
        this function in a try, except statement. This is because
        we expect self._socket.accept() to break if the server is stopped.
        """

        while self._is_running.is_set():
            try:
                self._socket.listen()
                client, addr = self._socket.accept()
                self.connection_function(client)
            except socket.timeout:
                pass

    @abstractmethod
    def connection_function(self, client):
        pass


class SshServerInterface(paramiko.ServerInterface):
    """
    Now we can override the methods that we need in order to get authentication to work. These are methods you can read about in the paramiko documentation link provide at the top of this section. If you omit these methods you won't be able to get your SSH client to connect to the server, since by default some of these methods will return values which block the connection.
    """

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_pty_request(
        self, channel, term, width, height, pixelwidth, pixelheight, modes
    ):
        return True

    def check_channel_shell_request(self, channel):
        return True
