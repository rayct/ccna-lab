from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.40.1",
    "username": "admin",
    "password": "admin",
}

connection = ConnectHandler(**device)
output = connection.send_command("show ip interface brief")
print(output)
connection.disconnect()
