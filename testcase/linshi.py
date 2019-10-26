import time
timeStamp = 1511515800
localTime = time.localtime(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S', localTime))