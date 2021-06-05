import config
import sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail


def send_mail(email, code, language):
    sg = sendgrid.SendGridAPIClient(config.API_KEY)
    from_email = Email(config.FROM_EMAIL)
    to_email = To(email)

    if language == config.RU:
        subject = 'Код подтверждения email для бота "Паркун"'
        content = Content('text/plain', 'Ваш код подтверждения: ' + str(code))
    else:
        subject = 'Код пацверджання email для бота "Паркун"'
        content = Content('text/plain', 'Ваш код пацверджання: ' + str(code))

    mail = Mail(from_email=from_email,
                subject=subject,
                to_emails=(to_email),
                plain_text_content=content)

    response = sg.client.mail.send.post(request_body=mail.get())
    return str(response.status_code)
