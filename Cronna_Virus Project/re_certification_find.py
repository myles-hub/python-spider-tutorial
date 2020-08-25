import re
import json

zs_lst = []

with open("data/1.txt", encoding='utf-8') as fp:
    lines = fp.readlines()
    for line in lines:
        zs = re.findall(r"《.+》", line)
        # print(zs)
        if zs:
            zs_lst.append(zs[0])
    # print(zs_lst)
    zs_set = list(set(zs_lst))
    # print(len(zs_set))

with open("data/zs-1.txt", 'w', encoding='utf-8') as fp:
    for zs in zs_set:
        fp.write(zs+'\n')