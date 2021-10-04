from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

def iterate_list(arr):
    for x in range(len(arr)):
        print(str(x+1)+":"+arr[x])

def unique_koala_facts(num):
    counter=0
    koala_facts=[]

    while len(koala_facts)!=num:
        fact = random_koala_fact()
        counter+=1
        if(fact not in koala_facts):
            koala_facts.append(fact)
        elif(counter==1000):
            return koala_facts

    return koala_facts

def count_joeys(facts):
    joey_facts=[]

    for x in facts:
        if('joey' in x):
            joey_facts.append(x)

    return len(set(joey_facts))

def num_joey_facts():
    facts=[]

    while True:
        random_fact = random_koala_fact()
        if(facts.count(random_fact)==10):
            return count_joeys(facts)
        elif(facts.count(random_fact)<10):
            facts.append(random_fact)


def koala_weight():
    facts= unique_koala_facts(28)
    weight=""
    for x in facts:
        if ('kg' in x):
            weight=x[x.find('kg')-2:x.find('kg')]

    return int(weight)

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':

    print()
