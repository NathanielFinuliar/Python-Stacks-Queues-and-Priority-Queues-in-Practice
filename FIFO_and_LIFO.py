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
