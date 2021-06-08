output_path = "../Mail Merge Project/Output/ReadyToSend/"

with open("../Mail Merge Project/Input/Names/invited_names.txt") as guests:
    names = guests.readlines()
with open("../Mail Merge Project/Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        f_name = name.strip()
        new_letter = letter.replace("[name]", f_name)
        with open(output_path+f"letter{f_name}.txt", "w") as final_letter:
            final_letter.write(new_letter)
