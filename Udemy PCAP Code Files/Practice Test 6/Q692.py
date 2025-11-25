
class Volume:
    chapter = 1

    def __init__(self, paragraph):
        self.paragraph = paragraph
        Volume.chapter += 1

    def remove(self):
        del self.paragraph


edition = Volume(1)
edition.remove()

print(Volume.__dict__['chapter'] != None)             # True
print(Volume.__dict__['chapter'] is not None)         # True
print(Volume.__dict__['chapter'])  # 2
# When edition was initialized, chapter was increased to 2.

print(len(edition.__dict__) != len(Volume.__dict__))  # True
print(len(edition.__dict__))  # 0
print(len(Volume.__dict__))   # 7

print('paragraph' in edition.__dict__)                # False
# The object edition doesn't have any attributes,
# because paragraph is removed.

print('paragraph' in Volume.__dict__)                 # False
# Even if paragraph wouldn't have been removed,
# it would not show up in the __dict__ of the class.
