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


def matrix_to_TeX(line):
    s = line[0] + ' '
    for i in range(1, len(line) - RES):
        s += '& ' + line[i] + ' '
    if RES != 0:
        s += '& \\aug '
    for i in range(len(line) - RES, len(line)):
        s += '& ' + line[i] + ' '
    s += '\\\\'
    return s


f = open('input.txt', encoding='utf-8')
out = open('output.txt', 'w+', encoding='utf-8')
RES = int(input())  # Amount of numbers in answer

started = False
c = 1
first = True
for line in f:
    if not started:
        started = True
        s = '\\[\n' if c % 2 != 0 else ''
        if not first and c % 2 != 0:
            s += '\\implies\n'
        else:
            first = False
        s += '\\begin{pmatrix}\n'
        out.write(s)
    if line == '\n':
        out.write('\\end{pmatrix}\n')
        out.write('\\implies\n')
        if c % 2 == 0:
            out.write('\\]\n')
        started = False
        c += 1
        continue
    line = line.replace('[', ' ')
    line = line.replace(']', ' ')
    line = line.split()
    out.write(matrix_to_TeX(line) + '\n')
out.write('\\end{pmatrix}\n\\]')
