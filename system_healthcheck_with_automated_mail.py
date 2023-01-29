import psutil as ut
import platform as plt
import uuid, datetime, socket, ssl
import smtplib as smt
import custom_modules.credentials as cred # put your own credential file in the main directorty
from email.message import EmailMessage
from sys import stdin
from custom_modules.smtp_connector import connect
from  custom_modules.system_checks import *


def main():
    port = 465
    smtp_mailaddr = 'smtp.gmail.com'
    from_id = cred.from_id
    passwd = cred.from_id_passwd
    to_id = input("\nEnter recipients's IDs seperated by comma.\n").split(',')
    cc = input("\nEnter CC recipients's IDs seperated by comma.\n").split(',')
    subject = input('\nEnter the Subject here:\n')
    sender = input('\nEnter the sender name: ')

    message = '%s\n\n%s\n%s\n\n%s\n\n%s\n%s\n\n%s\n%s\n\n%s\n\nSent by: %s'%(msg_body(), host(), cpu(), memory(), disk(), line(), system(), uid(), date_time(), sender)
    msg = EmailMessage()
    msg.set_content(message) 
    msg['Subject'] = subject
    msg['From'] = from_id
    msg['To'] = ', '.join(to_id)
    msg['Cc'] = ', '.join(cc)

    connect(smtp_mailaddr, port, from_id, passwd, to_id, msg)

if __name__ == '__main__':
    main()
else:
    print('Please run the main file')
