import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('192.168.0.111',port=22,username='goku',password='goku')
import imp
print imp.find_module('re')