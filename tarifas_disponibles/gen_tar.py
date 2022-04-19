gamas = {'BAJA' : 5, 'MEDIA' : 10, 'ALTA' : 20}
tipos = {'DIA_KM' : 3, 'DIA_KM_ILIM' : 27, 'FIN_SEMANA' : 24, 'SEMANAL' : 13, 'LARGA_DURACION' : 513}
temporadas = {1 : 5, 2 : 3, 3 : 9}

i = 1
for tipo in tipos:
    for gama in gamas:
        if tipo == 'LARGA_DURACION':
            temporada = 0
            precio = 50 + gamas[gama] + tipos[tipo]
            print(f't{i} = Tarifas.objects.create(tipo=TiposDeTarifas.{tipo}, gama=TiposDeGamas.{gama}, precio = {precio}, temporada = {temporada})')
            i += 1
        else:
            for temporada in temporadas:
                precio = 50 + gamas[gama] + tipos[tipo] + temporadas[temporada]
                print(f't{i} = Tarifas.objects.create(tipo=TiposDeTarifas.{tipo}, gama=TiposDeGamas.{gama}, precio = {precio}, temporada = {temporada})')
                i += 1
