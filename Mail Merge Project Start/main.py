PLACEHOLDER = "[name]"


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as name_list:
    name_list = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

    for name in name_list:
        name = name.strip()
        if " " in name:
            file_name = name.replace(" ", "_").lower()
        else:
            file_name = name.lower()
        with open(f"./Output/ReadyToSend/letter-to-{file_name}.txt", mode="w") as mail_merged:
            mail_merged.write(letter.replace(PLACEHOLDER, name))


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp