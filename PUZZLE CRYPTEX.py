#The puzzle cryptex
#Code 1 = 1-196-361-529-25-324 225-196-25

print("\nWelcome to a practice game to see if you are a dickhead. " + 
      "\n\nYou will have to solve 5 problems or else see a true mirror " + 
      "of yourself. You can try each question as many times as you need.")

#the dickhead
dickhead = (
    "    __________"
    "\n   /          \ "
    " \n  |            \_________"
    "\n /      \__    __________) "
    "\n|        @    (_)_)"
    "\n \       -     | "
    "\n  |            \ "
    "\n  |           ,_\ "
    "\n  |      / ___| "
    "\n  |      \'   _) "
    "\n  |          /  "
    "\n  |      \__/   "
    "\n   \______/     ")

#The winner
winner = (
    "\t  ________ "
  "\n\t/          \ "
 "\n       / _--_  _--_ \ "
"\n      |  \_O    O_/  | "
"\n      |    --  --    | " 
"\n      |      ||      | "
"\n      |     (..)     | "
 "\n       \  (------,  / "
  "\n        \  \____/  / "
   "\n         \        / "
    "\n          \______/ " )



#PROBLEM 1
print("\n\t\t\t\tPROBLEM ONE")

userinput = ""
while (userinput !="Answer One"):
  userinput = input("\nCode " + "=" + " 1-196-361-529-25-324 225-196-25: ").title()

  if userinput == "Answer One":
    print("Correct")
  else:
    print(dickhead)

#PROBLEM 2
print("\t\t\t\tPROBLEM TWO")
print("\nHomophones".upper() + "\n\nWhere were the two brothers during the day? " + 
      "\nOne was delivering mail to his male friend while the other had " + 
      "\nflown to Florence with the flu for a holiday by himself.")

userinput = ""
while (userinput !="Male" and userinput !="Mail"):
  userinput = input("\nChoose a word from the text that "
                    "has a homophone within the same text: ").title()

  if userinput == "Mail":
    print("Correct")
  elif userinput == "Male":
    print ("Correct")
  else:
    print(dickhead)

userinput = ""
while (userinput !="Male" and userinput !="Mail"):
  userinput = input("\nWrite the homophone of your first word: ").title()

  if userinput == "Mail":
    print("Correct")
  elif userinput == "Male":
    print ("Correct")
  else:
    print(dickhead)

#PROBLEM 3
print("\n\t\t\t\tPROBLEM THREE\n")

words = ["cat", "dog", "fish", "cow", "car", "elk"]

print(words)

odd_word = ""
while (odd_word !="Fish"):
  odd_word = str(input("\nWhich word is the odd one out: ")).title()

  if odd_word == "Fish":
    print("\nCorrect! It is the only word with four letters!")
  else:
    print(dickhead)

#PROBLEM 4

print("\n\t\t\t\tPROBLEM FOUR\n")

jumble = ("\t     R"
       "\n\t  I     S"
     "\n\tS         C"
     "\n\tS         M"
       "\n\t  A     N"
          "\n\t     I")

print(jumble)

jumble_solve = ""
while (jumble_solve !="Narcissism"):
  jumble_solve = str(input("\nWhat word does this jumble spell: ")).title()

  if jumble_solve == "Narcissism":
    print("Well done, you're not as stupid as you look, nor as beautiful as me")
  else:
    print(dickhead)

#PROBLEM 5

print("\n\t\t\t\tPROBLEM FIVE")
    
your_name = str(input("\nThis last one is an easy one, " +
                       "but you only get one try. Just type in your name: ")).title()

correcto = "Your Name"
if your_name == correcto:
    print("\n" + str(winner) + "\n\tSlow clap")
else:
    print("\n\tStart all over again" + str(dickhead))






