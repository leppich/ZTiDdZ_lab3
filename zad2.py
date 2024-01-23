import random
import string

def generate_password():
    min_length = 8
    criteria = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]

    password = [random.choice(criteria[i]) for i in range(4)]
    password += [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(min_length - 4)]

    random.shuffle(password)
    secure_password = ''.join(password)

    return secure_password if all(any(c in secure_password for c in crit) for crit in criteria) else generate_password()

result = generate_password()
print("Generated Password:", result)
