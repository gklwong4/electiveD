# Return True if the queue is empty
def isEmpty():    
    return ______________________
 

# Retutn True if the queue is full
def isFull():
    return __________________________


# Function to add an item to end of the queue
def add(item):
    global queue, front, end           #required in Python if we're modifying a global variable    
    
    
    
  

# Function to remove the front item from the queue
def remove():
    global queue, front, end
    
    
    
    
    return ______________
    
    
# Function to return the number of items in the queue
def size():
    return ____________________


# Function to return the front item without removing it from the queue
def peek():    
    if isEmpty():
        return None
    return queue[front]


# Function to print the queue contents
def printQueue():
    if isEmpty():
        print('Queue is empty')
    else:        
        for i in range(front, front+size()):
            print(f'{queue[i]} ', end=' ')    
    print()



'''
Global variables
'''
queue_size = 5                  #set queue_size here
queue = [None]*10000            #build a very long list
front = 0                       #front pointing to the first item of the queue
end = -1                        #end pointing to the last item of the queue, end < front if queue is empty


'''
Driver code - test the queue operations here
'''
add('a')
add('b')
add('c')
printQueue()
print('Dequeue:', remove())
printQueue()

add('d')
add('e')
add('f')
add('g')
printQueue()

print('Dequeue:', remove())
add('g')
printQueue()


print(f'The front item: {peek()}')
