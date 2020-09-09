import uuid
from string import ascii_uppercase, ascii_letters, digits, ascii_lowercase
from secrets import choice
guid_let = str(uuid.uuid4())
keywords = guid_let.split("-")

print(keywords)



characters = ascii_letters + ascii_uppercase + digits
length = 100
chain = ''.join(choice(characters) for char in range(length))

print(chain)
texto = 'Nkwj2KkVcC   '
print(texto)
print(texto.strip(' '))

