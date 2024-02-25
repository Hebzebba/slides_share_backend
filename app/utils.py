from passlib.hash import md5_crypt


def verify_hash_password(plain_password, hashed_password):
    return md5_crypt.verify(plain_password, hashed_password)


def hash_password(password):
    return md5_crypt.using(salt_size=4).hash(password)
