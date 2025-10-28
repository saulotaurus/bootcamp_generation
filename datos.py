def ingresar_datos():
    nombre = str((input("Ingrese su nombre: ")))
    edad = int(input("Ingrese su edad: "))
    cargo = str((input("Ingrese su cargo: ")))
    porcentaje = float(input("Ingrese el porcentaje de bono que recibe (sin el símbolo %): "))
    sueldo = float(input("Ingrese su salario mensual: "))
    return nombre, edad, cargo, porcentaje, sueldo


