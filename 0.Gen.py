import random
import sys


words_vn = [
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ['không', 'miệng', 'to', 'bận', 'trắng', '(hỏi) không', 'rất', 'đàn ông', 'tôi', 'you (bạn…)', 'mẹ', 'bố'],
]

words_cn = [
    ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十'],
    ['不', '口', '大', '忙', '白', '妈', '很', '汉', '我', '你', '妈妈', '爸爸']
]
line = 1

while True:
    kb = int(input("Control: "))
    match kb:
        case 0:
            sys.exit(0)
        case 1:
            string = input("VN words: ")
            string = string.split("\t")
            print(string)
            string = input("CN words: ")
            string = string.split("\t")
            print(string)
        case 2:
            count = 0
            while words_vn[line]:
                i = random.randint(0, len(words_vn[line]) - 1)
                print(f"VN: {words_vn[line][i]}")
                input()
                print(f"CN: {words_cn[line][i]}")
                print()
                words_vn[line].pop(i)
                words_cn[line].pop(i)
                count += 1
                