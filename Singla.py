import sys
sys.path.append('/module/')
import module
from module.mathy import *
print (responses[0])
print(responses[1])

while True:
    print()
    text=input("Enter some text ")
    for word in text.split(' '):
        l=extract_numbers_from_text(text)
        if word.upper() in operations.keys():
            try:
                
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something is wrong please, retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
