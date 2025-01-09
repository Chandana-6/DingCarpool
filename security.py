from settings import SECURITY_KEY

def validate_security_key(sk):
    if sk != SECURITY_KEY:
        return "0_sec_9999"
    return None



