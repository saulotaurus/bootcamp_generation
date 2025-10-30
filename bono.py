def calcular_bono(sueldo, porcentaje):
    bono = sueldo*(porcentaje/100) 
    sueldo_total = sueldo+bono
    return sueldo_total 