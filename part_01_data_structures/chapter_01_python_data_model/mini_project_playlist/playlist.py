class Playlist:

    def __init__(self, songs):

        self._songs = list(songs)


    def __len__(self):
        return len(self._songs)

    # If we didn't implement __getitem__ , object is not subscriptable.
    # When python sees
    # for song in playlist:
    # it tries in this order:
    # 1. Does the object have __iter__ ?
    # 2. If not, does it have __getitem__ starting at index 0?
    # Our playlist has no __iter__ but it does have __getitem__.
    # That's why iteration works.
    def __getitem__(self, index):
        return self._songs[index]


    # string representation for the developer
    def __repr__(self) -> str:
        return f"(Playlist ({self._songs}))"


    # string representation for the user
    def __str__(self) -> str:
        return " -> ".join(self._songs)


    # Operator overloading (Pythonic way)
    def __add__(self, other):
        return Playlist(self._songs + list(other))


    def __eq__(self, other):
        return self._songs == list(other)



p = Playlist(["Brooklyn Baby","Starboy"])

print(p)
print([p]) # Why does list use __repr__ and not __str__ ?
# python must diplay the list elements. lists are for developers, not end users.
# because repr must be:
# unambiguous
# debug-friendly
# ideally valid Python code


# When python sees
    # for song in playlist:
    # it tries in this order:
    # 1. Does the object have __iter__ ?
    # 2. If not, does it have __getitem__ starting at index 0?
    # Our playlist has no __iter__ but it does have __getitem__.
    # That's why iteration works.
for song in p:
    print(song)


# When python sees
    # It tries:
    # playlist.__contains__("This is a man's world") -> not defined in this case
    # Fallback: iterate over the object
    # __getitem__.
if "This is a man's world" in p:
    print("true")


# If you implement __getitem__
# You automatically get
# iteration
# containment
# slicing
# unpacking
# compatibility