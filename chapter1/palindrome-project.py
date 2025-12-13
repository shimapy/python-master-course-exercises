# checking palindrome
def is_palindrome():
    text = input()
    rev = ''.join(reversed(text))

    if text == rev:
        return "The string is a palindrome."
    return "The string is not a palindrome."
# run the application
if __name__ == "__main__":
    print(is_palindrome())
