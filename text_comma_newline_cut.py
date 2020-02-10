import os
import re

def tcnc(src):
    for root, dirs, files in os.walk(src):
        for name in files:
            if re.search(r'\.txt', name, re.I):
                rrr(root,name)

def rename(file_):
    return re.sub(
        r'\.txt$',
        '.cut',
        file_,
        flags=re.I,
    )

def rrr(r, n):
    file_ = os.path.join(r,n)
    with open(file_) as f:
        x = f.read()
        with open(rename(file_), 'w') as w:
            y = re.sub(
                r' *, *',
                '\n',
                x
            )
            w.write(y)

src = r'src'
tcnc(src)
