#!/usr/bin/env python3
import getpass, poplib, sys

account = poplib.POP3_SSL(sys.argv[1])
account.user(getpass.getuser())
account.pass_(getpass.getpass())
msg_count = len(account.list()[1])
for i in range(msg_count):
    for j in account.retr(i+1)[1]:
        print(j)
