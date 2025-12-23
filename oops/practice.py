# # # # # # # # # # def check(num):
# # # # # # # # # #     if num<=9:
# # # # # # # # # #         return num
# # # # # # # # # #     sum=0
# # # # # # # # # #     while num>9:
# # # # # # # # # #         sum+=num%10
# # # # # # # # # #         num//=10
# # # # # # # # # #     return check(sum)

# # # # # # # # # # print(check(877))

# # # # # # # # # def is_anagram(s1,s2):
# # # # # # # # #     if len(s1) != len(s2):
# # # # # # # # #         return False
    
# # # # # # # # #     freq1={}
# # # # # # # # #     freq2={}
# # # # # # # # #     # for i in s1:
# # # # # # # # #         # if i not in freq1:
# # # # # # # # #         #     freq1[i]=1
# # # # # # # # #         # else:
# # # # # # # # #         #     freq1[i]+=1
            
# # # # # # # # #     # for i in s2:
# # # # # # # # #     #     if i not in freq2:
# # # # # # # # #     #         freq2[i]=1
# # # # # # # # #     #     else:
# # # # # # # # #     #         freq2[i]+=1
    
# # # # # # # # #     for i,j in zip(s1,s2):
# # # # # # # # #         if i not in freq1:
# # # # # # # # #             freq1[i]=1
# # # # # # # # #             freq2[j]=1
# # # # # # # # #         else:
# # # # # # # # #             freq1[i]+=1
# # # # # # # # #             freq1[j]+=1
# # # # # # # # #     if freq
            
        
    
# # # # # # # # #     # for i in freq2:
# # # # # # # # #     #     if i not in freq1 or freq1[i]==0:
# # # # # # # # #     #         return False
        
            
        

# # # # # # # # # # print(is_anagram("listen", "silent"))  # True

# # # # # # # # s1="silentt"

# # # # # # # # freq = {}

# # # # # # # #     # Count characters in s1
# # # # # # # # for ch in s1:
# # # # # # # #     freq[ch] = freq.get(ch, 0)+1

# # # # # # # # print(freq)






# # # # # # # def next_prime(num):
# # # # # # #     status=True
# # # # # # #     while status:
# # # # # # #         if num<2:
# # # # # # #             # status=False
# # # # # # #             return 2
# # # # # # #         else:
# # # # # # #             num+=1
# # # # # # #             for i in range(2,num):
# # # # # # #                 if num%i==0:
# # # # # # #                     # status=True
# # # # # # #                     break
# # # # # # #             else:
# # # # # # #                 status=False
# # # # # # #                 return num
# # # # # # # print(next_prime(5))


# # # # # # Reverse a string without using slicing
# # # # # # x="raviteja"
# # # # # # rev=""
# # # # # # for i in range(len(x)-1,-1,-1):
# # # # # #     rev+=x[i]

# # # # # # print(rev)
# # # # # # Check whether a number is prime
# # # # # # num=15
# # # # # # for i in range(2,num):
# # # # # #     if num%i==0:
# # # # # #         print("not a prime")
# # # # # #         break
# # # # # # else:
# # # # # #     print("prime")
# # # # # # num=13
# # # # # # count=0
# # # # # # for i in range(1,num):
# # # # # #     if num%i ==0:
# # # # # #         count+=1
# # # # # # if count==1:
# # # # # #     print("prime")
# # # # # # else:
# # # # # #     print("not prime")
# # # # # # Find the largest and smallest element in a list (no built-ins)
# # # # # # lis=[1,2,3,4,5,6]
# # # # # # large=-float("Inf")
# # # # # # small=float("Inf")
# # # # # # for i in lis:
# # # # # #     if i>large:
# # # # # #         large=i
# # # # # #     if i<small:
# # # # # #         small=i
# # # # # # print(large,small)
    
# # # # # # Count vowels in a string
# # # # # # name="teja"
# # # # # # count=0
# # # # # # for i in name:
# # # # # #     if i in "aeiou":
# # # # # #         count+=1
# # # # # # print(count)
# # # # # # Swap two numbers without using a third variable
# # # # # # i=1
# # # # # # j=9
# # # # # # i,j=j,i
# # # # # # print(i,j)
# # # # # # Check whether a string is a palindrome
# # # # # # check="teja"
# # # # # # rev=""
# # # # # # for i in check:
# # # # # #     rev=i+rev
# # # # # #     print(rev)
# # # # # # Sum of digits of a number
# # # # # # num=153
# # # # # # sum=0
# # # # # # while num>0:
# # # # # #     sum+=num%10
# # # # # #     num//=10
# # # # # # print(sum)


# # # # # # def check(num):
# # # # # #     if num>9:
# # # # # #         sum=0
# # # # # #         while num>0:
# # # # # #             sum+=num%10
# # # # # #             num//=10
# # # # # #         if sum>9:
# # # # # #             return check(sum)
# # # # # #         return sum
# # # # # #     return num

# # # # # # a=check(111)
# # # # # # print(a)

# # # # # # def check(num):
# # # # # #     if num<10:
# # # # # #         return num
# # # # # #     s=0
# # # # # #     while num>0:
# # # # # #         s+=num%10
# # # # # #         num//=10
# # # # # #     return check(s)
# # # # # # a=check(987)
# # # # # # print(a)

