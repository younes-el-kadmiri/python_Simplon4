d = {"a": 3, "b": 1, "c": 5, "d": 2}
d_trie = dict(sorted(d.items(), key=lambda item: item[1]))
print("Dictionnaire trié par valeur :", d_trie)
