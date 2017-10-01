import threading
import time


def timer(name, delay, repeat):
    print 'Timer' + name + ' delay'

    while repeat > 0:
        time.sleep(delay)
        print name + ':' + str(time.ctime(time.time()))
        repeat -= 1
    print '{} had completed'.format(name)

def customer(name, location,sleep):
    time.sleep(sleep)
    print 'The customer name is {} and location is {} \n'.format(name,location)


def main():
    t1 = threading.Thread(target=timer, args=('timer1', 2, 8))
    t2 = threading.Thread(target=timer, args=('timer2', 4, 8))
    t3 = threading.Thread(target=customer,args=('Orange','France',10))
    t1.start()
    t2.start()
    t3.start()
    print 'Main function  is completed'


if __name__ == '__main__':
    main()
