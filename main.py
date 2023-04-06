import random
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize empty lists for X (player guesses) and y (whether guess was correct)
X = []
y = []

# Play the game
while True:
    guess = int(input("Γράψε έναν αριθμό από το 1 εώς το 100: "))

    X.append(guess)
    if guess < number:
        y.append(0)
        print("Πολύ χαμηλός!")
    elif guess > number:
        y.append(1)
        print("Πολύ μεγάλος!")
    else:
        y.append(2)
        print("Κέρδισες!")
        break

# Train a linear regression model on the player's guesses and feedback
model = LinearRegression()
model.fit(np.array(X).reshape(-1, 1), y)

# Predict the correct number based on the player's guesses
pred = int(model.predict([[number]])[0])
if pred == 0:
    print("Το νούμερο είναι πιο μεγάλο από", guess)
elif pred == 1:
    print("Το νούμερο είναι πιο μεγάλο από", guess)
else:
    print("Κέρδισες!")
