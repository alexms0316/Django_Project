import re

from django.core.exceptions import ValidationError

def email_validate(value):
    EMAIL_REGEX = '[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+'
    if not re.match(EMAIL_REGEX, value):
        raise ValidationError('INVALID_EMAIL')
        
def password_validate(value):
    PASSWORD_REGEX = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
    if not re.match(PASSWORD_REGEX, value):
        raise ValidationError('INVALID_PASSWORD')