
from datetime import datetime
datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))  # 19/November/27 11:27:22
print(datetime.strftime('%Y/%b/%d %H:%M:%S'))  # 2019/Nov/27 11:27:22
print(datetime.strftime('%y/%m/%d %H:%M:%S'))  # 19/11/27 11:27:22
print(datetime.strftime('%Y/%m/%d %H:%M:%S'))  # 2019/11/27 11:27:22
