# NLP100本ノック! かっとばせ〜〜！

# 1章

import re
import random

# 1


def p1():
    s = "stressed"
    return s[::-1]

# 2


def p2():
    s1 = "パタトクカシーー"
    return s1[::2]

# 3


def p3():
    s = "パトカー"
    s1 = "タクシー"
    s2 = ""
    for i, i1 in zip(s, s1):
        s2 += i + i1
    return s2

# 4


def p4(s):
    vocab = ""
    vocab_l = []
    for j, i in enumerate(s):
        if i == " " or (j == len(s) - 1):
            vocab_l.append(vocab)
            vocab = ""
        elif i == "," or i == ".":
            continue
        else:
            vocab += i
    return vocab_l

# 5


def p5():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    vocab = ""
    vocab_l = []
    vocab_dic = {}
    for i in s:
        if i == " ":
            vocab_l.append(vocab)
            vocab = ""
        elif i == "," or i == ".":
            continue
        else:
            vocab += i

    for i in range(len(vocab_l)):
        print(i)
        if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            vocab_dic[vocab_l[i][0]] = i
        else:
            vocab_dic[vocab_l[i][0:2]] = i

    return vocab_dic

# 6


def p6(s, scale):
    vocab = ""
    vocab_l = []
    s_bigram = []
    v_bigram = []
    s1 = s.replace(" ", "")
    print(s1)

    for i in range(len(s1) - 1):
        s_bigram.append(s1[i:i + scale])

    for j, i in enumerate(s):
        if i == " ":
            vocab_l.append(vocab)
            vocab = ""
        elif (j == len(s) - 1):
            if i == "," or i == "." or i == " ":
                vocab_l.append(vocab)
            else:
                vocab += i
                vocab_l.append(vocab)
        elif i == "," or i == ".":
            continue
        else:
            vocab += i

    for i in range(len(vocab_l) - scale + 1):
        v_bigram.append(vocab_l[i:i + scale])

    return s_bigram, v_bigram

# 7


def p7():
    X = p6("paraparaparadise", 2)[0]
    Y = p6("paragraph", 2)[0]

    # 集合型に変換する
    X, Y = set(X), set(Y)

    return "和集合は" + str(X | Y), "積集合は" + str(X & Y), "差集合は" + str(X ^ Y), "Xは" + str("se" in X) + "です", "Yは" + str("se" in Y) + "です"

# 8


def p8(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

# 9


def p9_encrypt(s):
    # 文字コードはUnicode想定.
    output = ""
    for i in s:
        if 97 <= ord(i) <= 122:
            output += str(219) + str(ord(i))
        else:
            output += i
    return output

# 9


def p9_decrypt(s):
    # 正規表現を使う
    encrypt_list = re.findall("219[9][789]|219[1][012]\d", s)
    for i in encrypt_list:
        s = re.sub(i, chr(int(i[3:])), s)
    return s

# 10


def p10(s):
    vocab_l = p4(s)
    for i, vocab in enumerate(vocab_l):
        if len(vocab) < 5:
            continue
        else:
            vocab_l[i] = vocab.replace(
                vocab[1:-1], "".join(random.sample(vocab[1:-1], len(vocab) - 2)))
    return " ".join(vocab_l)


if __name__ == "__main__":
    print(p1())
    print(p2())
    print(p3())
    print(p4("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
    print(p5())
    print(p6("I am an NLPer", 2))
    print(p7())
    print(p8(12, "気温", 22.4))
    print(p9_encrypt("I am GOD FATHER desu"))
    print(p9_decrypt("I 21997219109 GOD FATHER 219100219101219115219117"))
    print(p10("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))

# 出力例

# desserts
# パトカー
# パタトクカシーー
# ['Now', 'I', 'need', 'a', 'drink', 'alcoholic', 'of', 'course', 'after', 'the', 'heavy', 'lectures', 'involving', 'quantum', 'mechanics']
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# {'Hi': 0, 'H': 1, 'Li': 2, 'Be': 3, 'Bo': 4, 'C': 16, 'N': 9, 'O': 7, 'F': 8, 'Na': 10, 'Mi': 11, 'Al': 12, 'Si': 13, 'Pe': 14, 'S': 15, 'Ar': 17, 'Ki': 18}
# IamanNLPer
# (['Ia', 'am', 'ma', 'an', 'nN', 'NL', 'LP', 'Pe', 'er'], [['I', 'am'], ['am', 'an'], ['an', 'NLPer']])
# paraparaparadise
# paragraph
# ("和集合は{'se', 'pa', 'ar', 'di', 'gr', 'ag', 'is', 'ad', 'ph', 'ap', 'ra'}", "積集合は{'ra', 'ar', 'ap', 'pa'}", "差集合は{'se', 'di', 'ag', 'is', 'ad', 'gr', 'ph'}", 'XはTrueです', 'YはFalseです')
# 12時の気温は22.4
# I 21997219109 GOD FATHER 219100219101219115219117
# I am GOD FATHER desu
# I c'uondlt bvieele that I cloud aallucty unstnedard what I was radieng : the peamneonhl power of the haumn mind
