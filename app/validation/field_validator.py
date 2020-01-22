from email_validator import validate_email, EmailNotValidError

class FieldValidator(object):

    @staticmethod
    def isEmpty(values):
        return true if [x for x in values if x] else false

    @staticmethod
    def validateEmail(email):
        try:
            v = validate_email(email)
            return true
        except EmailNotValidError as e:
            print(str(e))
            return false