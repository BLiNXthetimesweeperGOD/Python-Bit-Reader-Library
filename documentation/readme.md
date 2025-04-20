# Bit Reader usage Documentation
Classes:
- BE_BitReader (Big Endian)
- LE_BitReader (Little Endian)

Usage format:

```python
file_bits_BE = BE_BitReader(opened_file) #Big Endian
file_bits_LE = LE_BitReader(opened_file) #Little Endian

#Seek to an offset
file_bits_LE.seek(offset)
file_bits_BE.seek(offset)

#Read a specified number of bits (can be anything above 0)
file_bits_LE.read(bits)
file_bits_BE.read(bits)

#Align to byte
file_bits_LE.align()
file_bits_BE.align()

#Get current offset (bits and bytes)
file_bits_LE.tell()
file_bits_BE.tell()
```
