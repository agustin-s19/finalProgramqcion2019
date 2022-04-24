Desaprobaste = False

{"Si": 1, "No" : 2}
while True:
    IniciarJuego=(input("¿Desea empezar a jugar?Si/No): "))
    if IniciarJuego.capitalize() not in ["Si", "No"]:
        print ("Has ingresado un comando inválido.Intente nuevamente")
    else:
        break

if IniciarJuego.capitalize() == "No":
    print ("Te perdiste de alto juego.Hasta pronto")
    
if IniciarJuego.capitalize() == "Si":
    print("Iniciando juego")
    print( )
    opciones1 =  {"A" : "Me quedo estudiando", "B" : "Salgo con mis amigos", "C" : "Me quedo mirando Netflix", "D" : "Me voy a dormir"}
    print("El lunes rendis un examen muy importante,es sabado y tus amigos te invitan a salir." )
    print("¿Que haces?")
    print( )
    for opcion in opciones1:
        print(opcion,"-", opciones1[opcion])
        
    while True:
        print( )
        pregunta1 =input("elijo: ")
        if pregunta1.capitalize() not in ["A","B","C","D"]:
            print( )
            print ("Has ingresado un comando inválido.Intente nuevamente")
            print("El lunes rendis un examen muy importante,es sabado y tus amigos te invitan a salir ¿Que haces?")
            print( )
            for opcion in opciones1:
                print(opcion,"-", opciones1[opcion])
        else:
            break   

    if pregunta1.capitalize() == "A":
        print()
        print("Te quedaste dormido de tanto estudiar")
        opciones2 = {"A" : "Te juntas con alguien a tomar mates", "B" : "Seguis estudiando", "C" : "Te pones a jugar Counter", "D" : "Invitas a alguien a ver Netflix"}
        print("A un dia del examen ¿Que haces?")
        print()
        for opcion in opciones2:
            print(opcion,"-", opciones2[opcion])
 
        while True:
            print( )
            pregunta2 =input("elijo: ")
            print ( )
            if pregunta2.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Te quedaste dormido de tanto estudiar")
                print("A un dia del examen ¿Que haces?")
                print( )
                for opcion in opciones2:
                    print(opcion,"-", opciones1[opcion])
            else:
                break   
        
        if pregunta2.capitalize() == "A":
            Desaprobaste = True
            print("Desaprobas el examen con una nota de 2,5")
            print("GAME OVER")

        elif pregunta2.capitalize() == "B":
            Desaprobaste = True
            print ("Te desvelaste estudiando, te dormiste y te perdiste el examen")
            print("GAME OVER")
        elif pregunta2.capitalize() == "C":
            Desaprobaste = True
            print("Perdiste la noción del tiempo, pasaron 3 dias")
            print("GAME OVER")
        else:
            Desaprobaste = True
            print("Desaprobaste el examen con una nota de 3,33 y dejaste embarazada a una ex-amiga")
            print("GAME OVER")
            
    elif pregunta1.capitalize() == "B":
        print( )
        print("La previa queda en la otra punta de la ciudad.")
        print("¿En que vas?")
        print( )
    else:
        Desaprobaste = True
        print("Desaprobaste el exámen y ya no tenes mas amigos")
        print("Game over")
    
    if(not Desaprobaste and pregunta1.capitalize() == "B"):

        opciones3 = {"A" : "Caminando", "B" : "Ecobici", "C" : "Uber", "D" : "Colectivo"}
    
        for opcion in opciones3:
            print(opcion,"-", opciones3[opcion])
            

        while True:
            print ( )
            pregunta3 =input("elijo: ")
            print( )
            if pregunta3.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("La previa queda en la otra punta de la ciudad.")
                print("¿En que vas?")
                print( )
                for opcion in opciones3:
                    print(opcion,"-", opciones3[opcion])
            else:
                break

        if pregunta3.capitalize() == "A":
            Desaprobaste = True
            print("Te mataron al asaltarte y ver que no tenias nada")
            print("GAME OVER")
        elif pregunta3.capitalize() == "B":
            Desaprobaste = True
            print("Llegando a la previa te atropella un camión y moris en el acto")
            print("GAME OVER")
        elif pregunta3.capitalize() == "C":
            print( )
            print("Llegaste a la previa")
            print("Te ofrecen para tomar,¿Que haces?")
            print ( )
        else:
            Desaprobaste = True
            print("Tiraron un piedrazo al colectivo que traspasó la ventana y te impacto en la cabeza, esto más el cristal te mató")
            print("GAME OVER")

    if(not Desaprobaste and pregunta3.capitalize() == "C"):
        opciones4 = {"A" : "Te negas y armas vos tu propio trago", "B" : "Jugas un juego de tragos", "C" : "Aceptas lo que te arman", "D" : "Aceptas lo que te arman, pero lo tiras sin que se den cuenta"}
        
        for opcion in opciones4:
            print(opcion,"-", opciones4[opcion])
            

        while True:
            print( )
            pregunta4 =input("elijo: ")
            print( )
            if pregunta4.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Llegaste a la previa")
                print("Te ofrecen para tomar,¿Que haces?")
                print( )
                for opcion in opciones4:
                    print(opcion,"-", opciones4[opcion])

            else:
                break

        if pregunta4.capitalize() == "A" :
            print( )
            print("Tomaste de más y te sentis mareado")
            print("¿Que haces?")
            print( )
        elif pregunta4.capitalize() == "D":
            print( )
            print("Tomaste de más y te sentis mareado")
            print("¿Que haces?")
            print( )
        else:
            Desaprobaste = True
            print("Terminaste vomitando y no llegaste ni al boliche ni a dar bien el examen")
            print("GAME OVER")

    if not Desaprobaste :
        opciones5 = {"A" : "Seguis tomando", "B" : "Te pones a tirar pasos de Fortnite", "C" : "Salis afuera a tomar aire", "D" : "Te dormis una siesta Pre-boliche"}
        for opcion in opciones5:
            print(opcion,"-", opciones5[opcion])

        while True:
            print( )
            pregunta5 =input("elijo: ")
            print( )
            if pregunta5.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Tomaste de más y te sentis mareado")
                print("¿Que haces?")
                print( )
                for opcion in opciones5:
                    print(opcion,"-", opciones5[opcion])

            else:
                break

        if pregunta5.capitalize() == "A" :
            Desaprobaste = True
            print("Te moris de un coma alcoholico.")
            print("GAME OVER")
        elif pregunta5.capitalize() == "B" :
            Desaprobaste = True
            print("Perdes la poca dignidad que tenias, tras vomitar bailando(mal)")
            print("GAME OVER")
        elif pregunta5.capitalize() == "C" :
            print("Ya te sentis mejor.Piden el Uber para ir al boliche.")
            print("20 minutos despues...")
            print("El Uber llegó y no los quiere llevar por que son 5.")
            print("¿Que haces?")
            print( )
        else:
            Desaprobaste = True
            print("Te despertas el martes, sin recordar nada.")
            print("GAME OVER")
            
    if(not Desaprobaste and pregunta5.capitalize() == "C"):
        opciones6 = {"A" : "Insistis agresivamente para que vayan los 5", "B" : "Le convidas del viajero para que vayan los 5", "C" : "Le pinchas las ruedas por gato", "D" : "Insistis diciendo que queda lejos y no van a dejar a ningun amigo atras"}
        for opcion in opciones6:
            print(opcion,"-", opciones6[opcion])
        while True:
            print( )
            pregunta6 =input("elijo: ")
            print( )
            if pregunta6.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Ya te sentis mejor.Piden el Uber para ir al boliche.")
                print("20 minutos despues...")
                print("El Uber llegó y no los quiere llevar por que son 5.")
                print("¿Que haces?")
                print( )
                for opcion in opciones6:
                    print(opcion,"-", opciones6[opcion])

            else:
                break  

        if pregunta6.capitalize() == "A" :
            Desaprobaste = True
            print("No llega ninguno al boliche, reprobas el examen y recibis una denuncia.")
            print("GAME OVER")
        elif pregunta6.capitalize() == "B" :
            Desaprobaste = True
            print("El chofer acepta llevarlos.")
            print("Se cruza con Chano en el camino y chocan a las 6 cuadras.")
            print("GAME OVER")
        elif pregunta6.capitalize() == "C" :
            Desaprobaste = True
            print("El conductor te sale a correr con un palo de fierro.")
            print("Ninguno llega al boliche,todavia tenes las marcas de los golpes que te dieron y reprobaste el examen.")
            print("GAME OVER")   
        else:
            print("El conductor acepta llevarlos.")
            print("Llegaron al boliche, este es para mayores de edad (vos sos menor)")
            print("¿Que haces?")
            print( )

    if(not Desaprobaste and pregunta6.capitalize() == "D"):
        opciones7 = {"A" : "Le pedis a una chica que pase con vos del brazo", "B" : "Pedis un DNI falso", "C" : "Pasas en patota con tus amigos, vos en el centro", "D" : "Le pedis al dueño del boliche que te haga pasar"}
        for opcion in opciones7:
            print(opcion,"-", opciones7[opcion])

        while True:
            print( )
            pregunta7 =input("elijo: ")
            print( )
            if pregunta7.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("El conductor acepta llevarlos.")
                print("Llegaron al boliche, este es para mayores de edad (vos sos menor)")
                print("¿Que haces?")
                print( )
                for opcion in opciones7:
                    print(opcion,"-", opciones7[opcion])
            else:
                break
        
        if pregunta7.capitalize() == "A" :
            Desaprobaste = True
            print("Rebotas, te va mal en el examen y salis escrachado en Redes Sociales.")
            print("GAME OVER")
        elif pregunta7.capitalize() == "B" : 
            Desaprobaste = True
            print ("Rebotaste como los mejores Jefferson Gutierritos")
            print ("GAME OVER" )
        elif pregunta7.capitalize() == "C" :
            Desaprobaste = True
            print ("Pasa la mitad de la patota y la demas se queda afuera")
            print ("Te descubren, no pasas y  desaprobas el examen" ) 
        else:
            print("Entras al Boliche.")
            print("Te cruzas al Profesor que te va a tomar el examen.")
            print("¿Que haces?")
            print( )
        
    if(not Desaprobaste and pregunta7.capitalize() == "D"):
        opciones8 = {"A" : "Seguis de largo como si no lo hubieras visto", "B" : "Lo saludas y te vas", "C" : "Le preguntas como va a ser el examen", "D" : "Lo intentas sobornar con un trago para que te apruebe"}
        for opcion in opciones8:
            print(opcion,"-", opciones8[opcion])
        
        while True:
            print( )
            pregunta8 =input("elijo: ")
            print( )
            if pregunta8.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Entras al Boliche.")
                print("Te cruzas al Profesor que te va a tomar el examen.")
                print("¿Que haces?")
                print( )
                for opcion in opciones8:
                    print(opcion,"-", opciones8[opcion])
            else:
                break
        
        if pregunta8.capitalize() == "A" :
            Desaprobaste = True
            print("El Profesor te toma bronca por no saludarlo y te reprueba en el examen.")
            print("GAME OVER")
        elif pregunta8.capitalize() == "B" :
            print("El Profesor te saluda")
            print("(Cambia tu imagen hacia el Profe, ahora te tiene como que sos copado y seguro)")
            print( )
        elif pregunta8.capitalize() == "C" :
            Desaprobaste = True
            print("El Profesor te toma bronca por hacerlo pensar en el trabajo")
            print("y arruinarle la noche")
            print("Te desaprueba")
            print("GAME OVER")
        else:
            Desaprobaste = True
            print("Lo sobornas pero despues te reprueba por intentar sobornarlo")
            print("GAME OVER")

    if(not Desaprobaste and pregunta8.capitalize() == "B"):
        opciones9 = {"A" : "Segundeo como un campeon a mi amiga", "B" : "Me voy corriendo al baño", "C" : "Pierdo una amiga, que me disculpe", "D" : "Digo que tengo novia"}
        print("Más tarde...")
        print("Una amiga se encuentra a un chico que le encanta, pero este solo acepta estar con ella si vos estas con su amiga.")
        print("¿Que haces?")
        print("Pd: la chica no te parece linda")
        print( )
        for opcion in opciones9:
            print(opcion,"-", opciones9[opcion])


        while True:
            print( )
            pregunta9 =input("elijo: ")
            print( )
            if pregunta9.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Una amiga se encuentra a un chico que le encanta, pero este solo acepta estar con ella si vos estas con su amiga.")
                print("¿Que haces?")
                print("Pd: la chica no te parece linda")
                print( )
                for opcion in opciones9:
                    print(opcion,"-", opciones9[opcion])
            else:
                break
        
        if pregunta9.capitalize() == "A" :
            print("Tu amiga esta con el chico de sus sueños y la chica te invita a irte con ella a su casa.")
            print("¿Que haces?")
            print( )
        elif pregunta9.capitalize() == "D":
            Desaprobaste = True
            print("Tu amiga revela que sos un virgen que nunca tuvo novia.")
            print("El Bullyng de la sociedad te consumio,no podes salir mas a la calle y dejaste la carrera.")
            print("GAME OVER")
        else:
            Desaprobaste = True
            print ("Tu amiga te odia y quedas como un fracasado")
            print("Desaprobas el examen con una nota de 3,33")
            print("GAME OVER")
    if(not Desaprobaste and pregunta9.capitalize() == "A"):
        opciones10 = { "A" : "Aceptas y vas con ella", "B" : "Te negas a ir con ella", "C" : "Le decis que tenes cosas mas importantes para hacer mencionando el examen", "D" : "Le decis que justo atropellaron a tu perro"}
        for opcion in opciones10:
            print(opcion,"-", opciones10[opcion])
        while True:
            print( )
            pregunta10 =input("elijo: ")
            
            print( )
            if pregunta10.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Tu amiga esta con el chico de sus sueños y la chica te invita a irte con ella a su casa.")
                print("¿Que haces?")
                print( )
                for opcion in opciones10:
                    print(opcion,"-", opciones10[opcion])
            else:
                break
        
        if pregunta10.capitalize() == "A" :
            print("Llegas a la casa de la chica y te enteras que ella es profesora de la materia que tenes que rendir el lunes")
            print("¿Que haces?")
            print( )
        elif pregunta10.capitalize() == "B":
            Desaprobaste = True
            print("La chica se enoja con vos, empieza a decir que sos un abusador")
            print("Vas a la carcel con condena de 16 años")
            print("16 años despues...")
            print("Salis de la carcel, feliz diciendo que ya nos sos virgen")
            print("GAME OVER")
        elif  pregunta10.capitalize() == "C":
            print("Ella te dice que ya curso esa materia ")
            print("¿Que haces?")
            print( )
        else:
            Desaprobaste = True
            print("No vas a la casa de ella, te tomas un Uber hasta tu casa")
            print("Y descubris que encerio atropeyaron a tu perro")
            print("El causante del accidente fue tu conductor de Uber")
            print("Que es nada mas ni menos que CHANO!")
            print("Por cierto entras en depresion y no te presentas al examen")
            print("GAME OVER")
        
    if(not Desaprobaste and pregunta10.capitalize() == "A"):     #PreguntaFinal1
        opciones11 = {"A" : "Le pedis que te ayude a estudiar para el examen", "B" : "Le decis de ir a ver Netflix", "C" : "Le decis que tenes ganas de dormir", "D" : "LLamas a tus amigos diciendoles que ahi es el After" }
        for opcion in opciones11:
            print(opcion,"-", opciones11[opcion])
        while True:
            print( )
            pregunta11 =input("elijo: ")
            print( )
            if pregunta11.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Llegas a la casa de la chica y te enteras que ella ya habia cursado la materia que tenes que rendir el lunes")
                print("¿Que haces?") 
                print( )
                for opcion in opciones11:
                    print(opcion,"-", opciones11[opcion])
            else:
                break
        if pregunta11.capitalize() == "A":
            print("La chica acepta ayudarte.")
            print( )
        elif pregunta11.capitalize() == "B":
            Desaprobaste = True
            print("Embarazas sin querer a la chica")
            print("Desaprobas el examen con una nota de 1")
            print("GAME OVER")
        elif pregunta11.capitalize() == "C":
            Desaprobaste = True
            print("La chica te echa de su casa y te tilda de virgo")
            print("Desaprobas el examen con una naota de 3,66")
            print("GAME OVER")
        else:
            Desaprobaste = True
            print("La chica va a la carcel por mandarse un After de la escala de Proyecto X.")
            print("Los padres presentan cargos contra vos y te condenan a 5 años de prision.")
            print("5 años despues...")
            print("Salis de la carcel, feliz diciendo que ya nos sos virgen.")
            print("GAME OVER")

        if (not Desaprobaste and pregunta11.capitalize() == "A"):
            print("Terminas aprobando el examen con un 7")
            print("Felicitaciones!!!" )
            print("Lograste aprobar la materia")
            print("Ganaste")

    if(not Desaprobaste and pregunta10.capitalize() == "C"):    #PreguntaFinal2
        opciones12 = {"A" : "Le pedis que te ayude a estudiar para el examen", "B" : "Te pones a bailar con ella", "C" : "Te vas a tu casa", "D" : "Se la presentas a tu profesor que te va a tomar el examen" }
        for opcion in opciones12:
            print(opcion,"-", opciones12[opcion])
        while True:
            print( )
            pregunta12 =input("elijo: ")
            print( )
            if pregunta12.capitalize() not in ["A","B","C","D"]:
                print( )
                print ("Has ingresado un comando inválido.Intente nuevamente")
                print("Ella te dice que ya curso esa materia ")
                print("¿Que haces?") 
                print( )
                for opcion in opciones12:
                    print(opcion,"-", opciones12[opcion])
            else:
                break
        
        if pregunta12.capitalize() == "A":
            print("La chica acepta ayudarte")
        elif pregunta12.capitalize() == "B":
            Desaprobaste = True
            print("Te filman y te haces viral")
            print("El baile de la anguila te empiezan a llamar")
            print("Desaprobas el examen debido a la angustia generada por esos comentarios")
            print("GAME OVER")
        elif pregunta12.capitalize() == "C": 
            Desaprobaste = True
            print("LLega el dia del examen y no te acordas nada")
            print("Te sacas un 2")
            print("GAME OVER")
        else:
            Desaprobaste = True
            print("Tu Profesor encara como un campeon hasta que se entera que es menor")
            print("Lo denuncias por abuso infantil")
            print("Va a la carcel con una condena de 25 años")
            print("Se pospone el examen")
            print("2 semanas despues rendis el examen")
            print("Te sacas un 3")
            print("(Casi te salis con la tuya)")
            print("GAME OVER")
        
        if (not Desaprobaste and pregunta12.capitalize() == "A"):  #FinalBueno2 
            print("Van a tu casa con la chica y te explica todo")
            print ("Terminas aprobando el examen con un 10")
            print("Felicitaciones!!!" )
            print("Lograste aprobar la materia")
            print ("Ganaste")
