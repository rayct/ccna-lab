from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.30.1",
    "username": "admin",
    "password": "admin",
}

conn = ConnectHandler(**device)

output = conn.send_command("show version")
print(output)

conn.disconnect()
