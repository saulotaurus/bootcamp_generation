
# Menú principal

def menu():
    nombre = ""
    edad = 0
    cargo = ""
    sueldo = 0
    porcentaje = 0.0
    total = None  # None indica que aún no se calculó el bono para diferenciarlo de 0

    while True:
        print("\n=== Menú ===")
        print("1. Ingresar datos del empleado")
        print("2. Calcular bono")
        print("3. Mostrar resumen")
        print("4. Salir")

        try:
            opcion = int(input("Ingrese la opción deseada: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        mensaje = ""


        # Opciones del menú

        if opcion == 1:
            nombre, edad, cargo, sueldo, porcentaje = ingresar_datos()
            mensaje = "Datos ingresados correctamente."

        elif opcion == 2:
            if nombre == "":
                mensaje = "Primero debe ingresar los datos del empleado."
            else:
                total = calcular_bono(sueldo, porcentaje)
                mensaje = "Bono calculado correctamente."

        elif opcion == 3:
            if total is None:
                mensaje = "Primero debe calcular el bono antes de mostrar el resumen."
            else:
                mostrar_resumen(nombre, edad, cargo, total)
                mensaje = ""  # No se necesita mensaje adicional

        elif opcion == 4:
            mostrar_mensaje_despedida()
            break

        else:
            mensaje = "Opción inválida. Intente nuevamente."

        if mensaje:
            print("\n" + mensaje)


# Función de despedida

def mostrar_mensaje_despedida():
    print("\n==== Gracias por calcular con nosotros ===\n")


# Ejecutar el menú

if __name__ == "__main__":
    menu()


