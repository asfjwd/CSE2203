import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FormatStrFormatter

def nonpolar(dat):
  x = [i for i in range(len(dat) + 1)]
  y = [0] + dat
  return x, y

def nrzL(dat):
  x = [i for i in range(len(dat) + 1)]
  y = [-1] + [-1 if i == 0 else 1 for i in dat]
  return x, y

def nrzI(dat):
  x = [i for i in range(len(dat) + 1)]
  choice = [1, -1]
  prev = 0
  y = [1]
  for d in dat:
    if d == 1:
      prev = prev ^ 1
    y.append(choice[prev])
  return x, y

def rz(dat):
  x = [i/2 for i in range(0, 2 * len(dat) + 1)]
  y = [0]
  for d in dat:
    if(d == 1):
      y.append(1)
    else:
      y.append(-1)
    y.append(0)
  return x, y

def manchester(dat):
  x = [i/2 for i in range(0, 2 * len(dat) + 1)]
  y = [1]
  for d in dat:
    if(d == 1):
      y.append(-1)
      y.append(1)
    else:
      y.append(1)
      y.append(-1)
  return x, y

def diffenrialManchester(dat):
  x = [i/2 for i in range(0, 2 * len(dat) + 1)]
  choice = [1, -1]
  y = [1]
  prev = 0
  for d in dat:
    if d == 0:
      prev = prev ^ 1
    y.append(choice[prev])
    prev = prev ^ 1
    y.append(choice[prev])
  return x, y

def ami(dat):
  x = [i for i in range(len(dat) + 1)]
  y = [0]
  nxt = 1
  for d in dat:
    if d == 1:
      y.append(nxt)
      nxt = nxt * -1;
    else:
      y.append(0)
  return x, y

def pseudoternary(dat):
  x = [i for i in range(len(dat) + 1)]
  y = [-1]
  nxt = 1
  for d in dat:
    if d == 0:
      y.append(nxt)
      nxt = nxt * -1;
    else:
      y.append(0)
  return x, y

def mlt3(dat):
  x = [i for i in range(len(dat) + 1)]
  y = [0]
  now = 0
  lastNonZero = -1
  for d in dat:
    if d == 0:
      y.append(now)
    else :
      if now:
        now = 0
        y.append(now)
      else:
        if lastNonZero == -1:
          now = 1
        else:
          now = -1
        y.append(now)
        lastNonZero = now
  return x, y

raw_data = input("Enter data = ")
data = [int(x) for x in raw_data]

# plt.style.use('ggplot')

fig = plt.figure(figsize=(12, 14))
plt.subplots_adjust(hspace = 0.35)


ax1 = plt.subplot(911)
ax1.set_title('Data = '+ raw_data, y = 1.5)
ax1.xaxis.set_label_coords(0.5, -0.1)
ax1.set_xlabel('Unipolar')
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax1.set_ylim(-0.25, 1.25)
ax1.set_xlim(xmin=-0.005)
ax1.set_ymargin(0.4)
ax1.set_xmargin(0.0)
x, y = nonpolar(data)
ax1.set_xticks(list(filter(lambda b: b == int(b), x)))
ax1.set_xticklabels([])
ax1.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax1.text(pos + 0.5, 0.5, bit)


ax2 = plt.subplot(912)
ax2.xaxis.set_label_coords(0.5, -0.1)
ax2.set_xlabel('NRZ-L')
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlim(xmin=-0.005)
ax2.set_ymargin(0.4)
ax2.set_xmargin(0.0)
x, y = nrzL(data)
ax2.set_xticks(list(filter(lambda b: b == int(b), x)))
ax2.set_xticklabels([])
ax2.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax2.text(pos + 0.5, 0, bit)

ax3 = plt.subplot(913)
ax3.xaxis.set_label_coords(0.5, -0.1)
ax3.set_xlabel('NRZ-I')
ax3.yaxis.set_major_locator(MaxNLocator(integer=True))
ax3.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax3.set_ylim(-1.5, 1.5)
ax3.set_xlim(xmin=-0.005)
ax3.set_ymargin(0.4)
ax3.set_xmargin(0.0)
x, y = nrzI(data)
ax3.set_xticks(list(filter(lambda b: b == int(b), x)))
ax3.set_xticklabels([])
ax3.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax3.text(pos + 0.5, 0, bit)

