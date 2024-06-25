import pandas as pd

# read csv containing morse characters.
data = pd.read_csv("morse.csv")
# Making a dictionary of morse/arabic char.
morse_char = {row.letter: row.morse for (index, row) in data.iterrows()}


def convert_to_morse():
    user_input = input("Type in text to be converted to morse code: ").upper()

    try:
        output = [morse_char[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters of the alphabet and numbers are supported. "
              "No special character support just yet. Try again.")
        convert_to_morse()
    else:
        print(output)


convert_to_morse()
