
def password_generator():

    import random
    import string
    import json

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    total_characters = lowercase + uppercase + symbols + numbers

    length = 15
    password = ''
    for i in range(length):
        password = password + random.choice(total_characters)

    print(password)

    password_data = ['Passwords:', password]

    with open('passwords.txt', 'r+') as stored_file:
        other_passwords = stored_file.read()
        if other_passwords == '':
            stored_file.write('\n'.join(password_data))
            
        else:
            stored_file.write('\n' + password)
            
        stored_file.close()
