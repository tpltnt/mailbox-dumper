#!/usr/bin/env python3
import getpass, poplib, socket, sys

if not (2 == len(sys.argv) or 3 == len(sys.argv)):
    print("usage: " + str(sys.argv[0]) + " hostname(:port) (username)")
    sys.exit(1)

# set account parameter & connect
try:
    if ':' in sys.argv[1]:
        host = sys.argv[1].split(':')[0]
        portnumber = sys.argv[1].split(':')[1]
        account = poplib.POP3_SSL(host,port=portnumber)
    else:
        account = poplib.POP3_SSL(sys.argv[1])
except socket.gaierror:
    print("can not connect to '" + str(sys.argv[1]) + "' on the default SSL port")
    sys.exit(2)


# send login credentials
if 2 == len(sys.argv):
    account.user(getpass.getuser())
else:
    account.user(sys.argv[2])

account.pass_(getpass.getpass())
# get basic statistics
print("found " + str(account.stat()[0]) + " messages taking "
      + str(account.stat()[1]) + " octets of space")
# iterate over all messages
msg_count = len(account.list()[1])
for i in range(msg_count):
    for j in account.retr(i+1)[1]:
        # print each message
        print(j)
# unlock mailbox and sign off
account.quit()
