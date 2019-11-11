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
for line in f:
    if not started:
        started = True
        out.write('\\begin{pmatrix}\n')
    if line == '\n':
        out.write('\\end{pmatrix}\n')
        out.write('\\implies\n')
        started = False
        continue
    line = line.replace('[', ' ')
    line = line.replace(']', ' ')
    line = line.split()
    print(line)
    out.write(matrix_to_TeX(line) + '\n')
out.write('\\end{pmatrix}\n')
