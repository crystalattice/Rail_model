from urllib import request
import time

# url = input("Please provide the stream's IP address and port. Format should be x.x.x.x:xxxx ")
url = "http://192.168.0.112:8081"
response = request.urlopen(url)
filename = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".mp4"

block_size = 1024

start_time = time.time()
time_limit = 10

print("Recording video...")

with open(filename, 'wb') as video_file:
    while (time.time() - start_time) < time_limit:  # Record for 10 seconds
        try:
            buffer = response.read(block_size)
            if not buffer:
                break
            video_file.write(buffer)
        except Exception as e:
            print(e)
