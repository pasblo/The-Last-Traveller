import smtplib
from email.mime.text import MIMEText
tx = open('servicio.txt', 'rb')
mensaje = MIMEText(tx.read())
tx.close()
mensaje['Subject'] = 'si ves esto es que funciono el codigo jajajajaja' #tema
mensaje['From'] = 'carraro.fernando@gmail.com'
#es es un mensaje
smtpserver = "smtp.gmail.com"
smtpuser = "carraro.fernando@gmail.com"#tu usr smtp, tu usuario gmail
smtppassword = "xb10dual"#tu pass smtp
SENDER = "carraro.fernando@gmail.com"
RECIPIENTS = "jhon.alex.pineda89@gmail.com" #email del destinatario
session = smtplib.SMTP(smtpserver, 587)
session.ehlo()
session.starttls()
session.ehlo()
session.login(smtpuser, smtppassword)
session.sendmail(SENDER, RECIPIENTS, mensaje.as_string())
session.quit()
