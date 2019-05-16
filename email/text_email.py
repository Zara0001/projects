import imaplib
import email
from email import message
import getpass
from search import srch

email_1 = 'imap.outlook.com'

email_user = 'a.myasnicova2017@outlook.com'
email_passwd = 'artem_uaga151201'

imap = imaplib.IMAP4_SSL(email_1)
imap.login(email_user, email_passwd)

imap.list()

while 1<2:

    imap.select('check')
    typ, response = imap.search(None,  'UNSEEN')
    # imap.search(None, 'ALL')
    # i = []
    if response[0] != []:
        for id in response[0].split():
        # id = response[0].split()
            status, data = imap.fetch(id, '(RFC822)')

            msg = email.message_from_bytes(data[0][1])
            subject = msg.get('Subject')

            if msg.is_multipart():

                        for part in msg.walk():

                            content_type = part.get_content_type()
                            filename = part.get_filename()
                            if filename:

                                with open(part.get_filename(), 'w') as new_file:

                                    new_file.write((str(part.get_payload(decode=True), encoding='utf-8')).lower())

                                    files = filename.split()
                                    # print(filename)
                                    # print(file)
                                    srch(files)

        for e_id in response[0].split():
            imap.store(e_id, '+FLAGS', '\Seen')

imap.logout()
