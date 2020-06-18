milista=[2,3,4,2,2,2,2,"Quetzi"]
mitupla=tuple(milista)
print(mitupla)
print(milista)
print(2 in mitupla)
print(mitupla.count(2))
print(mitupla.count("Quetzi"))
print(len(mitupla))

mituplauni=("Juan",)
print(len(mituplauni))
mituplarara="Alan", 23, 19.09,1
print(mituplarara)

nombre, dia, mes, agno = mituplarara
print(nombre)
print(dia)
print(agno)
print(mes)