import random
import numpy as np
from sklearn.linear_model import LinearRegression

# Δημιουργήστε έναν τυχαίο αριθμό μεταξύ 1 και 100
number = random.randint(1, 100)

# Αρχικοποίηση κενών λιστών για X (μαντεύει ο παίκτης) και y (αν η εικασία ήταν σωστή)
X = []
y = []

# Play the game
while True:
    guess = int(input("Guess the number between 1 and 100: "))

    # Καταγράψτε την εικασία και εάν ήταν πολύ υψηλή ή πολύ χαμηλή
    X.append(guess)
    if guess < number:
        y.append(0)  # Guess was too low
        print("Πολύ χαμηλός!")
    elif guess > number:
        y.append(1)  # Guess was too high
        print("Πολύ υψηλός!")
    else:
        y.append(2)  # Guess was correct
        print("Κέρδισες!")
        break

    # Εκπαιδεύστε ένα μοντέλο γραμμικής παλινδρόμησης στις εικασίες και τα σχόλια του παίκτη
    model = LinearRegression()
    model.fit(np.array(X).reshape(-1, 1), y)

    # Προβλέψτε τον σωστό αριθμό με βάση τις εικασίες του παίκτη
    pred = int(model.predict([[number]])[0])
    if pred == 0:
        print("Ο αριθμός είναι μικρότερος από", guess)
    elif pred == 1:
        print("Ο αριθμός είναι μεγαλύτερος από", guess)
    else:
        print("Κέρδισες!")
        break
