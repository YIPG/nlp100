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
    for i in s:
        if i == " ":
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

def p6(s , scale):
    vocab = ""
    vocab_l = []
    s_bigram=[]
    v_bigram=[]
    for i in range(len(s)):
        for n in scale:
            s_bi = s[i:i+n-1]

        # 単語リスト生成
        if i == " ":
            vocab_l.append(vocab)
            vocab = ""
        elif i == "," or i == ".":
            continue
        else:
            vocab += i



if __name__ == "__main__":
    print(p1())
    print(p2())
    print(p3())
    print(p4())
    print(p5())
