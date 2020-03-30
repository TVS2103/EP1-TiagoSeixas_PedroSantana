from random import randint
fichas = 100
programa = True
while fichas > 0 and programa == True:
    programa2 = True
    pergunta = input("Vai apostar ou sair? ")
    if pergunta != "sair":
        fase = "Come Out"
        print (fase)
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        Pass_Line_Bet = int(input("Aposta quanto na Pass Pine Bet? "))
        Field = int(input("Aposta quanto na Field? "))
        Any_Craps = int(input("Aposta quanto na Any Craps? "))
        Twelve = int(input("Aposta quanto na Twelve? "))
        if Pass_Line_Bet>0 and Field>=0 and Any_Craps>=0 and Twelve>=0:
            if dado1 + dado2 == 2:
                fichas -= Pass_Line_Bet
                fichas += Field*2
                fichas += Any_Craps*7
                fichas -= Twelve
            elif dado1 + dado2 == 3:
                fichas -= Pass_Line_Bet
                fichas += Field
                fichas += Any_Craps*7
                fichas -= Twelve
            elif dado1 + dado2 == 4:
                fichas += Field
                fichas -= Any_Craps
                fichas -= Twelve
                Point = dado1+dado2
                fase = "Point"
                print (fase)
                while programa2==True:
                    dado1 = randint(1,6)
                    dado2 = randint(1,6)
                    Field = int(input("Aposta quanto na Field? "))
                    Any_Craps = int(input("Aposta quanto na Any Craps? "))
                    Twelve = int(input("Aposta quanto na Twelve? "))
                    if dado1 + dado2 == 2:
                        fichas += Field*2
                        fichas += Any_Craps*7
                        fichas -= Twelve
                    elif dado1 + dado2 == 3:
                        fichas += Field
                        fichas += Any_Craps*7
                        fichas -= Twelve
                    elif dado1 + dado2 == 4:
                        fichas += Pass_Line_Bet
                        fichas += Field
                        fichas -= Any_Craps
                        fichas -= Twelve
                        programa2 = False
                    elif dado1+dado2 == 5 or 6 or 8:
                        fichas -= Field
                        fichas -= Any_Craps
                        fichas -= Twelve
                    elif dado1+dado2 == 7:
                        fichas -= Pass_Line_Bet
                        fichas -= Field
                        fichas -= Any_Craps
                        fichas -= Twelve
                        programa2 = False
                    elif dado1 + dado2 == 9 or 10:
                        fichas += Field
                        fichas -= Any_Craps
                        fichas -= Twelve
                    elif dado1 + dado2 == 11:
                        fichas += Field
                        fichas -= Any_Craps
                        fichas -= Twelve
                    elif dado1 + dado2 == 12:
                        fichas += Field*3
                        fichas += Any_Craps*7
                        fichas += Twelve*30
            elif dado1+dado2 == 5 or 6 or 8:
                fichas -= Field
                fichas -= Any_Craps
                fichas -= Twelve
                Point = dado1+dado2
                fase = "Point"
                print (fase)
                
            elif dado1+dado2 == 7:
                fichas += Pass_Line_Bet
                fichas -= Field
                fichas -= Any_Craps
                fichas -= Twelve

            elif dado1 + dado2 == 11:
                fichas += Pass_Line_Bet
                fichas += Field
                fichas -= Any_Craps
                fichas -= Twelve
            elif dado1 + dado2 == 12:
                fichas -= Pass_Line_Bet
                fichas += Field*3
                fichas += Any_Craps*7
                fichas += Twelve*30
        elif Pass_Line_Bet == 0 and Field>=0 and Any_Craps>=0 and Twelve>=0:
            if dado1 + dado2 == 2:
                fichas += Field*2
                fichas += Any_Craps*7
                fichas -= Twelve
            elif dado1 + dado2 == 3:
                fichas += Field
                fichas += Any_Craps*7
                fichas -= Twelve
            elif dado1 + dado2 == 4:
                fichas += Field
                fichas -= Any_Craps
                fichas -= Twelve
            elif dado1+dado2 == 5 or 6 or 7 or 8:
                fichas -= Field
                fichas -= Any_Craps
                fichas -= Twelve
            elif dado1 + dado2 == 9 or 10 or 11:
                fichas += Field
                fichas -= Any_Craps
                fichas -= Twelve
            elif dado1 + dado2 == 12:
                fichas += Field*3
                fichas += Any_Craps*7
                fichas += Twelve*30
        else:
            print ("Você digitou uma das apostas como sendo um valor negativo, tente novamente")
    else:
        print ("Obrigado por jogar")
        programa = False
