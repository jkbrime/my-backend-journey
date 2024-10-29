#1 create a function that squares a number
def sqr(x):
    return x*x
print(sqr(13))

#2 create a function to find the average of numbers in a list
def avg(list):
    return sum(list)/len(list)
print(avg([1,2,3,4,5]))

#3 create a function to reverse a list
def reverse(list):
    print(list[::-1])
    return
reverse([1,2,23,6])

#4
def cap():
    word = input('enter a word')
    print(word.upper())
    return
cap()

#5 to remove a number that appeared more than once from a list
def dup_removal(list_1):
    set1 = set(list_1)
    print(list(set1))
    return
dup_removal([1,2,3,3,4,5,5,6,7])

def combinator(list1, list2):
    print(set(list1)| set(list2))
    return
combinator([1,2,3,4],[5,6,7,8,9])