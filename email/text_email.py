import imaplib
import email
from email import message
import getpass

# email_servis = {
#     'yandex' : 'imap.yandex.com',
#     'outlook' : 'imap.outlook.com',
#     'gmail' : 'imap.gmail.com'
# }

email_1 = 'imap.outlook.com'

email_user = 'a.myasnicova2017@outlook.com'
email_passwd = 'artem_uaga151201'

imap = imaplib.IMAP4_SSL(email_1)
imap.login(email_user, email_passwd)

imap.list()
imap.select('check')
imap.search(None, "ALL")

status, data = imap.fetch(b'7', '(RFC822)')
# msg = email.message_from_bytes(data[0][1],
#     _class = email.message.EmailMessage)

msg = email.message_from_bytes(data[0][1])
subject = msg.get('Subject')

if msg.is_multipart():
    # for part in msg.get_payload():
    #     if part.get_content_maintype() == 'text' and part.get('Content-Disposition') == None:
    #         # msg_body = part.get_payload(decode=1)
    #         msg_body = part.get_payload()
    #
    #         # msg_body = (bytes(msg_body).decode('cp1251'))
    #
            # f = open('data.html', 'w')
    #         f.write(str(msg_body))
            # print(msg_body)

            for part in msg.walk():
                content_type = part.get_content_type()
                filename = part.get_filename()
                if filename:
                    # Нам плохого не надо, в письме может быть всякое барахло
                    with open(part.get_filename(), 'w') as new_file:
                        new_file.write((str(part.get_payload(decode=True), encoding='utf-8')).lower())
            # f.close

imap.logout()
