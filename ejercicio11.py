cantidad=int(input("ingrese cuanto desea invertir"))
interes=int(input("ingrse cuanto interes anual desea recibir"))
años=int(input("durante cuantos años desea invertir"))
anual=cantidad/100*interes
print("en"+ str(años)+ " vas a ganar: ")
print(anual*años)