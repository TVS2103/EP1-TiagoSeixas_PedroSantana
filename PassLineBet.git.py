from random import randint
fichas = 100
programa = True
while fichas > 0 and programa == True:
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
        if Pass_Line_Bet>0 and Field>0 and Any_Craps>0 and Twelve>0
        if Pass_Line_Bet>0 and Field>0 and Any_Craps>0 and Twelve == 0
        if Pass_Line_Bet>0 and Field>0 and Any_Craps == 0 and Twelve>0
        if Pass_Line_Bet>0 and Field == 0 and Any_Craps>0 and Twelve>0
        if Pass_Line_Bet>0 and Field>0 and Any_Craps == 0 and Twelve == 0
        if Pass_Line_Bet>0 and Field == 0 and Any_Craps == 0 and Twelve > 0
        if Pass_Line_Bet>0 and Field == 0 and Any_Craps>0 and Twelve == 0
        if Pass_Line_Bet>0 and Field == 0 and Any_Craps == 0 and Twelve == 0
        if Pass_Line_Bet == 0 and Field>=0 and Any_Craps>=0 and Twelve>=0:
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
