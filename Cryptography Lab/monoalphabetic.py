
import string
plaintext="thequickbrownfoxJumpover"
key="zebraistpdcfghjklmnoquvwxy"
cipher=""
for c in plaintext:
    if c in string.ascii_lowercase:
        index=(ord(c)-ord('a'))
        cipher=cipher+key[index]
    else:
        cipher=cipher+c
        print("plain:"+plaintext)
        print("cipher:"+cipher)