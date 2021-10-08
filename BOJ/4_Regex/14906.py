import re

def is_slump(str):
    if re.match('^[DE]F+([DE]F+)*G$', str):
        return True
    else:
        return False

#^A(H$|(^[DE]F+([DE]F+)*G)C$|)
def is_slimp(str):
    re.match('^A(H$|([DE]F+([DE]F+)*G)C$|B)', str)
    if len(str) < 2:
        return False
