from django.contrib.auth.tokens import PasswordResetTokenGenerator
#from django.utils
import six
#from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, applicant, timestamp):
        return (
            six.text_type(applicant.pk) + six.text_type(timestamp)
            # + six.text_type(applicant.is_active)
        )


account_activation_token = TokenGenerator()


