import random
import string


def get_random_password() -> str:
    return "".join(random.sample(string.ascii_letters + string.digits, 8))


print(get_random_password())
