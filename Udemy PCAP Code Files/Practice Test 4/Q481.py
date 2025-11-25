
def quote(quo):

    def embed(str):
        return quo + str + quo

    return embed


dblq = quote('"')
print(dblq('Jane Doe'))  # "Jane Doe"
