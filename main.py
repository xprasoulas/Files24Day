# TODO: Create a letter using starting_letter.txt
def get_letter():
    with open("./Input/Letters/starting_letter.txt") as my_letter:
        return my_letter.read()


# for each name in invited_names.txt
def get_names():
    with open("./Input/Names/invited_names.txt") as int_names:
        return int_names.readlines()


# Replace the [name] placeholder with the actual name.
for name in get_names():
    new_name = name.strip("\n")
    new_letter = get_letter().replace("[name]", new_name)
    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/{new_name}.txt", mode="w") as file:
        file.write(f"{new_letter}")

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
