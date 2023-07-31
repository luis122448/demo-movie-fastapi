from jwt import encode, decode

key_secret = "secret"

def create_token(data: dict):
    return encode(payload=data, key = key_secret, algorithm='HS256')


def verify_token(token: str):
    try:
        return decode(jwt=token, key=key_secret, algorithms=['HS256'])
    except:
        return None