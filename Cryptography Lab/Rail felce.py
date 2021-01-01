
#getting input s is for plain text mam and k is for key ,number of rows in grid
s=input("Enter string:")
k=int(input("Enter key:"))

#To create grid i use a blank list.NumPy arrays can be use here,
# To initialize the list, first fill the list with ‘ ‘(single space)
enc=[[" " for i in range(len(s))] for j in range(k)]
print(enc)

#variable to determine which row to add our character to and flag whether we should travel in an upward or a downward direction
flag=0
row=0
for i in range(len(s)):

  enc[row][i]=s[i]

  if row==0:
    flag=0   # If flag=0, then  need to continue in the downward

  elif row==k-1:   # the last row, the flag will be 1.
    flag=1  # travel in an upward direction.

  if flag==0:
    row+=1
  else:
    row-=1

# filled in our plaintext characters into our grid
    for i in range(k):
        print("".join(enc[i]))  #join() function which will convert  list to a string.


#convert  ct list to string
        ct = []
        for i in range(k):
            for j in range(len(s)):
                if enc[i][j] != ' ':
                    ct.append(enc[i][j])

                    cipher = "".join(ct)
                    print("Cipher Text: ", cipher) 

                    #Railfence by 171311066