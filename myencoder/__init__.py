import base64
ASCII = 'ascii'

""" Return converted string as hex """
def convertToHex(string):
    if(string is None):
        return

    hexStr = ''
    for char in string:
        hexStr += format(ord(char), 'x')

    return hexStr


""" Encode to base64 """
def encodeToBase64(string):
    return base64.b64encode(string.encode(ASCII)).decode(ASCII)


""" Decode from base64 """
def decodeFromBase64(string):
    try:
        return base64.b64decode(string.encode(ASCII)).decode(ASCII)

    except:
        print('string: {0} was not in correct format perhaps'.format(string))
        return None
