import imaplib
from email import message
import email
import getpass

imap = imaplib.IMAP4_SSL('imap.outlook.com') # ЗАХОДИМ НА СЕРВЕР
# imap.login('a.myasnicova2017@outlook.com', getpass.getpass('Pasword :')) # ЗАХОДИМ НА СВОЮ ПОЧТУ
imap.login('a.myasnicova2017@outlook.com', 'artem_uaga151201') # ЗАХОДИМ НА СВОЮ ПОЧТУ

imap.list() # СМОТРИМ СПИСОК ДОСТУПНЫХ ПАПОК ("INBOX", "Sent", и т.д.)
imap.select("check") # ПОДКЛЮЧАЕМСЯ К НУЖНОЙ НАМ ПАПКЕ
imap.search(None, "ALL") # ПОЛУЧАЕМ СПИСОК ID ЧЕРЕЗ ПРОБЕЛ

status, data = imap.fetch(b'2' , '(RFC822)') # ЗАГРУЖАЕМ НУЖНОЕ НАМ ПИСЬМО
msg = email.message_from_bytes(data[0][1],
    _class = email.message.EmailMessage)

b = email.message_from_string(msg[''])

# print(msg['Subject'])
f=open('data', 'w')
# typ, data = imap.fetch(data[0], '(RFC822)')
f.write('Message %sn%sn' % (status, data[0][1]))

f.close()
imap.close()
imap.logout()
