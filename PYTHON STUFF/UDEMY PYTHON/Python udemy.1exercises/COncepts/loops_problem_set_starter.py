
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
   print (char)

# Write a while loop that does the same thing!
count=0
while count<len(word):
    print(word[count])
    count+=1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
count=100
while count <140:
   count+=2
   print(count)




# Write a for loop that does the same thing (with range())
for num in range (100,142,2):
   print(num)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
user=input("Enter passphrase sillygoose ")
while user!="sillygoose":
    user=input("passphrase incorrect.Input sillygoose ")
print("passphrase accepted")   