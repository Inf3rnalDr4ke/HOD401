#python3
import subprocess
import socket
print(" Enter the IP Address: ")
IP = input()
case=0
oct1=IP.split('.')[0]
oct2=IP.split('.')[1]
oct3=IP.split('.')[2]
last=IP.split('.')[3]
oct4=last.split('/')[0]
sub=last.split('/')[1]
if int(sub)<=24:
    sub=pow(2,24-int(sub))
    case=1
else:
    sub=pow(2,32-int(sub))
print(oct1+oct2+oct3+oct4+str(sub))
if case:
    for i in range(int(oct3),int(oct3)+sub):
        for j in range(0,255):
            ipadd = ""+str(oct1)+"."+str(oct2)+"."+str(i)+"."+str(j)
            p = subprocess.Popen(['ping',ipadd,'-c','1',"-W","2"],stdout=subprocess.PIPE)
            p.wait()
            if p.poll():
                print(ipadd+" is down")
            else:
                print(ipadd+" is up")
                for j in range(1,65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.2)
                    result = sock.connect_ex((ipadd,j))
                    if result == 0:
                        print("Port "+str(j)+" is open")
                    else:
                        pass
else:
    for i in range(0,sub):
        ipadd = ""+str(oct1)+"."+str(oct2)+"."+str(oct3)+"."+str(i)
        p = subprocess.Popen(['ping',ipadd,'-c','1',"-W","2"],stdout=subprocess.PIPE)
        p.wait()
        if p.poll():
            print(ipadd+" is down")
        else:
            print(ipadd+" is up")
            for j in range(1,65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.2)
                    result = sock.connect_ex((ipadd,j))
                    if result == 0:
                        print("Port "+str(j)+" is open")
                    else:
                        pass




