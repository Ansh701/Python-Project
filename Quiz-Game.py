print("Welcome to My Quiz Game!")
playing = input("Do you want to play? Yes/No: ").title()

if playing != "Yes":
    quit()

print("Okay! Let's Play 🎮")
score = 0

# Question 1
answer = input("What is the capital of India? ").title()
if answer == "New Delhi":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 2
answer = input("What does CPU stand for? ").title()
if answer == "Central Processing Unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 3
answer = input("What is the chemical symbol for water? ").upper()
if answer == "H2O":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 4
answer = input("Who wrote 'Romeo and Juliet'? ").title()
if answer == "William Shakespeare":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 5
answer = input("What planet is known as the Red Planet? ").title()
if answer == "Mars":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 6
answer = input("What is the largest mammal? ").title()
if answer == "Blue Whale":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 7
answer = input("Which language is used to create Android apps? ").title()
if answer == "Java":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 8
answer = input("What is the boiling point of water in Celsius? ").strip()
if answer == "100":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 9
answer = input("Which organ pumps blood through the body? ").title()
if answer == "Heart":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 10
answer = input("What is the currency of Japan? ").title()
if answer == "Yen":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Final Score
print(f"\nYou got {score}/10 questions correct!")
if score >= 7:
    print("Great job! 🎉")
else:
    print("Keep practicing! 💪")
