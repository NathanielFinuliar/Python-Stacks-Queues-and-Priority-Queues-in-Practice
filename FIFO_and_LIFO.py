from queue import Queue, Stack

# FIFO(First In First Out)
# FIFO testing with enqueue and dequeue
print("_"*20)
FIFO_1 = Queue()
FIFO_1.enqueue("A1")
FIFO_1.enqueue("B2")
FIFO_1.enqueue("C3")

print("FIFO Test 1:")
for _ in range(len(FIFO_1)):
    print(" ",FIFO_1.dequeue())

# FIFO testing with Queues
print("_"*20)
FIFO_2 = Queue("A1","B2","C3")
print("FIFO Test 2:")
print("FIFO 2 length before: ",len(FIFO_2))
for item in FIFO_2:
    print(" ",item)

print("FIFO 2 length after: ",len(FIFO_2))


# LIFO (Last In First Out)
# LIFO testing with Stacks
print("_"*20)
print("LIFO Test 1:")
print("LIFO_1 Insert Order: ['A1', 'B2', 'C3']")
