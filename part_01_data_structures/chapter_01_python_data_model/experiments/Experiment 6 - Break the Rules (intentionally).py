class Weird:

    def __len__(self):
        return -1


w = Weird()
print(len(w))

# __len__() should return >= 0
