# 404CTF 2023: Rcette

## The scenario
![[404CTF-2023/crypto/Enonce.png]]

In this challenge we need to do 4 think

First convert the hex string to ascii
With this site : https://www.rapidtables.com/convert/number/hex-to-ascii.html it's really easy 
We get this string `2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o`

Now we need to devellop this tring
like 2i -> ii 4i -> iiii ...

We can make a quick algorithm to do it

```python
b = "2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o"
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
```

Now we need to decode the deadfish string `iisiiiisdddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddoiiiodddddddddddddddoddddddddddddddddddddddoddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiodddddddodddddoiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiododddddddddddddddddddodddddddddddddddddoddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddoiiiiiiiiiiiiiiiiioddddddddddddodddddddoiiiiiododdoiiiiiiiiiiiiodddddddddoddddddddddddddddddddddddddo`

with https://www.dcode.fr/deadfish-language we decode it into ASCII characters

We get this string : `1b^aR<(;4/1hgTC1NZtl1LFWKDIHFRI/`

Now we need to decode it with base85

```bash
tlyx@InspironNeon:~$ echo "1b^aR<(;4/1hgTC1NZtl1LFWKDIHFRI/" | base85 --decode
404CTF{M4igr3t_D3_c4naRd}
```

And there is the flag !

## Flag
``404CTF{M4igr3t_D3_c4naRd}``