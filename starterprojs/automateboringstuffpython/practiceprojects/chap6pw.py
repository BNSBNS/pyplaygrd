#! /usr/bin/python3
# pw.py, an insecure password locker program

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('usage: py pw.py [account] - copy acc pw')
    sys.exit()

account = sys.argv[1] #first cl arg is the acc name.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('there is no acc for ' + account)