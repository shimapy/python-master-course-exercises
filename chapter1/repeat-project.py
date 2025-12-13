# Finding repeated letters
def finding_repeated_letters():
    try:
        statment = input()
        word_list = statment.split()
        letter_count = 0
        letter = ""
        for word in word_list:
            if letter_count < len(word):
                letter = word
                letter_count = len(word)
            elif letter_count == len(word):
                letter += " " +word
        print("Longest word(s):")
        print(f"{letter} ({letter_count} letters)")
    except Exception as e:
        print(f"Error: {e}")
# run the application
if __name__ == "__main__":
    finding_repeated_letters()
    