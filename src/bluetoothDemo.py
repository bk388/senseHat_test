import bluetooth as bt
       
devices = bluetooth.discover_devices(duration = 5, lookup_names = True)

for address, name in devices:
    print(address, name)
    