# Все равны, как на подбор

def same_by(characteristic, objects):
    characteristic = True
    for i in objects:
        if i % 2 != 0:
            characteristic = not characteristic
            break
    return characteristic


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')