import speedtest

test = speedtest.Speedtest()
down = test.download()
up = test.upload()

down = (down/1024)/1024
up = (up/1024)/1024

print(f"Speed test by Mr-Cuda")
print(f"Download speed: {round(down, 2)} Mbps")
print(f"Upload speed: {round(up, 2)} Mbps")
