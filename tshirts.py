def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:  # ← bug: 38 queda fuera de S/M
        return 'M'
    else:
        return 'L'

if __name__ == '__main__':
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    print("All is well (maybe!)")

