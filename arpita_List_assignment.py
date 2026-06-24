##1.create a list with 5 friends and ask user a friend name and add that name in the list and print the list after that ask user to most important friend and add that friend at user choice
#create a list with 5 friends
#L=[1,2,3,4,5]
#friend_name=input("enter a name")
#L.append(friend_name)
#print(L)
#ask user most important friend name 
#n=input("enter a most important friend name ")
#L.insert(1,n)
#print(L)


##2.create a list of 10 number and print the list .
#J=[i for i in range(0,10)]
#print(J)



##3.create a list [1,10,100,3,6,8] and add 59 on 3 location after that append 5 and print list and length of list.
#J=[1,10,100,3,6,8]
#J.insert(3,59)
#J.append(5)
#print(J)
#print(len(J))



##4.find all the words in a list of strings that are less than 4 letters.
#words=['hi','hello','10','python','number','cat']
#n=[]
#for word in words:
   # if len(word)<4:
     #   n.append(word)
#print(n)   



##5.given numbers=range(20),produce a listcontaining the word "even" if a number in the number is a even ,and the word "odd" if the number is odd.Result would look like "odd","even",... 
#j=['even' if i%2==0 else 'odd' for i in range(20)]
#print(j) 

 

##6.find all the numbers from 1 to 1000 that are divisible by 7 .
# for i in range(1,1000):
#    if i%7==0:
#     print(i,end=" ")

##7.count the number of spaces in a string.
#text="python is a high level programming language"
#spaces=text.count(' ')
#print(spaces)


##8.find the common numbers in two lists(without using a tuple or set)
##Find the common numbers
# list_a=1,2,3,4          ##given list_a
# list_b=2,3,4,5          ##given list_b
# for i in list_a:
  # if i in list_b:
  #   print(i,end=" ")