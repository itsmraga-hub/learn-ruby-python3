import secrets


def private_key(p):
    pass


def public_key(p, g, private):
    pass


def secret(p, public, private):
    pass


# print(dir(secrets))
print(secrets.token_urlsafe())