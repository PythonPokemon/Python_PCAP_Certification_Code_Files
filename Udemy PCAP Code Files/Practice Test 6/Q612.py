
languages = ['English', 'Spanish', 'German']
more_languages = ['English', 'Spanish', 'German']
extra_languages = more_languages

print(more_languages is extra_languages)  # True
print(languages == more_languages)        # True
print(languages is more_languages)        # False
print(languages is extra_languages)       # False

print(id(languages))        # e.g. 140539383900864
print(id(more_languages))
# e.g. 140539383947452 (same number than extra_languages)
print(id(extra_languages))
# e.g. 140539383947452 (same number than more_languages)
