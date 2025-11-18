from netmiko import ConnectHandler

def acces_netmiko():
    cisco_device = {
        "device_type": "cisco_xr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    net_connect = ConnectHandler(**cisco_device)
    clock = net_connect.send_command("show clock")
    print("Heure du routeur :", clock)

    interfaces = net_connect.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)

acces_netmiko()