"""
Convert matrix in format:
[[    1     0     3     0    -7]
 [    0     1     3    -3  1840]
 [    0     0     0     0 -3941]
 [    0     0     0     0 10988]]
to:
begin{pmatrix}
1 & 0 & 3 & 0 & \aug & -7 \\
0 & 1 & 3 & -3 & \aug & 1840 \\
0 & 0 & 0 & 0 & \aug & -3941 \\
0 & 0 & 0 & 0 & \aug & 10988 \\
end{pmatrix}
"""

f = open('input.txt', encoding='utf-8')

x = f.readline()
a = []
while x != '':
    x = x[2:-2].split(' ')
    b = []
    for i in range(len(x)):
        if x[i] == '' or x[i] == ' ':
            continue
        else:
            b.append(int(x[i]))
    a.append(b)
    x = f.readline()
RES = 0  # Amount of numbers in answer
print('\\begin{pmatrix}')
for s in a:
    m = len(s) - RES
    for el in s[:RES]:
        print(el, '&', end=' ')
    if RES != 0:
        print('\\aug', end=' ')
    for i in range(RES, len(s)):
        if RES != 0:
            print('&', s[i], end=' ')
        elif i != len(s) - 1:
            print(s[i], '&', end=' ')
        else:
            print(s[i], end=' ')
    print('\\\\')
print('\\end{pmatrix}')
