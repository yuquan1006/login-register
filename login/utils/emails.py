import yagmail
from new.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD


def send_email(receiver=["york.yu@ihr360.com"],):
    try:
        if '@sina.com' in EMAIL_SEND_USERNAME:
            smtp_server = 'smtp.sina.com'
        elif '@163.com' in EMAIL_SEND_USERNAME:
            smtp_server = 'smtp.163.com'
        elif '@ihr360.com' in EMAIL_SEND_USERNAME or '@cnbexpress.com' in EMAIL_SEND_USERNAME:
            smtp_server = 'smtp.mxhichina.com'
        else:
            smtp_server = 'smtp.exmail.qq.com'

        # 建立连接
        yag = yagmail.SMTP(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD, smtp_server)  # yag = yagmail.SMTP("york.yu@ihr360.com", "Admin@123", "smtp.mxhichina.com", 465)

        # 发送邮件
        yag.send(to=receiver, subject="test1",
                 contents="HI,ALL\n   \t \t IHR - 延期bug统计通知！！！请相关开发人员知晓并处理. \n \n ")
        yag.close()
        print("发送邮件成功！")
    except BaseException as e:
        print("发送邮件失败！可能出现错误的原因：%s" % e)

if __name__ == '__main__':
    send_email()