ax4 = plt.subplot(914)
ax4.xaxis.set_label_coords(0.5, -0.1)
ax4.set_xlabel('Polar RZ')
ax4.yaxis.set_major_locator(MaxNLocator(integer=True))
ax4.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax4.set_ylim(-1.5, 1.5)
ax4.set_xlim(xmin=-0.005)
ax4.set_ymargin(0.4)
ax4.set_xmargin(0.0)
x, y = rz(data)
ax4.set_xticks(list(filter(lambda b: b == int(b), x)))
ax4.set_xticklabels([])
ax4.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax4.text(pos + 0.5, 0.75 if bit == 0 else -0.75, bit)

ax5 = plt.subplot(915)
ax5.xaxis.set_label_coords(0.5, -0.1)
ax5.set_xlabel('Manchester')
ax5.yaxis.set_major_locator(MaxNLocator(integer=True))
ax5.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax5.set_ylim(-1.5, 1.5)
ax5.set_xlim(xmin=-0.005)
ax5.set_ymargin(0.4)
ax5.set_xmargin(0.0)
x, y = manchester(data)
ax5.set_xticks(list(filter(lambda b: b == int(b), x)))
ax5.set_xticklabels([])
ax5.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax5.text(pos + 0.6, 0, bit)

ax6 = plt.subplot(916)
ax6.xaxis.set_label_coords(0.5, -0.1)
ax6.set_xlabel('Differential Manchester')
ax6.yaxis.set_major_locator(MaxNLocator(integer=True))
ax6.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax6.set_ylim(-1.5, 1.5)
ax6.set_xlim(xmin=-0.005)
ax6.set_ymargin(0.4)
ax6.set_xmargin(0.0)
x, y = diffenrialManchester(data)
ax6.set_xticks(list(filter(lambda b: b == int(b), x)))
ax6.set_xticklabels([])
ax6.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax6.text(pos + 0.6, 0, bit)

ax7 = plt.subplot(917)
ax7.xaxis.set_label_coords(0.5, -0.1)
ax7.set_xlabel('AMI')
ax7.yaxis.set_major_locator(MaxNLocator(integer=True))
ax7.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax7.set_ylim(-1.5, 1.5)
ax7.set_xlim(xmin=-0.005)
ax7.set_ymargin(0.4)
ax7.set_xmargin(0.0)
x, y = ami(data)
ax7.set_xticks(list(filter(lambda b: b == int(b), x)))
ax7.set_xticklabels([])
ax7.step(x, y, color = '#9367bd', linewidth=2.0)
for pos, bit in enumerate(data):
  ax7.text(pos + 0.5, 0 if bit == 1 else 0.25, bit)

ax8 = plt.subplot(918)
ax8.xaxis.set_label_coords(0.5, -0.1)
ax8.set_xlabel('Pseudoternary')
ax8.yaxis.set_major_locator(MaxNLocator(integer=True))
ax8.yaxis.set_major_formatter(FormatStrFormatter('%d V'))
ax8.set_ylim(-1.5, 1.5)
ax8.set_xlim(xmin=-0.005)
ax8.set_ymargin(0.4)
ax8.set_xmargin(0.0)
x, y = pseudoternary(data)
ax8.set_xticks(list(filter(lambda b: b == int(b), x)))
ax8.set_xticklabels([])
ax8.step(x, y, color = '#9367bd', linewidth=2.0, zorder = 1)
for pos, bit in enumerate(data):
  ax8.text(pos + 0.5, 0 if bit == 0 else 0.25, bit)

ax9 = plt.subplot(919)
ax9.xaxis.set_label_coords(0.5, -0.1)
ax9.set_xlabel('MLT-3')
ax9.yaxis.set_major_locator(MaxNLocator(integer=True))
ax9.set_ylim(-1.5, 1.5)
ax9.set_xlim(xmin=-0.005)
ax9.set_ymargin(0.4)
ax9.set_xmargin(0.0)
x, y = mlt3(data)
ax9.set_xticks(list(filter(lambda b: b == int(b), x)))
ax9.set_xticklabels([])
ax9.set_yticks([-1, 0, 1])
ax9.set_yticklabels([' -V', '0 V', ' +V'])
ax9.step(x, y, color = '#9367bd', linewidth=2.0, zorder = 1)
for pos, bit in enumerate(data):
  ax9.text(pos + 0.5, 0 if bit == 1 else 0.25, bit)

plt.show()
# plt.savefig('signal.png')