def CDT(usuario: str, capital: int, tiempo: int):
    porcentaje_interes = 0.03
    porcentaje_perder = 0.02
    valor_total = 0

    if(tiempo > 2):
        valor_interes = (capital*porcentaje_interes*tiempo)/12
        valor_total = capital + valor_interes
    else:
        valor_perder = capital*porcentaje_perder
        valor_total = capital - valor_perder
    # return 'Para el usuario '+str(usuario)+' La cantidad de dinero a recibir, según el monto inicial '+str(capital)+' para un tiempo de '+str(tiempo)+ ' meses es: '+str(Valor_total)
    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"


# print(CDT("Pepe", 5400, 5))
print(CDT("AB1012",1000000,3))