import pyotp

secret = ''

while True:
    inp = raw_input()
    if inp:
        secret = inp

    print pyotp.TOTP(secret).now()

