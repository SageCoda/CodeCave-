def cipher():
    logo = """           
    ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
    `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
            ""             88                                 
                            88                                 
    ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
    `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                88                                             
                88           
    """
    alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceaser(crypt,plain_text,shift_amount):
    
            w=[]
            for i in (text):
                if i in alphabet:
                    if crypt == 'encode':
                        cypher='encryption'
                        w.append(alphabet[(alphabet.index(i)+shift_amount)%27])
                    elif crypt == 'decode':
                        cypher='decryption'
                        w.append(alphabet[(alphabet.index(i)-shift_amount)%27])
                else:
                    w.append(i)
        
            word="".join(w)
            print(f'The {cypher} reads: {word}')
    

    ceaser(crypt=direction,plain_text=text,shift_amount=shift)

    restart=input("Type yes if you want to go again else type no ")
    while restart !='no':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(crypt=direction,plain_text=text,shift_amount=shift)
        restart=input("Type yes if you want to go again else type no ")






