#!/usr/bin/env python3
import getpass, poplib, sys

if 2 != len(sys.argv):
    print("usage: " + str(sys.argv[0]) + " hostname")
    sys.exit(1)

# set account parameter & connect
account = poplib.POP3_SSL(sys.argv[1])
account.user(getpass.getuser())
account.pass_(getpass.getpass())
# iterate over all messages
msg_count = len(account.list()[1])
for i in range(msg_count):
    for j in account.retr(i+1)[1]:
        # print each message
        print(j)
