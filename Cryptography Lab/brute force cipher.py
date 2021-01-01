

alphabet = "abcdefghijklmnopqrstuvwxyz"
enc_str=input("Enter Text:")

x = 0          #index starting
while x < 26:
    x = x + 1   #position increment
   # stringtodecrypt
    decrypt = enc_str

    decrypt = decrypt.lower()
    ciphershift = int(x)
    decrypted = ""
    for character in decrypt:
        position = alphabet.find(character)
        newposition = position - ciphershift   #dec formula here
        if character in alphabet:
            decrypted = decrypted + alphabet[newposition]
        else:
            decrypted = decrypted + character

    ciphershift = str(ciphershift)
    print("cipher shift of " + ciphershift)
    print("decrypted message:")
    print(decrypted)
    print("\n")



