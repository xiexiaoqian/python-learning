"""
发送邮件
smtplib和email为python内置模块
"""
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
# 负责构造邮件头信息
from email.header import Header
# SMTP服务器，这里使用qq邮箱
mail_host = 'smtp.qq.com'
# 发件人邮箱
mail_sender = '2320832818@qq.com'
# 邮箱授权码，注意这里不是邮箱密码！！！
mail_license = 'sixwtkpvebjldihj'
# 收件人邮箱，可以为多个收件人
mail_receivers = ['1224178565@qq.com']
# 构建MIMEMultipart对象代表邮件本身，可以往里面添加文本、图片、附件等
mm = MIMEMultipart('related')
# 邮件主题
subject_content = """夜班"""
# 设置发送者，注意格式，里面邮箱为发件人邮箱
mm['From'] = '谢晓茜<2320832818@qq.com>'
# 设置接受者，注意格式，里面邮箱为接收者邮箱，可以设置多个
mm['To'] = '张浩杰<1224178565@qq.com>'
# 设置邮件主题
mm['Subject'] = Header(subject_content, 'utf-8')
# 邮件正文内容
body_content = """夜班"""
# 构造文本，参数1：正文内容，参数2：文本格式，参数3：编码方式
message_text = MIMEText(body_content, 'plain', 'utf-8')
# 想MIMEMultipart对象中添加文本对象
mm.attach(message_text)
# 构造附件
atta = MIMEImage(open('./res/img/output3.png',
                      'rb').read())
# 设置附件信息
atta['Content-Disposition'] = 'attachment; filename="词云.png"'
# 添加附件到邮件信息当中去
mm.attach(atta)
# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)
# set_debugleve(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender, mail_license)
# 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式转成str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print('邮件发送成功')
# 关闭SMTP对象
stp.quit()
