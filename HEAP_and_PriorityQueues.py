from queue import PriorityQueue, ReversedPriorityQueue, heappush, heappop

# Heap testing 1, using heappush and heappop from heapq module 
languages = []
heappush(languages, "Mandarin") #2 in alphabetical order
heappush(languages, "English")  #1 in alphabetical order
heappush(languages, "Tagalog")  #3 in alphabetical order
print("_"*30)
print(" Heap test 1:")
print(" Heap values before heappop: \t",languages)

heappop(languages)
print(" Heap values after heappop: \t",languages)

# Heap testing 2, heap prioritized order concept using tuples
print("_"*30)
print("Heap test 2:")
entity1 = ("King","Skill", 100)
entity2 = ("King","Power", 100)
entity3 = ("King","Power", 50)

if(entity1 > entity2):
    print("Level 100 King with Skill has higher priority than Level 100 King with Power")
if(entity3 < entity2):
    print("Level 50 King, has a lower priority than Level 100, King")


# Priority Queue testing 1
Hard = 1
Medium = 2
Easy = 3

challenge = PriorityQueue()
challenge.enqueue_with_priority(Easy, "Level 1")
challenge.enqueue_with_priority(Medium, "Level 3")
challenge.enqueue_with_priority(Hard, "Level 5")
challenge.enqueue_with_priority(Medium, "Level 4")

print("_"*30)
print("Priority Queue Test 1: ")
for _ in range(len(challenge._elements)):
    print(challenge.dequeue())

# Priority Queue testing 2
Hard = 1
Medium = 2
Easy = 3
