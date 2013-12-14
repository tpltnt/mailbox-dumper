#!/usr/bin/env python3
import getpass, poplib, socket, sys

if 2 != len(sys.argv):
    print("usage: " + str(sys.argv[0]) + " hostname")
    sys.exit(1)

# set account parameter & connect
try:
    account = poplib.POP3_SSL(sys.argv[1],port=10101)
except socket.gaierror:
    print("can not connect to '" + str(sys.argv[1]) + "' on the default SSL port")
    sys.exit(2)

account.user(getpass.getuser())
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
