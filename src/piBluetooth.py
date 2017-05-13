import bluetooth as bt

class btDevice():
    
    deviceName = None
    deviceAddress = None
    socket = None
    port = 0
    
    def __init__(self, port=1):
        self.port = port
        
    def search(self, duration=1, lookup_names=True):
        devices = bt.discover_devices(duration=duration, lookup_names=lookup_names)
        return devices
        
    def connect(self, devName=None, devAddress=None, searchTime=5):
        if devAddress == None and devName == None:
            raise ValueError("No device specified")
        else:
            byName = True
            byAddress = True
            if devName == None:
                byName = False
            if devAddress == None:
                byAddress = False
                       
        connected = False
        devices = self.search(searchTime)
        
        if byName and byAddress:
            for address, name in devices:
                if address == devAddress and name == devName:
                    self.deviceName = name
                    self.deviceAddress = address
                    connected = True
        elif byName: 
            for address, name in devices:
                if name == devName:
                    self.deviceName = name
                    self.deviceAddress = address
                    connected = True
        else:
            for address, name in devices:
                if address == devAddress:
                    self.deviceName = name
                    self.deviceAddress = address
                    connected = True
                    
        self.socket = bt.BluetoothSocket(bt.RFCOMM)
        self.socket.connect(self.deviceAddress, self.port)
        
        return connected