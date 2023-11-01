


def Juft(a):
    # bu juft sonlikni aniqlash uchun funksiya
    if a % 2 == 0:
        return True
    return False

b = [2,3,4,20]

result = list(map(lambda a: a**3, b))
print(result)