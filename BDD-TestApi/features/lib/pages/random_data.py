from string import ascii_lowercase, ascii_letters, ascii_uppercase, digits
from secrets import choice
import uuid


class GeneratorRandomData:

    def random_name(self, lenght=5):
        characters = ascii_letters + ascii_uppercase + ascii_lowercase
        length = lenght
        chain = ''.join(choice(characters) for char in range(length))

        return chain

    def random_email(self, lenght=5):
        characters = ascii_lowercase + digits
        length = lenght
        chain = ''.join(choice(characters) for char in range(length))

        return chain

    def guid_pass(self):

        return str(uuid.uuid4())


