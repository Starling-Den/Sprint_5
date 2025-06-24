import random
import string

class DataGenerator:
    @staticmethod
    def name_generator():
        name_length = random.randint(3, 9)
        name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
        return name

    @staticmethod
    def email_generator():
        domen = ["@yandex.ru", "@mail.ru"]
        email_length = random.randint(3, 9)
        email = ''.join(random.choices(string.ascii_letters + string.digits, k=email_length)) + random.choice(domen)
        return email

    @staticmethod
    def password_generator():
        password_length = random.randint(6, 10)
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        return password