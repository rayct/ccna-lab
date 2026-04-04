from netmiko import ConnectHandler

asa = {
    "device_type": "cisco_asa",
    "host": "172.16.0.1",
    "username": "admin",
    "password": "admin",
}

conn = ConnectHandler(**asa)
print(conn.send_command("show version"))
conn.disconnect()
