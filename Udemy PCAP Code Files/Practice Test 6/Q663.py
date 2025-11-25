
class CriticalError(Exception):
    def __init__(self, message='This is a critical error.'):
        Exception.__init__(self, message)


raise CriticalError()

"""
Traceback (most recent call last):
  File "....py", line 7, in <module>
    raise CriticalError()
__main__.CriticalError: This is a critical error.
"""

