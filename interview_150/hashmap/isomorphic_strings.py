s = "egg"
t = "add"

"""Beats 97.58% of python3 users on runtime. Beats 28.92% on memory."""


n = len(t)
if len(s) != n:
    print(False)
    raise Exception("Done.")

s_to_t_mapping = {}
t_to_s_mapping = {}

for i in range(n):
    mapped_t = s_to_t_mapping.get(s[i])
    mapped_s = t_to_s_mapping.get(t[i])

    if not mapped_t:
        # s->t mapping doesn't yet exist
        s_to_t_mapping[s[i]] = t[i]
    else:
        if mapped_t != t[i]:
            print(False)
            raise Exception("Done.")

    if not mapped_s:
        # t->s mapping doesn't yet exist
        t_to_s_mapping[t[i]] = s[i]
    else:
        if mapped_s != s[i]:
            print(False)
            raise Exception("Done.")

print(True)
