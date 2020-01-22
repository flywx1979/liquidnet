from ..validation.field_validator import FieldValidator

class Validator:
   @staticmethod
   def validate(inputs):
       return FieldValidator.isEmptry([inputs["title"]), inputs["email"]]) \
              and FieldValidator.validateEmail(inputs["email"])