import random
import time

def hangmanz():
    hangman = (

    """
    _________
        |/        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
    _________
        |/   |      
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        H""",

    """
    _________       
        |/   |              
        |   (_)
        |                         
        |                       
        |                         
        |                          
        |___                       
        HA""",

    """
    ________               
        |/   |                   
        |   (_)                  
        |    |                     
        |    |                    
        |                           
        |                            
        |___                    
        HAN""",


    """
    _________             
        |/   |               
        |   (_)                   
        |   /|                     
        |    |                    
        |                        
        |                          
        |___                          
        HANG""",


    """
    _________              
        |/   |                     
        |   (_)                     
        |   /|\                    
        |    |                       
        |                             
        |                            
        |___                          
        HANGM""",



    """
    ________                   
        |/   |                         
        |   (_)                      
        |   /|\                             
        |    |                          
        |   /                            
        |                                  
        |___                              
        HANGMA""",


    """
    ________
        |/   |     
        |   (_)    
        |   /|\           
        |    |        
        |   / \        
        |               
        |___           
        HANGMAN""")
    hang=list(hangman)


    logo = ''' 
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/    '''
    def get_word():
        words = [
        'abruptly', 
        'absurd', 
        'abyss', 
        'affix', 
        'askew', 
        'avenue', 
        'awkward', 
        'axiom', 
        'azure', 
        'bagpipes', 
        'bandwagon', 
        'banjo', 
        'bayou', 
        'beekeeper', 
        'bikini', 
        'blitz', 
        'blizzard', 
        'boggle', 
        'bookworm', 
        'boxcar', 
        'boxful', 
        'buckaroo', 
        'buffalo', 
        'buffoon', 
        'buxom', 
        'buzzard', 
        'buzzing', 
        'buzzwords', 
        'caliph', 
        'cobweb', 
        'cockiness', 
        'croquet', 
        'crypt', 
        'curacao', 
        'cycle', 
        'daiquiri', 
        'dirndl', 
        'disavow', 
        'dizzying', 
        'duplex', 
        'dwarves', 
        'embezzle', 
        'equip', 
        'espionage', 
        'euouae', 
        'exodus', 
        'faking', 
        'fishhook', 
        'fixable', 
        'fjord', 
        'flapjack', 
        'flopping', 
        'fluffiness', 
        'flyby', 
        'foxglove', 
        'frazzled', 
        'frizzled', 
        'fuchsia', 
        'funny', 
        'gabby', 
        'galaxy', 
        'galvanize', 
        'gazebo', 
        'giaour', 
        'gizmo', 
        'glowworm', 
        'glyph', 
        'gnarly', 
        'gnostic', 
        'gossip', 
        'grogginess', 
        'haiku', 
        'haphazard', 
        'hyphen', 
        'iatrogenic', 
        'icebox', 
        'injury', 
        'ivory', 
        'ivy', 
        'jackpot', 
        'jaundice', 
        'jawbreaker', 
        'jaywalk', 
        'jazziest', 
        'jazzy', 
        'jelly', 
        'jigsaw', 
        'jinx', 
        'jiujitsu', 
        'jockey', 
        'jogging', 
        'joking', 
        'jovial', 
        'joyful', 
        'juicy', 
        'jukebox', 
        'jumbo', 
        'kayak', 
        'kazoo', 
        'keyhole', 
        'khaki', 
        'kilobyte', 
        'kiosk', 
        'kitsch', 
        'kiwifruit', 
        'klutz', 
        'knapsack', 
        'larynx', 
        'lengths', 
        'lucky', 
        'luxury', 
        'lymph', 
        'marquis', 
        'matrix', 
        'megahertz', 
        'microwave', 
        'mnemonic', 
        'mystify', 
        'naphtha', 
        'nightclub', 
        'nowadays', 
        'numbskull', 
        'nymph', 
        'onyx', 
        'ovary', 
        'oxidize', 
        'oxygen', 
        'pajama', 
        'peekaboo', 
        'phlegm', 
        'pixel', 
        'pizazz', 
        'pneumonia', 
        'polka', 
        'pshaw', 
        'psyche', 
        'puppy', 
        'puzzling', 
        'quartz', 
        'queue', 
        'quips', 
        'quixotic', 
        'quiz', 
        'quizzes', 
        'quorum', 
        'razzmatazz', 
        'rhubarb', 
        'rhythm', 
        'rickshaw', 
        'schnapps', 
        'scratch', 
        'shiv', 
        'snazzy', 
        'sphinx', 
        'spritz', 
        'squawk', 
        'staff', 
        'strength', 
        'strengths', 
        'stretch', 
        'stronghold', 
        'stymied', 
        'subway', 
        'swivel', 
        'syndrome', 
        'thriftless', 
        'thumbscrew', 
        'topaz', 
        'transcript', 
        'transgress', 
        'transplant', 
        'triphthong', 
        'twelfth', 
        'twelfths', 
        'unknown', 
        'unworthy', 
        'unzip', 
        'uptown', 
        'vaporize', 
        'vixen', 
        'vodka', 
        'voodoo', 
        'vortex', 
        'voyeurism', 
        'walkway', 
        'waltz', 
        'wave', 
        'wavy', 
        'waxy', 
        'wellspring', 
        'wheezy', 
        'whiskey', 
        'whizzing', 
        'whomever', 
        'wimpy', 
        'witchcraft', 
        'wizard', 
        'woozy', 
        'wristwatch', 
        'wyvern', 
        'xylophone', 
        'yachtsman', 
        'yippee', 
        'yoked', 
        'youthful', 
        'yummy', 
        'zephyr', 
        'zigzag', 
        'zigzagging', 
        'zilch', 
        'zipper', 
        'zodiac', 
        'zombie', 
    ]
        word=random.choice(words)
        return word

    print(logo)
    print(hang[0])

    print("Let's PLAY!!")
    def empty():
        blank=[]
        for _ in range(word_len):
            blank+='_'
        print(blank)
        return blank  

    word=get_word()
    word_len=len(word)
    blank=empty()

    lives=6
    hang_l=1

        
    while "_" in blank and lives>0 and hang_l<=7 :
        time.sleep(1)
        print('!!###Guess a letter,just one letter')
        time.sleep(1.5)
        print('More than one will cost you a life') 
        time.sleep(1)
        guess=input('Guess: ').lower()
        for position in range(word_len):
        
            if  word[position] == guess:
                blank[position]=guess
        blanke=' '.join(blank)        
        print(blanke)
        if len(guess) >1 or guess is int :
            print("You either just used more than one letter or you used a number.")
            time.sleep(1)
            print("Dont do it again.")
            time.sleep(2)
        if guess not in word:
            lives-=1
            hang_l+=1
            print( hang[hang_l])
            if lives==1:
                print(f'****You have {lives} life left.Try again****')
            elif lives==0:
                print("You've been hung!")
                time.sleep(1)
                print(f'The word was "{word}" ')
                time.sleep(1)
                print('Game Over!')
            else:
                print(f'you have {lives} lives left.Try again')
        
        
        if '_' not in blank:
            print("You guessed it!")