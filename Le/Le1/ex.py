# Another first script!!!

from urllib.request import urlopen

shakespeare = urlopen("http://composingprograms.com/shakespeare.txt")

words = set(shakespeare.read().decode().split())

x = {w for w in words if len(w) > 1 and w[::-1] in words and w != w[::-1]}

print(x)

print("brakpoint before termination")
