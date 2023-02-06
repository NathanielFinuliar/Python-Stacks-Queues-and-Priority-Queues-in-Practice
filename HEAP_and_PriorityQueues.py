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
