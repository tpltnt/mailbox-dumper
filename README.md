mailbox-dumper
==============

Dump and clean up your email inbox via [POP3](https://tools.ietf.org/html/rfc1939).
You have have to provide a hostname and can optionally provide a port
and a username. If no username is provided, the system username/loginname
will be used. For eample ```maildumper.py mail.example.net:2342 janedoe```
connects to the host mail.example.net at port 2342 and tries to log in
using the name janedoe. 
This script does *not* perserve any folder structure. It just downloads
and deletes all messages. It uses TLS (SSL) but currently does not make 
extensive checks with regards to security.

License: AGPL

Dependencies
------------
* [python 3](http://www.python.org)
