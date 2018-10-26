from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "mail.qq.com"
app.config["MAIL_PORT"] = 465  # 设置邮箱端口为465，默认为25，由于阿里云禁止了25端口，所以需要修改
app.config["MAIL_USE_SSL"] = True  # 163邮箱需要开启SSL
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USERNAME"] = "1990486426@qq.com"
app.config["MAIL_PASSWORD"] = "cynvreytmqndcicj"

mail = Mail(app)


@app.route("/")
def send_mail():
    """
    发送邮件， sender为发送者邮箱， recipients为接受者邮箱
    """
    message = Message("测试邮件标题122", sender=app.config["MAIL_USERNAME"], recipients=["1990486426@qq.com"])
    message.body = "测试邮件的内容122"

    send_email(message)

    return "发送成功"


def send_email(msg):
    with app.app_context():
        mail.send(msg)


if __name__ == "__main__":
    app.run()
