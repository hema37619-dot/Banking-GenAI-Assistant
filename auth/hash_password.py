import bcrypt

def hash_password(password) :

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hashed.decode('utf-8')

def verify_password(password, hashed):

    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8')

    return bcrypt.checkpw(password.encode('utf-8'), hashed)