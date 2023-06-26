
answer = input('Welcome to Fable Quest adventure game. Would you like to play? (yes/no)')

if answer.lower().strip() == 'yes':

    answer = input('Noble choice! What is your name hero? ')
    if answer == "Nathan":
        print('Long ago in the land of Albion a hero once held in high honor \
desired more power and was drawn to the dark side. \
This fallen hero known as Arbitar went to Forbidden Mountain \
and removed the Sword of the Ancients by defeating the order known as The Guardians. \
Through Arbitars actions he released the creatures of havoc in the forms of orcs and trolls. \
Now you hero must defeat Arbitars army of bandits, orcs and trolls and restore the Sword of Ancients back to its rightful place. \
Choose your path wisely hero. type "continue"')

else:
    print('Not everyone has what it takes to be a hero, bye for now!')