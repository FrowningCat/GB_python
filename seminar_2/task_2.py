import sys

data = [5, "hello", 3.14, True, 5]
i = 0

while i < len(data):
    if isinstance(data[i], int):
        print('position:', i, 'var:', data[i], 'id:', id(data[i]), 'size:', sys.getsizeof(data[i]), 'hash:',
              hash(data[i]), 'int: True')
    elif isinstance(data[i], str):
        print('position:', i, 'var:', data[i], 'id:', id(data[i]), 'size:', sys.getsizeof(data[i]), 'hash:',
              hash(data[i]), 'str: True')
    else:
        print('position:', i, 'var:', data[i], 'id:', id(data[i]), 'size:', sys.getsizeof(data[i]), 'hash:',
              hash(data[i]))
    i += 1
