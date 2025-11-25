
import sys
print('Error 1', file=sys.stderr)  # Error 1
sys.stderr.write('Error 2')        # Error 2
