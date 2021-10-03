from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

def unique_koala_facts(num):
    num = 28 if num>=28 else num
    koala_facts=[]

    while len(koala_facts)!=num:
        fact = random_koala_fact()
        if(fact not in koala_facts):
            koala_facts.append(fact)

    return koala_facts
        

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    
    timer=0
    for x in unique_koala_facts(50):
        if("joey" in x):
            print("Joey fact nr "+str(timer+1)+"\n"+x+"\n")
            timer+=1
