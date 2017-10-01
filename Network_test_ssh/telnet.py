import telnetlib
import getpass

host = '192.168.11.11'

username = 'goku'
password = getpass.getpass()
tn = telnetlib.Telnet(host)
print 'check1'
tn.read_until('Username: ')
print 'check2'
tn.write(username + '\n')
print 'check3'
if password:
    tn.read_until('Password: ')
    tn.write(password + '\n')

tn.write('conf t\n')
tn.write('interface lo0 \n')
tn.write('ip add 1.1.1.1 255.255.255.255 \n')
tn.write('exit\n')
tn.write('router os 1 \n')
tn.write('network 2.2.2.2 255.255.255.255 a 0 \n')
tn.write('end\n')
tn.write('exit\n')
print tn.read_all()
