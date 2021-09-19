list1 = ["b", "c"]
dict1 = {"b":1, "c":2, "d":3}
keys = list(dict1.keys())

# list1とdict1の一致要素
test1 = [l1 for l1 in list1 if l1 in keys]
print(test1)

test1plus = list(set(list1) & set(keys))
print(test1plus)

# list1にあってdict1にない要素
test2 = [l1 for l1 in list1 if l1 not in keys]
print(test2)

test2plus = list(set(list1) - set(keys))
print(test2plus)

# dict1にあってlist1にない要素
test3 = [d1 for d1 in keys if d1 not in list1]
print(test3)

test3plus = list(set(keys) - set(list1))
print(test3plus)

for i in test3:
    # listが空だとfor以下の処理が実行されない。
    if i:
        print(i)
    else:
        print("not exist")