class BE_BitReader: #Big Endian Bit Reader
    def __init__(self, file, offset=0):
        """Initialize BitReader with a file object opened in binary mode ('rb')
        Args:
            file: File object opened in binary mode
            offset (int): Starting byte offset in the file
        """
        self.file = file
        self.bitBuffer = 0
        self.bitsInBuffer = 0
        if offset > 0:
            self.file.seek(offset)
    
    def read(self, num_bits):
        """Read specified number of bits from the file
        
        Args:
            num_bits (int): Number of bits to read
            
        Returns:
            int: Value read from the bits
        """
        while self.bitsInBuffer < num_bits:
            byte = self.file.read(1)
            if not byte:
                raise EOFError("Reached end of file while reading bits")
            self.bitBuffer = (self.bitBuffer << 8) | int.from_bytes(byte, 'big')
            self.bitsInBuffer += 8
            
        value = (self.bitBuffer >> (self.bitsInBuffer - num_bits)) & ((1 << num_bits) - 1)
        self.bitsInBuffer -= num_bits
        return value
    
    def align(self):
        """Align the bit reader to the next byte boundary by discarding remaining bits"""
        self.bitBuffer = 0
        self.bitsInBuffer = 0
    
    def seek(self, offset):
        """Seek to a specific byte offset in the file
        
        Args:
            offset (int): Byte offset to seek to
        """
        self.file.seek(offset)
        self.bitBuffer = 0
        self.bitsInBuffer = 0
    
    def tell(self):
        """Get current position in the file
        
        Returns:
            tuple: (byte_offset, bits_into_byte)
            - byte_offset is the offset of the last byte read
            - bits_into_byte is how many bits we've read into the current byte
        """
        byte_pos = self.file.tell()
        
        if self.bitsInBuffer > 0:
            complete_bytes = self.bitsInBuffer // 8
            byte_pos -= complete_bytes
            bits_into_byte = 8 - (self.bitsInBuffer % 8)
            if bits_into_byte == 8:
                bits_into_byte = 0
        else:
            bits_into_byte = 0
            
        return (byte_pos, bits_into_byte)

class LE_BitReader: #Little Endian Bit Reader
    def __init__(self, file, chunk_size=1, offset=0):
        """Initialize BitReaderLE with a file object opened in binary mode ('rb')
        
        Args:
            file: File object opened in binary mode
            chunk_size (int): Number of bytes to read at once for each data chunk
            offset (int): Starting byte offset in the file
        """
        self.file = file
        self.chunk_size = chunk_size
        self.bitBuffer = 0
        self.bitsInBuffer = 0
        if offset > 0:
            self.file.seek(offset)
    
    def read(self, num_bits):
        """Read specified number of bits from the file in little endian order
        
        Args:
            num_bits (int): Number of bits to read
            
        Returns:
            int: Value read from the bits
        """
        while self.bitsInBuffer < num_bits:
            bytes_needed = max(self.chunk_size, (num_bits - self.bitsInBuffer + 7) // 8)
            chunk = self.file.read(bytes_needed)
            if not chunk:
                raise EOFError("Reached end of file while reading bits")
                
            value = int.from_bytes(chunk, 'little')
            self.bitBuffer |= value << self.bitsInBuffer
            self.bitsInBuffer += len(chunk) * 8
            
        value = self.bitBuffer & ((1 << num_bits) - 1)
        self.bitBuffer >>= num_bits
        self.bitsInBuffer -= num_bits
        return value
    
    def align(self):
        """Align the bit reader to the next byte boundary by discarding remaining bits"""
        remaining_bits = self.bitsInBuffer % 8
        if remaining_bits:
            self.bitBuffer >>= remaining_bits
            self.bitsInBuffer -= remaining_bits
    
    def seek(self, offset):
        """Seek to a specific byte offset in the file
        
        Args:
            offset (int): Byte offset to seek to
        """
        self.file.seek(offset)
        self.bitBuffer = 0
        self.bitsInBuffer = 0
    
    def tell(self):
        """Get current position in the file
        
        Returns:
            tuple: (byte_offset, bits_into_byte)
            - byte_offset is the offset of the last byte read
            - bits_into_byte is how many bits we've read into the current byte
        """
        byte_pos = self.file.tell()
        
        if self.bitsInBuffer > 0:
            complete_bytes = self.bitsInBuffer // 8
            byte_pos -= complete_bytes
            bits_into_byte = self.bitsInBuffer % 8
        else:
            bits_into_byte = 0
            
        return (byte_pos, bits_into_byte)
