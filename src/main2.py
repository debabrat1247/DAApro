from linearprob import linearprob
import time
import math
def loadHashTable(name):
    ch = linearprob(105000)
    with open(name,"r") as f:
        for i in f:
            
            ch.insert([i])
    return ch

def addnewword(add_new,ch):
    add_new = add_new + '\n'
    f = open("american_english.txt",'a')
    f.write(add_new)
    f.close()
    ch.insert([add_new])

def AutoCorrect(dic,word):
    word=word+"\n"
    possible_words=list()
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(word)-2,-1,-1):
        for letter in alphabets:
            new_word=list(word)
            new_word[i]=letter
            new_word=''.join(new_word)
            isvalid=dic.lookup(new_word)
            if (isvalid):
                if(new_word[:len(new_word)-1] in possible_words):
                    pass

                else:

                    possible_words.append(new_word[:len(new_word)-1])

            new_word2=list(word)
            new_word2.append('')
            for j in range(len(word)-1,i,-1):
                new_word2[j+1]=new_word2[j]
            new_word2[i+1]=letter
            new_word3=list(new_word2)
            if i==0:
                new_word3[i+1]=new_word3[i]
                new_word3[i]=letter
                new_word3=''.join(new_word3)
                isvalid=dic.lookup(new_word3)
                if (isvalid):
                    if (new_word3[:len(new_word3)-1] in possible_words):
                        pass

                    else:

                        possible_words.append(new_word3[:len(new_word3)-1])
            new_word2=''.join(new_word2)
            isvalid=dic.lookup(new_word2)
            if isvalid:
                if(new_word2[:len(new_word2)-1] in possible_words):
                    pass
                else:
                    possible_words.append(new_word2[:len(new_word2)-1])

        new_word4=list(word)
        for j in range(i,len(word)-1):
            new_word4[j]=new_word4[j+1]
        temp=new_word4.pop()
        new_word4=''.join(new_word4)    
        isvalid=dic.lookup(new_word4)
        if isvalid:
            if (new_word4[:len(new_word4)-1]):
                pass
            else:
                possible_words.append(new_word4[:len(new_word4)-1])

    return possible_words

def display(mistakes):
    if len(mistakes)>0:
        for i in mistakes:
            if len(mistakes[i])>0:
                print(i," can be replaced by:",mistakes[i])
            else:
                print("Cannot find a replacement for",i)
    else:
        print("All good!")


def main():
    print("---------------------SPELL-CHECK-------------------------")
    print("Starting to load linearprobing Hash Table...")
    t0=time.clock()
    ch = loadHashTable("american_english.txt")
    print("Loading done!")
    t1=time.clock() - t0
    print("Time taken to load:",t1,"s")
    while True:
        sent=input("Enter a word to be checked: ")
        t0=time.clock()
        mistakes={}
        if not ch.lookup(sent+"\n"):
            t1=time.clock() - t0
            mistakes[sent]=AutoCorrect(ch,sent)
        else:
            t1=time.clock() - t0
        display(mistakes)
        
        print("Time taken for lookup:",t1*math.pow(10,6),"microsecond") 
        if(len(mistakes) and input("Do you want to add this to your dictionary?[y/n]").lower() == 'y'):
            addnewword(sent,ch)
        con=input("Continue?[y/n]").lower()
        if con in ['n','no']:
            break
    print("Closing...Goodbye")



if __name__=='__main__':
    main()