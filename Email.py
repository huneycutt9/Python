import smtplib
try:
    if 1/1 == 1:
        print "good"
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        user = '#####'
        password = '########'
        recip = ['###########']
        smtpObj.login(user,password)
        subj = 'Email through Python good'
        body = 'Hey if you get this, I figured out how to email through python with a subject and body.'
        message = 'Subject: {}\n\n{}'.format(subj, body)
        smtpObj.sendmail(user, recip, message)
        {}
        smtpObj.quit()

except:
    print "not good"
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    user = '##############'
    password = '###########'
    recip = ['####################']
    smtpObj.login(user,password)
    subj = 'Email through Python Error'
    body = 'Hey if you get this, I figured out how to email through python with a subject and body.'
    message = 'Subject: {}\n\n{}'.format(subj, body)
    smtpObj.sendmail(user, recip, message)
    {}
    smtpObj.quit()
