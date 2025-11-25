
class Content:
    title = "None"

    def __init__(self, this):
        self.name = this + " than " + Content.title


text_1 = Content("Paper")
text_2 = Content("Article")
print(text_1.title == text_2.name)  # False
