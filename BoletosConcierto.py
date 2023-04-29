("boletosConcierto")
print("comprar boletos para un concierto")
print("comprar online")
online = input().upper()
if online == "SI":
    print("entrar a un sitio web para comprar los boletos")
else:
    print("ir a un centro comercial y comprar los boletos")
    comprar = input()
print("comprar los boletos mas caros")
boletoCaro = input().upper()
if boletoCaro == "SI":
    print("comprar la cantidad de boletos que quiero")
    cantidadBoleto = input()
else:
    print("comprar boletos economicos")
    boletoEconomico = input()
print("pagar con tajeta de credito o debito")
tarjeta = input().upper()
if tarjeta == "credito":
    print("elegir numero de cuotas y pagar")
    numCuotas = input()
else:
    print("digitar los datos y pagar")
    digDatos = input()
print("los boletos llegaron al correo")
correo = input().upper()
if correo == "NO":
    print("llamar a la empresa que vnedio los boletos y reclamar")
else:
    print("verificar datos")
    correoBoletos = input()