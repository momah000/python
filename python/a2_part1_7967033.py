import random
random.randint

n=input("Hi, what is your name?")
print("Welcome",n,"!")
print("Welcome to addition/multiplication test. How many questions will you like to be tested on?")
i=int(input("Enter a non-negative integer"))
print("This software tests you with", i,"questions")
q=input("enter 0 for or 1 to do the following,0)Addition /n 1)Multiplication")




def perform_test(n,i,q):
        if q==0o
        :
            print('addition')
            g=0
            for c in range (i):
                u=random.randint(0,9)
                p=random.randint(0,9)
                print("what is",u,'+', p,'?')
                a=int(input("ans="))
                if a==u+p:
                    g=g+1
                    print (n, "well done")
                else:
                    print("The correct anser is",u+p)

        elif q==1:
            print('Get ready to learn multiplication')
            g=0
            for c in range (i):
               d=random.randint(0,9)
               t=random.randint(0,9)
               print("What is", d,"x",t,"?")
               b=int(input('ans='))
               if b== int(d*t):
                   g=g+1
                   print("Correct!")

               else:
                   print("incorrect you fool!! the answer is,",d*t)
        else:
             print("You have selected a wrong entry")

##def grade(g,i):
##     if g/i>=0.8:
##         print("Ayy matey! Congratulations")
##     elif g/i>0.8 and g/i>0.5:
##         print("Not so bad but you should practice more")
##     else:
##         print("please study more and ask your techer for help")
##


    

                
               
                
                
                      

                
            
    
    
    
    
    
    
    
    
    
    

