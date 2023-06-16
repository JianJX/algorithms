#Organizing Containers of Balls
'''
David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

Each container contains only balls of the same type.
No two balls of the same type are located in different containers.
'''

'''
calculate total number of balls for each type
loop and calculate the total number of balls in each container
if the numbers of balls of that type doesn't match its corresponding container
return impossible
'''
def organizingContainers(container):
    count = [0]*len(container[0])
    for i in container:
        temp = 0
        for j in i:
            count[temp]+=j
            temp+=1
    temp = 0
    for i in count:
        flag = False
        for j in container:
            if i == sum(j):
                flag = True
        if flag == False:
            return "Impossible"
    return "Possible"
