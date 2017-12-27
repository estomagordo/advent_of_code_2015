from hashlib import md5

def solve(prefix):
    x = 0

    while True:
        hd = md5((prefix + str(x)).encode()).hexdigest()
        if hd[:6] == '000000':
            return x

        x += 1

print(solve('bgvyzdsv'))