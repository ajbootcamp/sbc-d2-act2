from random import randint

choose1 = "Kulob!"
choose2 = "Hayang!"
c2 = randint(1,2)
c3 = randint(1,2) 

p1 = (input("Kulob/Hayang:"))
print("Player 1:", p1)

if c2 == 1:
    c2 = "Kulob!"
    print("Com2: Kulob!")
else:
    c2 = "Hayang!"
    print("Com2: Hayang!")

if c3 == 1:
    c3 = "Kulob!"
    print("Com3: Kulob!")
else:
    c3 = "Hayang"
    print("Com3: Hayang!")

if (p1 == "Kulob!" and c2 == "Hayang!" and c3 == "Hayang!") or (p1 == "Hayang!" and c2 == "Kulob!" and c3 == "Kulob!"):
    print("Player 1 Win!")

elif (p1 == "Hayang!" and c2 == "Kulob!" and c3 == "Hayang!") or (p1 == "Kulob!" and c2 == "Hayang!" and c3 == "Kulob!"):
    print("Computer 2 Win!")

elif (p1 == "Hayang!" and c2 == "Hayang!" and c3 == "Kulob!") or (p1 == "Kulob!" and c2 == "Kulob!" and c3 == "Hayang!"):
    print("Computer 3 Win!")

else:
    print("No one wins!")