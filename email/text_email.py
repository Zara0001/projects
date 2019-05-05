import imaplib
import email
from email import message
import getpass

imap = imaplib.IMAP4_SSL('imap.outlook.com')
imap.login('a.myasnicova2017@outlook.com', getpass.getpass())

imap.list()
imap.select('check')
imap.search(None, "ALL")

# imap.fetch(b'1', ('HTML'))
status, data = imap.fetch(b'1', ('RFC822'))

msg = email.message_from_bytes(data[0][1],
    _class = email.message.EmailMessage)
        # parser subject
subject = msg.get('Subject')

        # parser body
if msg.is_multipart():
    for part in msg.get_payload():
        if part.get_content_maintype() == 'text' and part.get('Content-Disposition') == None:
            msg_body = part.get_payload(decode=1)

            f = open('data.txt', 'w')
            f.write(str(msg_body))
            # print(msg_body)
else:
    msg_body = msg.get_payload()

imap.logout()
