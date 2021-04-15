# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
import pandas

# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#  1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# new_dict = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
#
# print(new_dict)

#  2. Create a list of the phonetic code words from a word that the user inputs.

phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_letters = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}


def generate_phonetic_word():
    input_word = input("Enter a word: ").upper()
    try:
        new_word = [phonetic_letters[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only numbers in the alphabet")
    else:
        print(new_word)
    finally:
        generate_phonetic_word()


generate_phonetic_word()
