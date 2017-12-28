def is_valid(password):
    l = len(password)

    increasing_trip = False
    for x in range(l - 2):
        if ord(password[x]) == ord(password[x + 1]) - 1 and ord(password[x]) == ord(password[x + 2]) - 2:
            increasing_trip = True
            break

    if not increasing_trip:
        return False

    if 'i' in password or 'o' in password or 'l' in password:
        return False

    pairs = False
    for x in range(l - 3):
        if password[x] == password[x + 1]:
            for y in range(x + 2, l - 1):
                if password[y] == password[y + 1]:
                    pairs = True
                    break

    return pairs

def solve(password):
    while not is_valid(password):
        pos = -1
        paslist = list(password)
        
        while paslist[pos] == 'z':
            pos -= 1
        
        paslist[pos] = chr(ord(paslist[pos]) + 1)
        
        for x in range(pos + 1, 0):
            paslist[x] = 'a'

        password = ''.join(paslist)

    return password

print(solve('hxbxwxba'))