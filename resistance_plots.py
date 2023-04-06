import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.stats import linregress
import numpy as np

markers = ["o", "*", "^", "v", "s", "d", ">", "<", "h"] #, "_"] #NOT 10 MARKES AS THERE ARE ALSO 10 COLORS

df = pd.read_excel("cymatics_ez_water_experiment_ALL.xlsx", sheet_name="Sheet1")

df = df.sort_values(by=["Frequency [Hz]"])

ival = 0
plt.figure()
plt.xlabel("Resistance before, SZ - EZ diff. [MΩ]")
plt.ylabel("Symmetry fold")
plt.title("Symm-fold versus resistance difference")
for freq in df["Frequency [Hz]"].unique():
  print(f"Working on f={freq}...")
  df_filtered = df[df["Frequency [Hz]"]==freq]
  R1 = df_filtered["Res. before SZ [MΩ]"].to_numpy()
  R2 = df_filtered["Res. before EZ [MΩ]"].to_numpy()
  symm_filt = df_filtered["Symm1"]
  plt.plot(R1-R2, symm_filt, marker=markers[ival % len(markers)], linestyle='None', label=f"f={freq} Hz")
  ival += 1
plt.legend()
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("RBefSZEZ.png")

ival = 0
plt.figure()
plt.xlabel("Resistance after, SZ - EZ diff. [MΩ]")
plt.ylabel("Symmetry fold")
plt.title("Symm-fold versus resistance difference")
for freq in df["Frequency [Hz]"].unique():
  print(f"Working on f={freq}...")
  df_filtered = df[df["Frequency [Hz]"]==freq]
  R1 = df_filtered["Res. after SZ [MΩ]"].to_numpy()
  R2 = df_filtered["Res. after EZ [MΩ]"].to_numpy()
  symm_filt = df_filtered["Symm1"]
  plt.plot(R1-R2, symm_filt, marker=markers[ival % len(markers)], linestyle='None', label=f"f={freq} Hz")
  ival += 1
plt.legend()
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("RAftSZEZ.png")

ival = 0
plt.figure()
plt.xlabel("EZ resistance after - before diff. [MΩ]")
plt.ylabel("Symmetry fold")
plt.title("Symm-fold versus resistance difference")
for freq in df["Frequency [Hz]"].unique():
  print(f"Working on f={freq}...")
  df_filtered = df[df["Frequency [Hz]"]==freq]
  R1 = df_filtered["Res. after EZ [MΩ]"].to_numpy()
  R2 = df_filtered["Res. before EZ [MΩ]"].to_numpy()
  symm_filt = df_filtered["Symm1"]
  plt.plot(R1-R2, symm_filt, marker=markers[ival % len(markers)], linestyle='None', label=f"f={freq} Hz")
  ival += 1
plt.legend()
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("REZAftBef.png")

ival = 0
plt.figure()
plt.xlabel("SZ resistance after - before diff. [MΩ]")
plt.ylabel("Symmetry fold")
plt.title("Symm-fold versus resistance difference")
for freq in df["Frequency [Hz]"].unique():
  print(f"Working on f={freq}...")
  df_filtered = df[df["Frequency [Hz]"]==freq]
  R1 = df_filtered["Res. after SZ [MΩ]"].to_numpy()
  R2 = df_filtered["Res. before SZ [MΩ]"].to_numpy()
  symm_filt = df_filtered["Symm1"]
  plt.plot(R1-R2, symm_filt, marker=markers[ival % len(markers)], linestyle='None', label=f"f={freq} Hz")
  ival += 1
plt.legend()
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("RSZAftBef.png")
