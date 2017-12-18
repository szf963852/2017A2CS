def testBit(field, bit):
    if (field>>bit)%2==1:
        return(True)
    else:
        return(False)
    
def setBit(field, bit):
    if testBit(field,bit):
        return field
    else:
        return field+2**bit

def clearBit(field, bit):
    if testBit(field,bit):
        return field-2**bit
    else:
        return field

def toggle(field, bit):
    if testBit(field, bit):
        return field-2**bit
    else:
        return field+2**bit
