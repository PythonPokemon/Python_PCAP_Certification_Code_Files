
class BluePrint:
    __element = 1

    def __init__(self):
        self.component = 1

    def __action(self):
        pass


product = BluePrint()

BluePrint._BluePrint__element += 1
print(BluePrint._BluePrint__element)  # 2

product._BluePrint__element += 1
print(product._BluePrint__element)    # 3

# BluePrint.element += 1
# AttributeError: type object 'BluePrint' has no attribute 'element'

# _product__element += 1
# NameError: name '_product__element' is not defined
