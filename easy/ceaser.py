def caesarCipherEncryptor(string, key):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    print(len(letters))
    s = ""
    for c in string:
        new_letter_idx = (letters.index(c) + key) % 26
        s = s + letters[new_letter_idx]
    return s

print(caesarCipherEncryptor("xza", 2))