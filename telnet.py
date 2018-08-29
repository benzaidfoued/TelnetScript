import telnetlib
import time

def OpenTelnet(ip):

     username = "teopy"
     password = "python"
     port = "23"

     file_input = input("‪C:\Users\root\Desktop\config.txt")

     conn_timeout = 5
     read_delay = 5

     connexion = telnetlib.Telnet(ip,port,conn_timeout)

     connexion.read_until('username',read_delay)
     connexion.write(username + "\n")
     time.sleep(3)
     #waiting for the password prompt

     router_output = connexion.read_until('password',read_delay)
     connexion.write(password + "\n")
     time.sleep(1)

     config_file = open(file_input,'r')

     config_file.seek(0)

     for config in config_file.readlines():
         connexion.write(config + "\n")
         time.sleep(1)
    # config_file.close()

    router_output = connexion.read_very_eager()
    print(router_output)

    connexion.close()

    OpenTelnet(192.168.0.220)     

     
