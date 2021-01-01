plaintext=input("Enter Text:")
alphabet="abcdefghijklmnopqrstuvwxyz"
key=3
cipher=''
for c in plaintext:
    position=alphabet.find(c)
    newposition=(position-3)%26
    cipher+=alphabet[newposition]

print("dec message:"+cipher)