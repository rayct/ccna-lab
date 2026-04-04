from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "10.0.0.1", "username": "admin", "cisco": "admin"},
    {"device_type": "cisco_ios", "host": "192.168.30.1", "username": "admin", "cisco": "admin"},
    {"device_type": "cisco_ios", "host": "192.168.30.2", "username": "admin", "cisco": "admin"},
]

for device in devices:
    print(f"\nConnecting to {device['host']}")

    conn = ConnectHandler(**device)
    output = conn.send_command("show ip interface brief")
    print(output)
    conn.disconnect()
