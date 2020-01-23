import json

path_to_jupyters = '/Users/dankondr/Documents/Jupyters/'
filename = 'IDZ_3_n1.ipynb'
f = open(path_to_jupyters + filename, 'rb')
f_out = open('input.txt', 'w ')

cells = json.load(f)['cells']
for cell in cells:
    out = cell['outputs']
    if len(out) == 0:
        continue
    for line in out[0]['text']:
        f_out.write(line)
    f_out.write("\n")
    # f_out.write(out[0]['text'][0])
