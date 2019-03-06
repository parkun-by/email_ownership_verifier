import random
import mailer
import config


def get_secret_code():
    return random.randint(1000000, 9999999)


def get_parameters(raw_parameters):
    if 'address' in raw_parameters:
        return raw_parameters['address'].replace('%40', '@')
    else:
        return ''


def send_verification_mail(raw_parameters):
    email = get_parameters(raw_parameters)

    if not email:
        return config.FAIL

    secret_code = get_secret_code()

    if mailer.send_mail(email, secret_code) in config.SUCCESS_CODES:
        return str(secret_code)
    else:
        return config.FAIL
