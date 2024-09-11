class PriorityQueue:
    def __init__(self):
        self.queue = []
    def swap(self,i,j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
    def insert(self, value):
        self.queue.append(value)
        i=len(self.queue)-1
        while i != 0 and self.queue[(i-1)//2]>self.queue[i]:
            self.swap(i,(i-1)//2)
            i= (i-1)//2
    def heapify(self,i):
        smallest=i
        left=2*i+1
        right=2*i+2
        if left<len(self.queue) and self.queue[left]<self.queue[smallest]:
            smallest=left
        if right<len(self.queue) and self.queue[right]<self.queue[smallest]:
            smallest=right
        if smallest!=i:
            self.swap(i,smallest)
            self.heapify(smallest)
    def extract_min(self):
        if len(self.queue)==0:
            print("Priority Queue is empty!")
            return None
        if len(self.queue)==1:
            return self.queue.pop()
        root=self.queue[0]
        self.queue[0]=self.queue.pop()
        self.heapify(0)
        return root
    def display(self):
        print(self.queue)

pq=PriorityQueue()
pq.insert(10)
pq.insert(30)
pq.insert(20)
pq.insert(5)
pq.insert(1)
print("Priority Queue:",end=" ")
pq.display()

print("Extracted Min:",pq.extract_min())

print("Priority Queue after extracting min:",end=" ")

pq.display()