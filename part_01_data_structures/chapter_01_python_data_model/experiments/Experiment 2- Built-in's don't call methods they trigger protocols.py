class Demo:
    def __len__(self):
        return 42


demo = Demo()

print(len(demo))
print(demo.__len__())
print(bool(len(demo)))

# Protocol insight; bool(x) -> x.__bool__() -> x.__len__() | if x.__bool__() is not overriden.


