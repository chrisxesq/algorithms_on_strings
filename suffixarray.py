# python3
text='abaab$'


def sort_characters(text):
    res_order = [0] * len(text)
    char_set = sorted(set(text))
    count = [text.count(c) for c in char_set]

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i, c in reversed(list(enumerate(text))):
        #print(i,c,char_set.index(c),count[char_set.index(c)])
        count[char_set.index(c)] -= 1
        res_order[count[char_set.index(c)]] = i

    return res_order

def compute_char_classes(text, order):
    clss = [0] * len(text)

    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            clss[order[i]] = clss[order[i - 1]] + 1
        else:
            clss[order[i]] = clss[order[i - 1]]

    return clss

def sort_doubled(text, l, order, clss):
    len_text = len(text)
    count = [0] * len_text
    new_order = [0] * len_text

    for i in range(len_text):
        count[clss[i]] += 1
    for j in range(1, len_text):
        count[j] += count[j - 1]

    for i in range(len_text - 1, -1, -1):
        start = (order[i] - l + len_text) % len_text
        cl = clss[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order

def update_classes(new_order, clss, l):
    n = len(new_order)
    new_clss = [0] * n

    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = cur + l, (prev + l) % n
        if clss[cur] != clss[prev] or clss[mid] != clss[mid_prev]:
            new_clss[cur] = new_clss[prev] + 1
        else:
            new_clss[cur] = new_clss[prev]

    return new_clss


def build_suffix_array(text):
    order = sort_characters(text)
    clss = compute_char_classes(text, order)
    length = 1
    len_text = len(text)

    while length < len_text:
        order = sort_doubled(text, length, order, clss)
        clss = update_classes(order, clss, length)
        length = length * 2

    return order
print(build_suffix_array(text))
