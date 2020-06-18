#midiccionario = {"Alemania": "Berlín", "Francia": "París", "México": "CDMX", "Reino Unido": "Londres", "Alan": 9}
#midiccionario ["Italia"] = "Lisboa"
#print(midiccionario)
#midiccionario["Italia"] = "Roma"
#print(midiccionario)
#del midiccionario ["México"]
#print(midiccionario)


##mitupla = ["España", "Francia", "Reino Unido", 78, 2]
##midicc={mitupla[0]: "Madrid", mitupla[1]: "Paris", mitupla[2]: "Londres", mitupla[3]: 67, mitupla[4]: 1 }
##print(midicc["Francia"])

###midicci={23:"Jordan", "nombre": "Michael", "equipo":"idk", "anillos":[1991, 1992, 1993, 1994]}
###print(midicci["anillos"][0])


midiccionarioconundiccionariodentro={23:"Jordan", "nombre": "Michael", "equipo":"idk", "anillos":{"temporadas": [1991, 1992, 1993, 1994]}}
print(midiccionarioconundiccionariodentro.keys())
print(midiccionarioconundiccionariodentro.values())
print(len(midiccionarioconundiccionariodentro))