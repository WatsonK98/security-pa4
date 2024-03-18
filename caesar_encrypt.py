import string

alphabet = string.ascii_lowercase

key = 7

plain_text = "Programming is like cooking. Even if you follow the recipe perfectly, there's always a chance you'll end up with a big mess.".lower()

encrypted_message = ""

for i in plain_text:

    if i in alphabet:
        #get the position of the letter in the alphabet
        position = alphabet.find(i)
        #create a new position from the key
        new_pos = (position + key) % 26
        #get the letter from the new position
        new_char = alphabet[new_pos]
        #concatenate the letter into the string
        encrypted_message += new_char
    
    else:
        #if it's not a letter then just add to the encrypted string
        encrypted_message += i

print("encrypted message: ", encrypted_message)