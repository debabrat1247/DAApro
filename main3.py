from datetime import datetime
import math
dict = { }
t1 = datetime.today().timestamp()
with open('american_english.txt',"r") as f:
    for i in f:
        i = i.strip().split("\n")[0]
        dict[i]=1
t2 = datetime.today().timestamp()
print("Loading done!....here using python dictionary")
print("Time taken to load:",t2-t1,"secs")



while True:
    n=input("Enter a word to be checked: ")
    n = n.strip().split("\n")[0]
    t3 = datetime.today().timestamp()
    if n in dict.keys():
        print("All good, ", end =" ") 

    else:
        print("Not found")
    t4 = datetime.today().timestamp()
    print('time taken for lookup:',(t4-t3)*math.pow(10,6),"microsecond")
    con=input("Continue?[y/n]").lower()
    if con in ['n','no']:
        break
print("Closing...Goodbye")
