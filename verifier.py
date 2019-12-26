import random
from typing import Tuple
import mailer
import config


def get_secret_code() -> int:
    return random.randint(1000000, 9999999)


def get_parameters(raw_parameters: dict) -> Tuple[str, str]:
    email = ''
    language = config.BY

    if 'address' in raw_parameters:
        email = raw_parameters['address'].replace('%40', '@')

    if 'language' in raw_parameters:
        if raw_parameters['language'] == config.RU:
            language = config.RU

    return email, language


def send_verification_mail(raw_parameters: dict) -> str:
    email, language = get_parameters(raw_parameters)

    if not email:
        return config.FAIL

    secret_code = get_secret_code()

    if mailer.send_mail(email, secret_code, language) in config.SUCCESS_CODES:
        print(f"email: {email}, code: {str(secret_code)}")
        return str(secret_code)
    else:
        print(f"email: {email}, fail")
        return config.FAIL
