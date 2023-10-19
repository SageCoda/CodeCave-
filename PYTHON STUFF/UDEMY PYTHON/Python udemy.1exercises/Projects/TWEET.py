# tweet=input('Enter your Tweet:')
# max_tweet=40
# if len(tweet) <= max_tweet :
#     print(f'That {len(tweet)} char tweet will work! ')
# elif len(tweet) > max_tweet :
#     print(f'Your {len(tweet)} char tweet is {len(tweet)-max_tweet} char(s) too long')   

word="elephantt"

empty=[]
for _ in range(len(word)):
    empty+='_'
print (empty )


guess = input("Guess letter ").lower()

for position in range(len(word)):
    letter= word[position]
    if letter == guess:
        empty[position]= letter
print(empty)
        
  