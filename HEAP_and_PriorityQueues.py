from queue import PriorityQueue, ReversedPriorityQueue, heappush, heappop

# Heap testing 1, using heappush and heappop from heapq module 
languages = []
heappush(languages, "Mandarin") #2 in alphabetical order
heappush(languages, "English")  #1 in alphabetical order
heappush(languages, "Tagalog")  #3 in alphabetical order
print("_"*30)
print(" Heap test 1:")
print(" Heap values before heappop: \t",languages)
