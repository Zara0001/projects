import imaplib
import email
from email import message
import getpass

imap = imaplib.IMAP4_SSL('imap.outlook.com')
imap.login('a.myasnicova2017@outlook.com', getpass.getpass())

imap.list()
imap.select('check')
imap.search(None, "ALL")



imap.logout()
