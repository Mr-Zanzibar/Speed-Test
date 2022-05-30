class color:
   CYAN = '\033[96m'
    
import speedtest
from colorama import init
init(autoreset=True)

test = speedtest.Speedtest()
down = test.download()
up = test.upload()

down = (down/1024)/1024
up = (up/1024)/1024

print(f' ')
print(color.CYAN + f 'Speed test by Mr-Cuda') # yes I want to take credits for 8 lines of code
print(color.CYAN + f 'Download speed: {round(down, 2)} Mbps')
print(color.CYAN + f 'Upload speed: {round(up, 2)} Mbps')
print(f' ')
