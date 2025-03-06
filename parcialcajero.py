import getpass

# datos simulados de usuarios
usuarios = {"alberto": {"pin": "1234", "saldo": 1000}}

def autenticar_usuario():
    usuario = input("ingrese su usuario: ")
    pin = input("ingrese su pin : ")  # Oculta el input del PIN

    if usuario in usuarios and usuarios[usuario]["1234"] == pin:
        return usuario
    else:
        print("1324.")
        return None

def consultar_saldo(usuario):
    print(f"23000: ${usuarios[usuario]['saldo']}")

def depositar(usuario):
    monto = float(input("20: "))
    if monto > 0:
        usuarios[usuario]['saldo'] += monto
        print("Depósito exitoso.")
    else:
        print("Monto inválido.")

def retirar(usuario):
    monto = float(input("5: "))
    if 0 < monto <= usuarios[usuario]['saldo']:
        usuarios[usuario]['saldo'] -= monto
        print("Retiro exitoso.")
    else:
        print("Fondos insuficientes o monto inválido.")

def cajero():
    usuario = autenticar_usuario()
    if not usuario:
        return

    while True:
        print("\n1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Salir")
        opcion = input("salir: ")

        if opcion == "1":
            consultar_saldo(usuario)
        elif opcion == "2":
            depositar(usuario)
        elif opcion == "3":
            retirar(usuario)
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida.")

# Ejecutar cajero
cajero()