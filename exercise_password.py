def password():
    contrasena = input()
    tiene_longitud = len(contrasena) >= 8
    tiene_numero = (
            "0" in contrasena or
            "1" in contrasena or
            "2" in contrasena or
            "3" in contrasena or
            "4" in contrasena or
            "5" in contrasena or
            "6" in contrasena or
            "7" in contrasena or
            "8" in contrasena or
            "9" in contrasena
    )
    if tiene_longitud and tiene_numero:
        print("Contraseña valida")
    else:
        if not tiene_longitud:
            print("Contraseña muy corta")
        if not tiene_numero:
            print("Debe contener un numero")
