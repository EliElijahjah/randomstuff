import random
import pandas as pd
def colored(r,g,b,text):
    return"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)
not_word_pool =pd.read_csv('words2.csv')
word_pool=[]
for eachthing in not_word_pool['aback']:
    word_pool.append(eachthing)
guess=''
answer=word_pool[random.randint(0,len(word_pool)-1)]
result=''
goodguess=False
for each_thing in range(0,6):
    goodguess=False
    guess=input('Input Guess: ')
    for eachthing in word_pool:
        if eachthing==guess:
            goodguess=True
            break 
    if goodguess==False:
        guess+='hahahahaha'
        print("invalid word")
    if len(guess)==5:
        for each_number in range(0,5):
         if guess[each_number] == answer[each_number]:
                result+=colored(0,255,0,f"{guess[each_number]}")
         elif answer.count(guess[each_number])>0:
            result+=colored(255,255,0,f"{guess[each_number]}")
         else:
             result+=colored(255,0,0,f"{guess[each_number]}")
        print(result)
        result=''
    else:
        continue
    if guess==answer:
        print("you win!")
        break
if guess!= answer:
    print("You lose!")
    print(f'The Answer was {answer}')
