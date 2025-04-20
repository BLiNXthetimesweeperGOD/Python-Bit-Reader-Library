# Python Bit Reader Library
I'm releasing this as a standalone library because it's really annoying to find any sort of bit reader library online for Python.

This allows you to read a file's contents bit by bit (and effectively read as many as you want at once)

#### Use cases
- You can read integers in both little and big endian and of any bit width with just a single BitReader.read()
- File formats that store data smaller than a byte don't need any extra decoding/bit shifting logic
- You can mix BitReader reads with normal Python file I/O reads, meaning you aren't limited to the output of this library

#### Usage example
```python
from BitReader import *

with open("TEST.bin", "w+b") as TEST: #Open a file named "TEST.bin" and write a simple byte string
    TEST.write(b'These are some bytes')

with open("TEST.bin", "rb") as test: #Open TEST.bin again and print out the bytes
    testReader = LE_BitReader(test) #Open the file in the Bit Reader (endianness doesn't matter for this example)
    for i in range(20):
        data = testReader.read(8) #Read 8 bits at a time, as each character is 8 bits wide
        print(chr(data)) #Display the characters
```

This library has both a big endian class (BE_BitReader) and a little endian class (LE_BitReader).

Nobody needs to ask for permission to use this. I released it as a standalone library for convenience.

#### External dependencies
There is none. It doesn't need to have anything extra installed besides Python itself to work.

This was written with Python 3, so I'd recommend using Python 3 with this.
