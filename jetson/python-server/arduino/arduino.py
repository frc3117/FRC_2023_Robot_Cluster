import serial

from threading import Thread

class Arduino:
    def __init__(self, port: str, baudrate: int = 9600):
        self.__port__ = port
        self.__baudrate__ = baudrate

        self.__arduino__: serial.Serial = None
        self.__should_run__ = False

    def start(self):
        self.__should_run__ = True

        t = Thread(daemon=False, target=self.__loop__)
        t.start()

    def stop(self):
        self.__should_run__ = False

    def __loop__(self):
        self.__arduino__ = serial.Serial(port=self.__port__,
                                         baudrate=self.__baudrate__)

        while self.__should_run__:
            if not self.__arduino__.is_open:
                self.__should_run__ = False
                break

            if (self.read_bytes(1) == b'$' and self.__arduino__.read(1) == b'$'):
                msgLen = self.read_byte_as_int()
                msgType = self.read_byte_as_int()

    def read_bytes(self, byte_count: int) -> bytes:
        return self.__arduino__.read(byte_count)
    
    def read_byte_as_int(self) -> int:
        return int.from_bytes(self.read_bytes(1), 'little')
    
    def read_string(self) -> str:
        return self.read_bytes(self.read_byte_as_int()).decode('utf-8')