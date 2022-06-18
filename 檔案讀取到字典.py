file = open("names.txt", mode="w")
file.write('''411071112 陳仰玟
411071114 陸新玫
411071115 陳晏樺
411071116 鄧蘭茂
411071118 賴怡潔
411071120 朱京念
411071122 李苑旭
411071124 李政宏
411071125 林承翰
411071126 許亦禮''')
file = open("names.txt", mode="r")
print(file.read())
a = {}
with open("names.txt") as f:
  for line in f:
    (k, v) = line.split()
    a[int(k)] = v
print(a)