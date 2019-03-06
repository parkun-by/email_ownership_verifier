import config
import sendgrid
from sendgrid.helpers.mail import *


def send_mail(email, code):
    sg = sendgrid.SendGridAPIClient(apikey=config.API_KEY)
    from_email = Email(config.FROM_EMAIL)
    to_email = Email(email)
    subject = 'Код подтверждения email для бота "Паркун"'
    content = Content('text/plain', 'Ваш код подтверждения: ' + str(code))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return str(response.status_code)
