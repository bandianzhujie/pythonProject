import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.126.com"  # SMTP服务器
mail_user = "benpaodelongxiaqd"  # 用户名
mail_pass = "Pw8992311"  # 密码

sender = 'benpaodelongxiaqd@126.com'
receivers = ['1009853267@qq.com']


msg = MIMEText("The body of the email is here !")

msg['Subject'] = "An Email Alert"
msg['From'] = "benpaodelongxiaqd@126.com"
msg['To'] = "1009853267@qq.com"


smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
smtpObj.login(mail_user, mail_pass)
smtpObj.send_message(msg)
smtpObj.quit()