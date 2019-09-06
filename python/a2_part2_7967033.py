###Question 01
##def in_or_out_square(x,y,l,x2,y):
##    if l>0:
##        if ((x>x2<(x+l))and(y<y2<(y2+l))):
##            return"the point("+str(x2)+","+str(y2)')is in the circle'
##        else:
##            return"the point("+str(x2)+","+str(y2)+"is not in the circle"
##    else:
##        print('Invalid side length')
##    
#Question 02
def factorial(n):
    '''(number)->(number)
         takes as input one number, n,
        and returns the value n*(n-1)*(n-2)*⋯*2*1'''
    a=1
    for r in range (n):
        a=a*(r+1)
    return a
           
#Question 03
def strange_count(s):
     '''takes as input a string s and
       prints the number of characters in s that are lower case letters of
       English alphabet between 'b' and 's' (including 'b' and 's') or digits
       between '3' and '7' (including '3' and '7'). '''
     x="b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,3,4,5,6,7"
     totalx = 0
     for x in x:
         if x in s:
            totalx=totalx+1
     return totalx
           
#Question 04
def vote(s):
    '''takes the number of strings'yes' and 'no'in string results and calculates the percentage of 'yes' in result
     among all 'yes' and 'no'.'''      

    y=int(s.count('yes'))
    a=int(s.count('yes')+s.count('no'))
    percentageofy=(y/a)
    return percentageofy

#Question5
def vote_percentage():
    
    ''' (number)->(string)
    If all the votes are yes, then the proposal passes "unanimously", if at
    least 2/3 of the votes are yes, then the proposal passes with "super
    majority", if at least 1/2 of the votes are yes, then the proposal
    passes by "simple majority", and otherwise it fails'''
    
    d=input(print("Enter the yes, no, abstained votes one by one and then press enter"))
    a=float(vote(d))
    if a==1.0:
        print("Proposal passes unanimously")
    elif a>=0.6:
        print("Proposal passes with super majority")
    elif a==0.5:
            print("Proposal passes with simple majority")
    else:
        print("Proposal fails")

#Question6
def roman():
    '''(string)->(number)
    Returns roman numerals'''
    r=input("Enter a roman numeral using capital letters")
    s='M,D,C,X,V,I'
    m=int(r.count('M'))
    d=int(r.count('D'))
    c=int(r.count('C'))
    x=int(r.count('X'))
    v=int(r.count('V'))
    i=int(r.count('I'))
    for s in s:
            return (m*1000)+(d*500)+(c*100)+(x*10)+(v*5)+i

#Question7
def roman_v2():
    '''(string)->(number)
    Returns roman numerals'''
    s=input('Enter a roman number using capital letters M, D, C, X, and I')
    m=0
    d=0
    x=0
    c=0
    v=0
    i=0
    for e in s:
        if e =='M':
            m=m+1
        elif e=='D':
            d=d+1
        elif e=='X':
            x=x+1
        elif e=='C':
            c=c+1
        elif e=='V':
            v=v+1
        elif e=='I':
            i=i+1
            
    return(m*1000)+(d*500)+(c*100)+(x*10)+(v*5)+i

#Question8

def emphasize(s):
     '''that takes as an input a string s and
    returns a string with a blank space inserted between every pair of
    consecutive characters in s.'''
     return s.replace(""," ")[1:-1]


###Question 9
##def crypto(s):
##    ''' takes as an input a string s and
##    returns an encrypted string where encryption proceeds as follows:
##    split the text up into blocks of two letters each and swap each pair
##    of letters'''
##    c=list(s)
##    if len(s)%2==0:
##        for i in range(0, len(c), 2):
##            s=c[i]
##            c[i]=c[i+1]
##            c[i+1]=s
##            g=print(''.join(c))
##        return g
##    else:
##        for i in range[0, len(c), 2]:
##            if i==len(c)-1:
##                g=print(''.join(c))
##        return g
##
##    else:
##        s=t[i]
##        c[i]=[i+1]
##        c[i+1]=s



        
    
  

    

    
    

             
                        


    
          
    
    
    
                    
                    
    
   
    
   



     

    
            
        
   
