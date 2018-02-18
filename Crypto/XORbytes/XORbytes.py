import re

SHOW_ALL = False

regex = re.compile(b'gigem', re.IGNORECASE)
narrow_regex = re.compile(b'gigem{\w+}', re.IGNORECASE)

found = set()
with open('hexxy', 'rb') as f:
    data = f.read()

for i in range(len(data)):
    shifted = data[i:] + data[:i]
    xored = bytes(x ^ y for x, y in zip(data, shifted))
    m = regex.search(xored)
    if m:
        value = xored[m.start():m.start() + 32]
        m = narrow_regex.match(value)
        if m and m.group(0) not in found:
            found.add(m.group(0))
            if SHOW_ALL:
                print('Possible solution at {}: {}'.format(i, m.group(0)))
            else:
                print('Found solution at {}: {}'.format(i, m.group(0)))
                break
