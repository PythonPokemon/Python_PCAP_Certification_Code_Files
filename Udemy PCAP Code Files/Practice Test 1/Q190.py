
import platform

print(platform.platform())   # e.g. macOS-10.16-x86_64-i386-64bit
print(platform.processor())  # e.g. i386

# print(platform.hardware())  # AttributeError: ...

print(platform.node())  # my_computer.my_domain
