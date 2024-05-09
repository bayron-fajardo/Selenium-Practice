import bcrypt


pwd = b'$2b$12$05FTnULrkLhxsw0dUAAQWufCELni8w7GZucnzT5FFNPoHJRSUjFO.'

txt = bytes(input("Ingrese un texto: "), "utf-8")

if bcrypt.checkpw(txt,pwd):
    print("La contraseñas coinciden")

else:
    print("La contraseñas no coinciden")