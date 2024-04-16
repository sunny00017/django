import smtplib
content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='shivampandey74826@gmail.com'
recipient='pshivam941@gmail.com'
mail.login('shivampandey74826@gmail.com','lfra pnnl sstf atue')
header='To:'+recipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()