# 1章

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


def p4():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
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
            if i == "," or i == "." or i ==" ":
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



if __name__ == "__main__":
    print(p1())
    print(p2())
    print(p3())
    print(p4())
    print(p5())
    print(p6("I am an NLPer", 2))
