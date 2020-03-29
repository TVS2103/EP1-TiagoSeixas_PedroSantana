from random import randint
fichas = 100
programa = True
while fichas > 0 and programa == True:
    pergunta = input("Vai apostar ou sair? ")
    if pergunta != "sair":
        print ("Come Out")
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        Pass_Line_Bet = int(input("Aposta quanto na Pass Pine Bet? "))
        Field = int(input("Aposta quanto na Field? "))
        Any_Craps = int(input("Aposta quanto na Any Craps? "))
        Twelve = int(input("Aposta quanto na Twelve? "))
        if Pass_Line_Bet>0 and Field>0 and Any_Craps>0 and Twelve>0:
