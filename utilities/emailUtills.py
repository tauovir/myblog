from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

def sendMail(name, fromEmail, subject, bodyMessage):
    subject = subject
    to_email = settings.DEFAULT_TO_EMAIL
    message = bodyMessage
    name = name
    emailData = {
        'name' :name,
        'message' : message,
        'email' : fromEmail,
    }
    print("To email: ",to_email)
    messageTemplate = get_template('emails/contactus.html').render(emailData)
    response = send_mail(
        subject,
        messageTemplate,
        fromEmail,
        [to_email],
        fail_silently=True
    )
    return response
    