# # # # # #     while num>9:
# # # # # #         sum+=num%10
# # # # # #         num//=10
# # # # # #     if sum>9:
# # # # # #         return check(sum)
# # # # # #     else:
# # # # # #         return sum
# # # # # # a=check(258)
# # # # # # print(a)
# # # # # # Find factorial using a function
# # # # # # num=int(input("enter number:"))
# # # # # # for i in range(1,num):
# # # # # #     num*=i
# # # # # # print(num)
# # # # # # Print first n Fibonacci numbers
# # # # # # n=10
# # # # # # a,b=0,1
# # # # # # for i in range(n):
# # # # # #     print(a,b)
# # # # # #     a,b=b,a+b
# # # # # # Count frequency of each character in a string
# # # # # # name="raviteja"
# # # # # # freq={}
# # # # # # for i in name:
# # # # # #     if i not in freq:
# # # # # #         freq[i]=1
# # # # # #     else:
# # # # # #         freq[i]+=1
# # # # # # print(freq)


# # # # # # LEVEL 2 — Lists, Tuples, Dictionaries

# # # # # # Remove duplicates from a list without using set
# # # # # # num=[1,1,2,3,4,6,8,9,7,4,9]
# # # # # # nondup=[]
# # # # # # for i in num:
# # # # # #     if i not in nondup:
# # # # # #         nondup.append(i)
# # # # # # print(nondup)
# # # # # # Find the second largest number in a list
# # # # # num=[1,5,2,8,6,9,3]
# # # # # first=second=-float("Inf")

# # # # # for i in num:
# # # # #     if i>first:
# # # # #         second=first
# # # # #         first=i
# # # # #     elif  and first<i:
# # # # #         second=i
        
# # # # # # print(first,second)

# # # # # # Merge two lists and sort without using sort()
# # # # a=[1,4,6,8]
# # # # b=[9,5,2,7]
# # # # a+=b
# # # # for i in range(len(a)):
# # # #     for j in range(i+1,len(a)):
# # # #         if a[i]>a[j]:
# # # #             a[i],a[j]=a[j],a[i]
# # # # print(a)
# # # # # # Find common elements between two lists
# # # # a=[1,2,3,9]
# # # # b=[4,5,2,1]
# # # # for i in (a):
# # # #     if i in b:
# # # #         print(i)
# # # # # # Convert a list into a dictionary
# # # # l=["a","b","c","d"]
# # # # # print(dict(enumerate(l)))
# # # # for i,fruit in enumerate(l,start=0):
# # # #     print(i,fruit)

# # # # l=[1,2,3,4,5]
# # # # c=list(enumerate(l))
# # # # print(c)
    
# # # # # # ["a", "b", "c"] → { "a": 1, "b": 2, "c": 3 }


# # # # # # Count frequency of elements in a list using dictionary

# # # # # # Find key with maximum value in a dictionary
# # # # d={"a":1,"b":2,"c":12}
# # # # a=0
# # # # k=""
# # # # for i,j in d.items():
# # # #     if j>a:
# # # #         k=i
# # # # print(k)
# # # # # # # Reverse a list in place

# # # # # # # Check if two lists are anagrams

# # # # # # # Sort a dictionary by values
# # # # d={"b":2,"a":-1,"c":12}

# # # # # sor={}
# # # # # for i,j in d.items():
# # # # #     if

# # # # a=sorted(d.items(), key=lambda i:i[1])
# # # # print(a)

# # # # a=[1,2,3,4,5]

# # # # squared=list(map(lambda x:x*2, a))
# # # # print(squared)

# # # a=[1,2,3,4,5]
# # # double=list(map(lambda x:x+5,a))
# # # print(double)


# # # Convert a list into a dictionary

# # # a=["a", "b", "c"]
# # # for i,a in enumerate(a,start=1):
# # #     print(a,i)
        
# # # # print(dict(enumerate(a)))

    
# # # # { "a": 1, "b": 2, "c": 3 }

# # # a=["r",'a','v','i']
# # # new=""
# # # for i in range(int(len(a)/2)):
# # #     a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
# # # print(a)
# # # a=['teja','ravi']
# # # for i in range(int(len(a)/2)):
# # #     a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
# # # print(a)
# # # new=""
# # # for i in a:
# # #     new+=i+" "
# # # print(new)


# # # Write a recursive function for factorial
# # # def fact(num):
# # #     if num<0:
# # #         return "negative numbers not allowed "
# # #     elif num==0:
# # #         return 1
# # #     fac=num
# # #     for i in range(1,num):
# # #         fac*=i
# # #     return fac
        
# # # a=fact(-1)
# # # print(a)
# # # def check(num):
# # #     if num==0:
# # #         return 1
# # #     return num*check(num-1)
# # # a=check(5)
# # # print(a)


# # # Write a function to flatten a nested list
# # # a=[1,[2,3],[4,[5,6]]]
# # # def outer():
    
# # #     new=[]
# # #     def check(sy):
# # #         for i in sy:
# # #             if type(i)==list:
# # #                 check(i)
# # #             else:
# # #                 new.append(i)
# # #         return new
# # #     check(a)
# # # print(outer())



    
# # #     for i in a:
# # #         if type(i)==list:
# # # new=[]          
# # # x=check(a)
# # # print(x)

# # # for i in a:
# # #     if type(i)==list:
# # #         for j in i:
# # #             if type(j)==list:
# # #                 new+=j
# # #             else:
# # #                 new.append(j)
# # #     else:
# # #         new.append(i)
# # # print(new)

# # while True:
# #     continue

# # h="hub".split("")
# # print(h)
# h="her"
# new=[i for i in h]
# print(new)


# with open("daa.txt","r") as file:
#     print(file.read())

# if __name__ == "__main__":
#     f = open("daa.txt", "r")
#     print(f.readline())
#     print("Main file")


a=["a","b","h"]
print(id(a))
b=["a","b","h"]
print(id(b))
# print(a == b)