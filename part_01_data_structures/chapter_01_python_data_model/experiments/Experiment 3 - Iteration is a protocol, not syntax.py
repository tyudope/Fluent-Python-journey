class CountDown:

    def __init__(self, start):
        self.start = start


    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1



for i in CountDown(3):
    print(i)