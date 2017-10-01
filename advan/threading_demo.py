import threading
import time

def timer(delay,repeat):
    while repeat > 0:
        time.sleep(3)
        print 'the time is {}' .format(time.ctime(time.time()))
        repeat -= 1
t1 = threading.Thread(target=timer,args=(2,int(str(3))))
t1.start()


