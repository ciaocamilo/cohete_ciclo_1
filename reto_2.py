def cliente(informacion: dict) -> dict:
    cliente_id = informacion['id_cliente']
    cliente_nombre = informacion['nombre']
    cliente_edad = informacion['edad']
    cliente_primer_ingreso = informacion['primer_ingreso']

    if cliente_edad > 18:
        atraccion = 'X-Treme'
        apto = True
        if cliente_primer_ingreso == True:
            total_boleta = 20000 - (20000*0.05)
        else:
            total_boleta = 20000
    elif cliente_edad >= 15 and cliente_edad <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if cliente_primer_ingreso == True:
            total_boleta = 5000 - (5000*0.07)
        else:
            total_boleta = 5000
    elif cliente_edad >= 7 and cliente_edad < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if cliente_primer_ingreso == True:
            total_boleta = 10000 - (10000*0.05)
        else:
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'

    diccionario_respuesta = {
        'nombre': cliente_nombre,
        'edad': cliente_edad,
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': cliente_primer_ingreso,
        'total_boleta': total_boleta
    }

    return diccionario_respuesta




# informacion = {
#     'id_cliente':1,
#     'nombre':'Johana Fernandez',
#     'edad':20,
#     'primer_ingreso':True
# }

informacion = {
    'id_cliente':2,
    'nombre':'Gloria Suarez',
    'edad':3,
    'primer_ingreso':True
}

print(cliente(informacion))