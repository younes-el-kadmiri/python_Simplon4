dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5}

fusion = dict1.copy()
fusion.update(dict2)
fusion.update(dict3)

print("Dictionnaire fusionne :", fusion)
