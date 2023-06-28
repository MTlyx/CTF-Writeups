b = "2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o"

print(b)

c = ""
lettre = ["i","d","s","o"]
passage = 0
nombre = 0
for i in range(len(b)):
    if b[i] not in lettre:
        if passage > 0:
            nombre *= 10
            nombre += int(b[i])
            passage += 1
        else:
            nombre += int(b[i])
            passage += 1
    else:
        c += b[i]*nombre
        nombre = 0
        passage = 0

print(c)