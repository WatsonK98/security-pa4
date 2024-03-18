import string

#for simplicity just use ascii encoding in lowercase
alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

#ask for key
key = int(input("Enter key: "))

#encrypted message set to lowercase
encrypted_message = "Tvsxigx csyv hexe amxl gevi erh geyxmsr. Epaecw ywi wxvsrk erh yrmuyi tewwasvhw jsv iegl eggsyrx, vikypevpc ythexi, erh oiit csyv hizmgiw erh wsjxaevi yt xs hexi".lower()
#set for the decrypted characters
decrypted_message = ""

#loop to go through each letter in the cipher
for i in encrypted_message:

    #check each character against the alphabet
    if i in alphabet:
        #find the position of the cipher character in terms of the ascii alphabet
        position = alphabet.find(i)
        #move the position in comparison with the key
        new_pos = (position - key) % 26
        #the new character is the new position within the ascii alphabet
        new_char = alphabet[new_pos]
        #add the attempted decryption to the decrypted message
        decrypted_message += new_char
    else:
        #if character is not in the alphabet then add to message anyway
        decrypted_message += i

#...print the decrypted message
print("message: ", decrypted_message)