def conv_num(num_str):
    # Validate type
    if not isinstance(num_str, str):
        return None
    if num_str == "":
        return None

    idx = 0
    is_negative = False

    # Optional leading sign
    if num_str[0] == '-':
        is_negative = True
        idx = 1
        if idx == len(num_str):  # string was just "-"
            return None

    # Look at the remaining substring
    body = num_str[idx:]

    # Hex path: must start with 0x or 0X
    if len(body) >= 2 and body[0] == '0' and (body[1] == 'x' or body[1] == 'X'):
        # Hex cannot have any decimal point, but _parse_hex will catch invalid chars anyway
        hex_body = body[2:]
        return _parse_hex(hex_body, is_negative)

    # Decimal path (int or float)
    return _parse_decimal(body, is_negative)

def _hex_char_value(ch):
    """Return integer value of a single hex digit or None if invalid."""
    if '0' <= ch <= '9':
        return ord(ch) - ord('0')
    # Normalize to lowercase for alpha digits
    if 'A' <= ch <= 'F':
        return 10 + (ord(ch) - ord('A'))
    if 'a' <= ch <= 'f':
        return 10 + (ord(ch) - ord('a'))
    return None

def _parse_decimal(num_body, is_negative):
    # num_body has no sign and no '0x' prefix
    if not num_body:
        return None

    dot_count = 0
    for ch in num_body:
        if ch == '.':
            dot_count += 1
            if dot_count > 1:
                return None
        elif not ('0' <= ch <= '9'):
            return None

    # If no decimal point, parse as integer
    if dot_count == 0:
        value = 0
        for ch in num_body:
            value = value * 10 + (ord(ch) - ord('0'))
        if is_negative:
            value = -value
        return value

    # There is exactly one decimal point: parse as float
    dot_index = num_body.find('.')
    int_part_str = num_body[:dot_index]
    frac_part_str = num_body[dot_index + 1:]

    # integer part
    int_value = 0
    if int_part_str:
        for ch in int_part_str:
            # just accumulate
            int_value = int_value * 10 + (ord(ch) - ord('0'))

    # fractional part
    frac_value = 0.0
    divisor = 1.0
    if frac_part_str:
        for ch in frac_part_str:
            divisor *= 10.0
            frac_value += (ord(ch) - ord('0')) / divisor

    total = int_value + frac_value
    if is_negative:
        total = -total
    return total

def _parse_hex(num_body, is_negative):
    # num_body is the part after 0x/0X
    if not num_body:
        return None

    value = 0
    for ch in num_body:
        digit = _hex_char_value(ch)
        if digit is None:
            return None
        value = value * 16 + digit

    if is_negative:
        value = -value
    return value

def my_datetime(num_sec):
    """Takes integer value that represents number of seconds since epoch
    returns string of that date MM-DD-YYYY"""
    return None

def conv_endian(num,endian="big"):
    """Takes an integer value and converts to hexadecimal in either big or little endian"""
    #check for valid input
    if not isinstance(num, int):
        return None
    if not (endian == "big" or endian == "little"):
        return None
    if num == 0:
        return "00"

    #check for negative values
    is_negative = ""
    if num < 0:
        is_negative = "-"
        num = -1*num
    
    return is_negative + _make_string(num,endian)


def _make_byte(num):
    """Creates a single byte of information for a given number"""
    hexa_characters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    byte = hexa_characters[num%16]
    num = num//16
    byte = hexa_characters[num%16] + byte
    return byte

def _make_string(num,endian):
    """Recurvisely creates a string of bytes given a number and endian format"""
    new_num = num//16//16
    if num == 0: #actually wondering if this is necessary
        #theoretically this should never get called with 0
        return ""
    if new_num == 0:
        return _make_byte(num)
    if endian == "big":
        return _make_string(new_num,endian) + " " + _make_byte(num)
    else:
        return _make_byte(num) + " " + _make_string(new_num,endian)
        
