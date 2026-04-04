from netmiko import ConnectHandler

asa = {
    "device_type": "cisco_asa",
    "host": "172.16.0.1",
    "username": "admin",
    "password": "password1234",
}

conn = ConnectHandler(**asa)
print(conn.send_command("show version"))
conn.disconnect()
