import getpass
import imaplib
import email


imap_host = 'imap.outlook.com'
mail = imaplib.IMAP4_SSL(imap_host)
mail.login('a.myasnicova2017@outlook.com', getpass.getpass())
mail.select("check")
# mail = get_unseen(mail)
result, data = mail.uid('search', None, 'ALL')
uid_list = data[0].split()
print (len(uid_list), 'Unseen emails.')
for i in range(len(uid_list)):
    email_uid = uid_list[i]
    res, dat = mail.uid('fetch', email_uid, '(RFC822)')
    raw_email = dat[0][1]
    msg = email.message_from_bytes(raw_email)
    print ('')
    print ('New email:\n')
    print (i,'UID:', email_uid, 'Sender:', email.utils.parseaddr(msg['From'])[0],email.utils.parseaddr(msg['From'])[1])
    print ('Subjct:',msg['Subject'])
    print ('Message: ')
    print (get_body(msg))
    attach_list = get_attach_list(msg)
    print (len(attach_list),'Attachments:',attach_list, get_attach(msg))
# def get_body(msg):
#     for part in msg.walk():
#     content_type = part.get_content_type()
#     if content_type == 'text/plain' or content_type =='text/html':
#     payload = part.get_payload(decode=True)
#     if payload:
#     print payload
#     return def get_attach_list(msg):
#     attach_list=[]
#     for part in msg.walk():
#     filename = part.get_filename()
#     if filename: attach_list.append(filename)
#     return attach_list def get_attach(msg):
#     for part in msg.walk():
#     filename = part.get_filename()
#     if filename:
#     fp = open(filename,'wb') fp.write(part.get_payload(decode=True))
#     fp.close()
#     return
