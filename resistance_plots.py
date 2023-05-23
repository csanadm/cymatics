import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.stats import linregress
import numpy as np

markers = ["o", "*", "^", "v", "s", "d", ">", "<", "h"] #, "_"] #NOT 10 MARKES AS THERE ARE ALSO 10 COLORS

def linear_regression_calc(xvector, yvector):
  npoints = np.size(xvector)
  mean_x = np.mean(xvector)
  mean_y = np.mean(yvector)
  SS_yy = np.sum(yvector*yvector) - npoints*mean_y*mean_y
  SS_xy = np.sum(yvector*xvector) - npoints*mean_x*mean_y
  SS_xx = np.sum(xvector*xvector) - npoints*mean_x*mean_x
  if(SS_xx==0 or SS_yy==0 or npoints<=2): return (mean_y, 0, -0.999) #No meaningful r-value, don't care about b0 and b1 either
  b1 = SS_xy/SS_xx
  b0 = mean_y - b1*mean_x
  resvector = yvector - b0 - b1*xvector
  SS_res = np.sum(resvector*resvector)
  rvalue = 1 - SS_res/SS_yy
  #if(rvalue>0.5):
  #  print(xvector)
  #  print(yvector)
  return (b0, b1, rvalue)

def one_resinstance_diff_plot(xlabel, ylabel, title, groupby, shortgroup, groupunit, R1name, R2name, xvariable, plotname):
  ival = 0
  plt.figure()
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  for groupvar in df[groupby].unique():
    df_filtered = df[df[groupby]==groupvar]
    R = df_filtered[R1name].to_numpy()
    if(R2name != ""): R -= df_filtered[R2name].to_numpy()
    xvar_filtered = df_filtered[xvariable]
    plt.plot(R, xvar_filtered, marker=markers[ival % len(markers)], linestyle='None', label=(shortgroup + "=" + str(groupvar) + groupunit))
    print(str(groupvar) + " -> " + str(linear_regression_calc(R, xvar_filtered)[2]))
    ival += 1
  plt.legend()
  ax = plt.subplot(111)
  box = ax.get_position()
  ax.set_position([box.x0-box.width*0.03,box.y0,box.width*0.91,box.height*1.06])
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.savefig(plotname)

df = pd.read_excel("cymatics_ez_water_experiment_ALL.xlsx", sheet_name="Sheet1")
df = df[~df['Symm1'].isna()] # Remove lines with empty Symm1

#####################################################################
############### DIFFERENCES VERSUS SYMMETRY-FOLD ####################
#####################################################################

df = df.sort_values(by=["Frequency [Hz]"])

one_resinstance_diff_plot("Resistance before, SZ - EZ diff. [MΩ]",  "Symmetry fold", "Symm-fold versus resistance difference", "Frequency [Hz]", "f", " Hz", "Res. before SZ [MΩ]", "Res. before EZ [MΩ]", "Symm1", "RBefSZEZ.png")
one_resinstance_diff_plot("Resistance after, SZ - EZ diff. [MΩ]",   "Symmetry fold", "Symm-fold versus resistance difference", "Frequency [Hz]", "f", " Hz", "Res. after SZ [MΩ]",  "Res. after EZ [MΩ]",  "Symm1", "RAftSZEZ.png")
one_resinstance_diff_plot("EZ resistance after - before diff. [MΩ]","Symmetry fold", "Symm-fold versus resistance difference", "Frequency [Hz]", "f", " Hz", "Res. after EZ [MΩ]",  "Res. before EZ [MΩ]", "Symm1", "REZAftBef.png")
one_resinstance_diff_plot("SZ resistance after - before diff. [MΩ]","Symmetry fold", "Symm-fold versus resistance difference", "Frequency [Hz]", "f", " Hz", "Res. after SZ [MΩ]",  "Res. before SZ [MΩ]", "Symm1", "RSZAftBef.png")


#####################################################################
############### SINGLE VALUES VERSUS SYMMETRY-FOLD ##################
#####################################################################

df = df.sort_values(by=["Frequency [Hz]"])

one_resinstance_diff_plot("Resistance before, SZ [MΩ]", "Symmetry fold", "Symm-fold versus resistance", "Frequency [Hz]", "f", " Hz", "Res. before SZ [MΩ]", "", "Symm1", "RBefSZ.png")
one_resinstance_diff_plot("Resistance after, SZ [MΩ]",  "Symmetry fold", "Symm-fold versus resistance", "Frequency [Hz]", "f", " Hz", "Res. after SZ [MΩ]",  "", "Symm1", "RAftSZ.png")
one_resinstance_diff_plot("Resistance before, EZ [MΩ]", "Symmetry fold", "Symm-fold versus resistance", "Frequency [Hz]", "f", " Hz", "Res. before EZ [MΩ]", "", "Symm1", "RBefEZ.png")
one_resinstance_diff_plot("Resistance after, EZ [MΩ]",  "Symmetry fold", "Symm-fold versus resistance", "Frequency [Hz]", "f", " Hz", "Res. after EZ [MΩ]",  "", "Symm1", "RAftEZ.png")

#####################################################################
################## DIFFERENCES VERSUS FREQUENCY #####################
#####################################################################

df = df.sort_values(by=["Symm1"])

one_resinstance_diff_plot("Resistance before, SZ - EZ diff. [MΩ]",  "Frequency [Hz]", "Frequency versus resistance difference", "Symm1", "symm", "", "Res. before SZ [MΩ]", "Res. before EZ [MΩ]", "Frequency [Hz]", "RBefSZEZ_vs_f.png")
one_resinstance_diff_plot("Resistance after, SZ - EZ diff. [MΩ]",   "Frequency [Hz]", "Frequency versus resistance difference", "Symm1", "symm", "", "Res. after SZ [MΩ]",  "Res. after EZ [MΩ]",  "Frequency [Hz]", "RAftSZEZ_vs_f.png")
one_resinstance_diff_plot("EZ resistance after - before diff. [MΩ]","Frequency [Hz]", "Frequency versus resistance difference", "Symm1", "symm", "", "Res. after EZ [MΩ]",  "Res. before EZ [MΩ]", "Frequency [Hz]", "REZAftBef_vs_f.png")
one_resinstance_diff_plot("SZ resistance after - before diff. [MΩ]","Frequency [Hz]", "Frequency versus resistance difference", "Symm1", "symm", "", "Res. after SZ [MΩ]",  "Res. before SZ [MΩ]", "Frequency [Hz]", "RSZAftBef_vs_f.png")