#tahia teran
#03/04/2025

altura =int(input('cual es tu altura (cm)'))
credito =int(input('cuantos creditos tienes'))

if altura >=137 and creditos >=10:
    print('disfruta tu viaje')


elif altura < 137 and creditos >=10:
    print('no tienes la altura suficiente para subir ')

elif credito < 10 and altura >=137:
    print('no tienes suficinte credito')

else:
    print('no tines la altura ni el credito')