from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
from pathlib import Path
from dbcon import DbCon


template = Template(Path("template.html").read_text(encoding="utf-8"))
receivers = ['test@test.pl']


# providing data from database
con = DbCon()

dic = {
    "name": con.single_data("SELECT name FROM code"),
    "code": con.single_data("SELECT code FROM code"),
}


def send_emails(receivers):
    for receiver in receivers:

        message = MIMEMultipart()
        message['from'] = 'Your name'
        message['to'] = receiver
        message['subject'] = 'Test email'
        body = template.substitute(dic)
        message.attach(MIMEText(body, "html"))
        message.attach(MIMEImage(Path("image.png").read_bytes()))

        with smtplib.SMTP(host="mail-serwer21335.lh.pl", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("test@test.pl", "****")
            smtp.send_message(message)
            print(f"sent... to {receiver}")
