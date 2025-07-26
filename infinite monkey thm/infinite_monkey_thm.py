# Infinite Monkey Theorem
import random
class Monkey:
    def __init__(self,best=0,sen=None):
        self.best=best
        self.sen=sen
        

    def sentence_input(self):
        self.sen = input("Please enter the string: ")

    def match(self,gen):
        if self.sen==gen:
            print("Found")
            self.best=100
            return 
        self.best_score_update(gen)
        
    
    def score(self,gen):
        score=0
        for i in range(len(self.sen)):
            if self.sen[i]==gen[i]:
                score+=1
        return (score/len(gen))*100
    
    
    def best_score_update(self,gen):
        s= self.score(gen)
        print(gen, s)
        if s>self.best:
            self.best = s
        return
    
    def generate(self):
        l = len(self.sen)
        alphabets = "abcdefghijklmnopqrstuvwxyz "
        gen=""
        while len(gen)!=l:
            gen+= alphabets[random.randint(0,26)]
        self.match(gen)

print("Welcome!")

monkey= Monkey()
monkey.sentence_input()
opt='Y'
while monkey.best!=100 and opt=='Y':
    count=0
    while monkey.best!=100 and count!=10000:
        monkey.generate()
        count+=1
    if count==10000 and monkey.best!=0:
        print("Completed 50 trials")
        print("Your best score till now:",monkey.best)
        print("Wanna continue?")
        opt=input("Y or N")
print(count)
        
        