import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FormatStrFormatter

def B8ZS(dat):
  x = [i for i in range(len(dat) + 1)]
  y = [0]
  pos = []
  i = 0

  lastNonZero = 0 #(0, 1) -> last non zero level was (-ve, +ve)
  nonZeroParity = 0
  opt = [ [[1, 0, 0, 1], [0, 0, 0, -1]], [[-1, 0, 0, -1], [0, 0, 0, 1]] ]
  while i < len(dat):
    if dat[i]:
      y.append(-1 if lastNonZero else 1)
      nonZeroParity = nonZeroParity ^ 1
      lastNonZero = lastNonZero ^ 1;
      i = i + 1
    else:
      if i + 4 <= len(dat) and all(v == 0 for v in dat[i:i+4]):
        pos.append((i, i + 4))
        y = y + opt[lastNonZero][nonZeroParity]
        if nonZeroParity == 0:
          lastNonZero = lastNonZero ^ 1
        else :
          nonZeroParity = 0
        i = i + 4
      else:
        y.append(0)
        i = i + 1
  return x, y, pos

colors = ['#17bdcf', '#d62727']

raw_data = input("Enter data = ")
data = [int(x) for x in raw_data]

plt.figure(figsize=(7, 3))
ax = plt.subplot(111)
ax.axhline(0, color='k', alpha = 0.3)
ax.grid(axis='x', linestyle='--')
ax.xaxis.set_label_coords(0.5, -0.05)
ax.set_xlabel('HDB3')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(xmin=-0.030)
ax.set_ymargin(0.4)
ax.set_xmargin(0.0)
x, y, pos = B8ZS(data)
# print(pos)
c = 0
for p in pos:
  plt.axvspan(p[0], p[1], color=colors[c], alpha=0.2)
  c = c ^ 1
ax.set_xticks(list(filter(lambda b: b == int(b), x)))
ax.set_xticklabels([])
ax.step(x, y, color = '#9367bd', linewidth=3.0)
for pos, bit in enumerate(data):
  ax.text(pos + 0.5, 0.5, bit)

plt.show()
# plt.savefig('P4-14 (HDB3).png')