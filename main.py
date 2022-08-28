import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(df)

df_dict = {row.letter: row.code for index, row in df.iterrows()}


def start():
    name = input("Enter a name: ").upper().replace(" ", "")

    try:
        nato = [df_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        start()
    else:
        print(nato)


start()
