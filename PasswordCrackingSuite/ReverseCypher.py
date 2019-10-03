# Reverse Cipher
message = input("Enter in Text To Cypher: ")
translated = ""

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)