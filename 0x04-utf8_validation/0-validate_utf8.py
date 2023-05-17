def validUTF8(data):
    # Number of bytes to validate for the current character
    num_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte
        if num_bytes > 0 and (byte >> 6) == 0b10:
            num_bytes -= 1
        # Check if the current byte is a starting byte
        elif num_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            mask = 0b10000000
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # Handle invalid cases
            if num_bytes == 1 or num_bytes > 4:
                return False
        # Invalid case: current byte is not a continuation byte
        else:
            return False

    # Check if all expected continuation bytes are present
    return num_bytes == 0
