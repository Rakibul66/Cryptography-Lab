plaintext=input("Enter Text:")
alphabet="abcdefghijklmnopqrstuvwxyz"
key=3
cipher=''
for c in plaintext:
    if c in alphabet:
     cipher+=alphabet[(alphabet.index(c)+key)%len(alphabet)]
     print("Encrypted message:"+cipher)