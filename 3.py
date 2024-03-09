# Pedir al usuario que ingrese la distancia en metros
metros = float(input("Ingrese la distancia en metros: "))

# Realizar la conversión de metros a millas (1 metro = 0.000621371 millas)
millas = metros * 0.000621371

print(f"{metros} metros equivalen a {millas} millas")
