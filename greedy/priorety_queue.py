class PriorityQueue:
    def __init__(self):
        self.data = []

    def insert(self, element):
        self.data.append(element)
        i = len(self.data)
        while i // 2 >= 1:
            if self.data[i-1] > self.data[i//2 - 1]:
                self.data[i-1],self.data[i//2 - 1] = self.data[i//2 - 1],self.data[i-1]
                i //= 2
            else:
                break

    def extract_max(self):
        result = self.data[0]
        if len(self.data) == 1:
            self.data.pop()
            return result

        self.data[0] = self.data.pop()
        i = 1
        while 2*i <= len(self.data):
            if 2*i + 1 <= len(self.data):
                if self.data[i-1] < self.data[2*i -1] and self.data[2*i] <= self.data[2*i -1]:
                    self.data[i-1], self.data[2*i -1] = self.data[2*i -1], self.data[i-1]
                    i = 2*i
                elif self.data[i-1] < self.data[2*i] and self.data[2*i - 1] <= self.data[2*i]:
                    self.data[i-1], self.data[2*i] = self.data[2*i], self.data[i-1]
                    i = 2*i + 1
                else:
                    break
            else:
                if self.data[i-1] < self.data[2*i-1]:
                    self.data[i-1], self.data[2*i-1] = self.data[2*i-1], self.data[i-1]
                break

        return result


pr_q = PriorityQueue()
n = int(input())
for i in range(n):
    commands = input().split()
    if commands[0] == 'Insert':
        pr_q.insert(int(commands[1]))
    else:
        print(pr_q.extract_max())
    # print(pr_q.data)
