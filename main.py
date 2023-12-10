itms = [
    {"n": "r", "s": 3, "sp": 25},
    {"n": "m", "s": 2, "sp": 20},
    {"n": "a", "s": 1, "sp": 10},
    {"n": "t", "s": 1, "sp": 25},
    {"n": "ax", "s": 3, "sp": 20},
    {"n": "p", "s": 2, "sp": 15},
    {"n": "am", "s": 2, "sp": 15},
    {"n": "k", "s": 1, "sp": 15},
    {"n": "s", "s": 2, "sp": 20},
    {"n": "f", "s": 1, "sp": 15},
    {"n": "c", "s": 2, "sp": 20},
    {"n": "i", "s": 1, "sp": 5}
]

itms_srt = sorted(itms, key=lambda x: x["sp"], reverse=True)

bw = 3
bh = 3

p_itms = []
rs = bw * bh

for itm in itms_srt:
    if itm["n"] == "i":
        if itm["s"] <= rs:
            p_itms.append(itm["n"])
            rs -= itm["s"]

for itm in itms_srt:
    if itm["n"] not in p_itms and itm["n"] != "i":
        if itm["s"] <= rs:
            p_itms.append(itm["n"])
            rs -= itm["s"]

print("Упакованные предметы:", p_itms)
t_sp = sum(itm["sp"] for itm in itms_srt if itm["n"] in p_itms)
print("Итоговые очки выживания:", t_sp)   