from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = mutugieddie3@gmail.com

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**mango)
    email.html = render_template(template + ".html",**mango)
    mail.send(email)
