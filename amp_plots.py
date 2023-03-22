import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

markers = ["o", "*", "x", "+", "s", "d", "|", "1", "2"] #, "_"] #NOT 10 MARKES AS THERE ARE ALSO 10 COLORS

df = pd.read_excel("Baseline_ALL_202303.xlsx", sheet_name="ALL")

plt.figure()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.title("Amplitude vs frequency")
xvector = df["Frequency [Hz]"].to_numpy()
yminvec = df["V1Min"].to_numpy()
ymaxvec = df["V1Max"].to_numpy()
#ymaxvec = np.nan_to_num(ymaxvec, nan=-999)
nan_mask = np.isnan(ymaxvec)
ymaxvec[nan_mask] = yminvec[nan_mask]

#plt.boxplot([yminvec, ymaxvec], positions=xvector, widths=0.5, showfliers=False)

#plt.plot(xvector, yminvec, marker="_", linestyle='None', label="")
#plt.plot(xvector, ymaxvec, marker="_", linestyle='None', label="")
plt.xlim(xvector.min()-10, xvector.max()+10)
plt.ylim(yminvec.min()-0.1, ymaxvec.max()+0.1)

for ipoint in range(len(xvector)):
    #plt.vlines(xvector[ipoint], yminvec[ipoint], ymaxvec[ipoint], colors='r', linewidth=4)
    plt.gca().add_patch(Rectangle((xvector[ipoint]-1,yminvec[ipoint]), 2, ymaxvec[ipoint]-yminvec[ipoint], linewidth=1, edgecolor='r', facecolor='none'))
plt.savefig("amplitude_vs_frequency.png")

Symm1vals = sorted(df["Symm1"].unique())
Nsymmvals = len(Symm1vals)

ival = 0
plt.figure()
plt.xlabel("Frequency [Hz]")
plt.ylabel("V1Min")
plt.title("Amplitude vs frequency for each symm-fold")
for Symm1val in Symm1vals:
  print(f"Working on Symm1={Symm1val} versus frequency...")
  df_filtered = df[df["Symm1"]==Symm1val]
  xvector = df_filtered["Frequency [Hz]"]
  yvector = df_filtered["V1Min"]
  plt.plot(xvector, yvector, marker=markers[ival % len(markers)], linestyle='None', label=f"symm={Symm1val}")
  ival += 1
plt.legend()
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("V1min_vs_frequency_by_symm.png")

ival = 0
plt.figure()
plt.xlabel("Frequency [Hz]")
plt.ylabel("V1Max")
plt.title("Amplitude vs frequency for each symm-fold")
for Symm1val in Symm1vals:
  print(f"Working on Symm1={Symm1val} versus frequency...")
  df_filtered = df[df["Symm1"]==Symm1val]
  xvector = df_filtered["Frequency [Hz]"]
  yvector = df_filtered["V1Max"]
  plt.plot(xvector, yvector, marker=markers[ival % len(markers)], linestyle='None', label=f"symm={Symm1val}")
  ival += 1
plt.legend()
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("V1Max_vs_frequency_by_symm.png")