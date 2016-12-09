#!/usrbin/python3


def decompressSize(compressed, recurse):
    index = 0
    size = 0

    while "(" in compressed[index:]:
        markerLoc = compressed[index:].find("(")
        closeLoc = compressed[index:].find(")")
        size += markerLoc
        marker = compressed[(index+markerLoc+1):(index+closeLoc)]
        markerString = "".join(marker)
        splitMarker = markerString.split("x")
        length = int(splitMarker[0])
        multiplier = int(splitMarker[1])
        substring = compressed[(index+closeLoc+1):(index+closeLoc+1+length)]
        if recurse and "(" in substring:
            substringSize = decompressSize(substring, recurse)
        else:
            substringSize = len(substring)
        size += (substringSize * multiplier)
        index += closeLoc + 1 + length
    size += len(compressed[index:])
    return size

raw = input("? ")
print decompressSize(raw, False)
print decompressSize(raw, True)
