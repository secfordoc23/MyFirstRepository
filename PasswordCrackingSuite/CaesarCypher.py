# Caesar Cypher
characters = "abcdefghijklmnopqrstuvwxyz1234567890"

message = input("Enter in Text To Cypher: ")
key = "100"
while not key.isdigit() and int(key) >= len(characters):
    key = input("Enter Key: ")

option = "0"
while not option.isdigit() and 0 < int(option) < 3:
    option = input("Enter 1 to Encrypt or 2 to Decrypt: ")

resultMessage = ""
for char in message:
    if char.lower() in characters:
        charIndex = characters.find(char.lower())
        if int(option) == 1:  # Encrypting
            shiftedIndex = charIndex + int(key)
        else:  # Decrypting
            shiftedIndex = charIndex - int(key)

        # Handle Character List wrap around
        if shiftedIndex >= len(characters):
            shiftedIndex = shiftedIndex = len(characters)
        elif shiftedIndex < 0:
            shiftedIndex = shiftedIndex + len(characters)
        resultMessage = resultMessage + characters[shiftedIndex]
    else:
        print("Unable to find character {} in character list".format(char))
        resultMessage = resultMessage + char

print("Message Result: \n{}".format(resultMessage))
