# print('siemanko')
#
# blacks_count = int(input('ile masz czarnuchów?\n'))
#
# if blacks_count > 0:
#     print("zabic")
# elif blacks_count < 0:
#     print("dobra liczba czarnuchow")
# else:
#     print("nie trzeba zabic")
#
# for i in range(48, 156, 4):
#     print(i)
# while blacks_count > 0:
#     print(" zabic czarnuchuw 🗡️👨🏿☠️----> ", "zostalo", '👨🏿' * blacks_count, "nigerów")
#     blacks_count -= 1

# liczba = 1000000.12345
# dupa = f'dgsdfsdgsdfs {czarnuch:_.4f}'
# print(dupa)

# czarnuchy = [l for l in "murzyn"]
# print(czarnuchy)


murzyny = [4, 5, 6, 3, 2, 2, 1, 2, 5, 5]
for i, ocena in enumerate(murzyny):
    if i % 3 == 0 and ocena < 6:
        print(f"indeks: {i}, ocena:{ocena}")

murzyny.append(6)
murzyny.extend(sorted([4, 9, 11, 8],
                      reverse=True))
print(murzyny)
# DOHLCV
candle1 = [2, 3, 4, 5, 0.5]
candle2 = [3, 4, 4, 5, 0.5]
candle3 = [4, 5, 4, 5, 0.5]
candle4 = [5, 6, 4, 5, 0.5]
candles = [candle1, candle2, candle3, candle4]
print(candles)
# murzyny = sorted(murzyn)
# 3 swieca high fstring
print(f'3 swieca high= {candles[2][2]}')

