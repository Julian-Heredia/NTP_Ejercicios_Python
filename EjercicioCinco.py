Luz = 299792

Km_Marte = 227943824

Metros = Km_Marte * 1000

Segundos = round(Metros/Luz)

Resultado_Uno = round(Segundos/1000)

Resultado_Final = round(Resultado_Uno/65)

print("Los segundos que le toma a la luz del sol viajar a Marte son: " + str(Resultado_Final) + " segundos")