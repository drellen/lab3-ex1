

import smtplib

fromaddr = 'drellenster@gmail.com'
toaddr  = 'dre_allen@hotmail.com'
fromname = 'The One'
toname = 'Teach'
subject = 'Test'


message = "From: %s\nTo: %s\nFromName: %s\ntoName: %s\nSubject\n%s" % ( fromaddr, toaddr, fromname, toname, subject,)



messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             message)

# Credentials (if needed)
username = 'drellenster@gmail.com'
password = 'svnvsegwoklmxyge'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()
