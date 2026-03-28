#INTRODUCTION
print("Hello! I am your friendly chatbot.")

#QUESTION 1- NAME
name = input("What is your name?")
print(f"Nice to meet you, {name}!\n")

#QUESTION 2 - FEELING
feeling = input("How are you feeling today?")
if "good" in feeling.lower() or "great" in feeling.lower():
  print("\n I'm glad to hear that! \n")
else:
  print("\n I hope that your day gets better! \n")

#QUESTION 3 - HOBBY
hobby = input("What is your favorite hobby ?")
print(f"\n Wow, {hobby} sounds fun! \n")
