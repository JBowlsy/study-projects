#Challenge 6 - code breakers
from collections import Counter

print("\nWelcome to the Code Breaker App\n")

no_letter_22 = ["'", "_", "-", ";", ":", ".", ",", "", "´", " ", "?", "!", "&", "1", "3", "4", "5", "6", "7", "8", "9", "0" "\n", "\t"]

key_phrase_1 = """There was only one catch and that was Catch-22, which specified that a concern for one's safety in the face of dangers that were real and immediate was the process of a rational mind. Orr was crazy and could be grounded. All he had to do was ask; and as soon as he did, he would no longer be crazy and would have to fly more missions. Orr would be crazy to fly more missions and sane if he didn't, but if he was sane he had to fly them. If he flew them he was crazy and didn't have to; but if he didn't want to he was sane and had to. Yossarian was moved very deeply by the absolutesimplicity of this clause of Catch-22 and let out a respectful whistle.""".lower()

#Remove spaces
for non_letter in no_letter_22:
    key_phrase_1 = key_phrase_1.replace(non_letter, "")

total_occurrences = len(key_phrase_1)

letter_count = Counter(key_phrase_1)


#sort alphabet
print("Frequency of letters in first excerpt")
print("\tletter" + "\t\tOccurrence" + "\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = round((value/total_occurrences)*100, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage))

#order letters from high to low occurrence
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for key in ordered_letter_count:
    key_phrase_1_ordered_letters.append(key[0])

#printing letters
print("\nLetters from highest to lowest occurence")
for letter in key_phrase_1_ordered_letters:
    print(letter, end="")


key_phrase_2 = """You're inches away from death every time you go on a mission. How much oldercan you be at your age? A half minute before that you were stepping into highschool, and an unhooked brassiere was as close as you ever hoped to get to Paradise. Only a fifth of a second before that you were a small kid with a ten-week summer vacation that lasted a hundred thousand years and still ended too soon. Zip! They go rocketing by so fast. How the hell else are you ever going to slow down?' Dunbar was almost angry when he finished.""".lower()

#Remove spaces and characters
for non_letter in no_letter_22:
    key_phrase_2 = key_phrase_2.replace(non_letter, "")

total_occurrences = len(key_phrase_2)

letter_count = Counter(key_phrase_2)

#sort alphabet
print("\n\nFrequency of letters in second excerpt")
print("\tletter" + "\t\tOccurrence" + "\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = round((value/total_occurrences)*100, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage))

#order letters from high to low occurrence
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for key in ordered_letter_count:
    key_phrase_2_ordered_letters.append(key[0])

#printing letters
print("\nLetters from highest to lowest occurence")
for letter in key_phrase_2_ordered_letters:
    print(letter, end="")

d_encode = input("\n\nWould you like to encode or decode a message: ").lower()


#Get user´s phrase to encode
user_en_phrase = input("What is the phrase: ").lower()

#remove non letters
for non_letter in no_letter_22:
    user_en_phrase = user_en_phrase.replace(non_letter, "")
print(user_en_phrase)

#encode phrase
if d_encode == "encode":
    encoded_phrase = []
    for letter in user_en_phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)

    print("\The encoded message is: ")
    for letter in encoded_phrase:
        print(letter, end="")
#decode phrase
elif d_encode == "decode":
    decoded_phrase = []
    for letter in user_en_phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter= key_phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)

    print("\nThe decoded message is: ")
    for letter in decoded_phrase:
        print(letter, end="")

#bad input from user
else:
    print("\nPlease type ´encode´ or ´decode´. Try again.")







