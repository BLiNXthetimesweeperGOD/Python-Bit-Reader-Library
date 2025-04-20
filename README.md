# Python Bit Reader Library
I'm releasing this as a standalone library because it's really annoying to find any sort of bit reader library online for Python.

### Usage example
```python
from BitReader import *

with open("TEST.bin", "w+b") as TEST: #Open a file named "TEST.bin" and write a simple byte string
    TEST.write(b'These are some bytes')

with open("TEST.bin", "rb") as test: #Open TEST.bin again and print out the bytes
    testReader = LE_BitReader(test)
    for i in range(20):
        data = testReader.read(8) #Read 8 bits at a time, as each character is 8 bits wide
        print(chr(data)) #Display the characters
```
