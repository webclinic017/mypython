import smtplib

gmail_user = 'owenyang15@gmail.com'
gmail_password = '222121wj'

sent_from = gmail_user
to = ['owenyang15@gmail.com', 'anlerme@gmail.com']
subject = 'OMG Super Important Message'
body = "Hey, what's up?"
email_text="hi this is Owen what is your ssn"
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:
    print 'Something went wrong...'