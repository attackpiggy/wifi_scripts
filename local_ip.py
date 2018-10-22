import socket





def get_Host_IP():
    try:
        
        host_name=socket.gethostname()
        host_ip=socket.gethostbyname(host_name)
        print("HostName: ",host_name)
        print("IP: ",host_ip)
    except:
         
         print("Unable to fetch informtaion")
        


    f=open('ip.txt','w')
    f.write(host_name)
    f.write(host_ip)


interface="wlan0"
    

    
    

get_Host_IP()
