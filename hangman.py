import string
import random
letters_guessed=[]

#returns the list of words
def load_words():
 #    Returns a list of valid words. Words are strings of lowercase letters.
   
 #    Depending on the size of the word list, this function may
 #    take a while to finish.

    print("Loading word list from file...")
    # inFile: file
    filename="words.txt"
    inFile = open(filename, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


#chooses a secret word

def choose_word(wordlist):
    secret_word=random.choice(wordlist)
    return secret_word


#defining hangman_with_hints
def hangman_with_hints():
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(cw),'long')
    print('-'*15)



#gets alphabets not guessed till now
def get_available_letters (letters_guessed):
      s=''
      for i in range (0,len(string.ascii_lowercase)):
          if string.ascii_lowercase[i] in letters_guessed:
              s=s+''
          else:
              s=s+string.ascii_lowercase[i]
      return s


  
def is_word_guessed (cw,letters_guessed):
    for i in range (0,len(cw)):
        if cw[i] in letters_guessed:
            continue
        else: 
            return False
    return True


#matches the unguessed word with other_word
def match_with_gaps(my_word,other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word)==len(other_word):
            for n in range (0,len(other_word)):
                if my_word[n]!='_':
                    if my_word[n]==other_word[n]:
                        continue
                    else:
                        return False
                else:
                    continue
            return True
    return False

        
#prints list of matched letters        
def show_possible_matches(my_word):
    list=[]
    for n in range (0,len(lw)):
        other_word=lw[n]
        if match_with_gaps(my_word, other_word) is True:
            list.append(other_word)
    print(list)
        

     
#the main game
def get_guessed_word (cw,letters_guessed):  
    letters_guessed=[]
    guess_num=6
    warnings=3
    letter=('_'+" ")*len(cw)
    # my_word=letter.replace(" ","")
    vowels=['a','e','i','o','u']

    
    while guess_num >0 and letter.strip() not in cw:
        print('You have',warnings,'warnings left' )
        print('You have',guess_num,'guesses left')
        print(get_available_letters(letters_guessed))
        user_input=input('Please guess a letter:')
        user_input=user_input.lower()
        letters_guessed += user_input
        
#       If letter guessed is an aste
     
        
        if letters_guessed[-1] not in string.ascii_letters or user_input in letters_guessed[:-1]:
            if warnings>0:
                warnings=warnings-1
           
            elif guess_num > 0:
                guess_num=guess_num-1
            else:
                break
            print('Oops!That is not a valid letter.You have',warnings,'left:',letter)
        

#       If valid letter, but not in secret word

        if letters_guessed[-1] not in cw:
            if guess_num > 0:
                if letters_guessed[-1] in vowels:
                    guess_num=guess_num - 2
                else:
                    guess_num=guess_num - 1
            print('Oops! Wrong guess:',letter)
            
#       If valid letter and in secret word
        else:
            for i in range (0,len(cw)):
                if letters_guessed[-1] in cw[i]:
                    x=i
                    letter=letter[0:2*x]+cw[x]+letter[2*x+1:]
            print('Good guess',letter)
                           
        if letters_guessed[-1]=='*':
            my_word = letter
            show_possible_matches(my_word)
                           
    if letter.strip()==cw:
        print('Congratulations! You have won the game')
    else:
        print('Sorry you lost!The letter was', cw)


            
        
lw=load_words()
print(lw)
cw=choose_word(lw)  

    
hangman_with_hints()

get_guessed_word(cw,letters_guessed)
    
           
    
           

    

  

 

    
    
