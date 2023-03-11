import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

markers = ["o", "*", "x", "+", "s", "d", "|", "1", "2"] #, "_"] #NOT 10 MARKES AS THERE ARE ALSO 10 COLORS

def linear_regression_calc(xvector, yvector):
  npoints = np.size(xvector)
  mean_x = np.mean(xvector)
  mean_y = np.mean(yvector)
  SS_yy = np.sum(yvector*yvector) - npoints*mean_y*mean_y
  SS_xy = np.sum(yvector*xvector) - npoints*mean_x*mean_y
  SS_xx = np.sum(xvector*xvector) - npoints*mean_x*mean_x
  if(SS_xx==0 or SS_yy==0 or npoints<=1): return (mean_y, 0, -0.999) #No meaningful r-value, don't care about b0 and b1 either
  b1 = SS_xy/SS_xx
  b0 = mean_y - b1*mean_x
  resvector = yvector - b0 - b1*xvector
  SS_res = np.sum(resvector*resvector)
  rvalue = 1 - SS_res/SS_yy
  return (b0, b1, rvalue)

df = pd.read_excel("Baseline_ALL_202303.xlsx", sheet_name="ALL")

columns = df.columns
print(columns)
mycolumns = ["Duration [min]", "Humidity [%]", "Air pressure [mb]", "Water temp. [⁰C]", "Air temp. [⁰C]", "Moon illumination"]
Ncolumns = len(mycolumns)

frequencies = df["Frequency [Hz]"].unique()
Nfreqs = len(frequencies)

rvalues = np.zeros([Ncolumns,Nfreqs])

ifield = 0
for field in mycolumns:
  plt.figure()
  ifreq = 0
  print("Working on " + field + " versus frequency...")
  for f in frequencies:
    df_filtered = df[df["Frequency [Hz]"]==f]
    xvector = df_filtered[field]
    yvector = df_filtered["Symm1"]
    plt.plot(xvector, yvector, marker=markers[ifreq % len(markers)], linestyle='None', label='f='+str(f)+' Hz')
    linregrpars = linear_regression_calc(xvector,yvector)
    #print("f = " + str(f) + " Hz -> " + "{:.3f}".format(linregrpars[2]))
    rvalues[ifield][ifreq] = linregrpars[2]
    ifreq += 1
  plt.legend()
  plt.xlabel(field)
  shortfield = field.split(' ')[0]
  titlefield = shortfield
  if(len(field.split(' '))>2):
    titlefield += " " + field.split(' ')[1]
    shortfield += "_" + field.split(' ')[1]
    shortfield = shortfield.replace('.','')
  plt.ylabel("Symmetry-fold")
  plt.title("Symmetry-fold vs " + titlefield + " and Frequency")
  ax = plt.subplot(111)
  box = ax.get_position()
  ax.set_position([box.x0-box.width*0.05,box.y0,box.width*0.92,box.height*1.06])
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  #plt.savefig(shortfield + ".png")
  ifield += 1

plt.figure()
plt.title("Regression r-value versus frequency")
plt.xlabel("Frequency [Hz]")
plt.ylim(0,1.05)
for ifield in range(Ncolumns):
  plt.plot(frequencies, rvalues[ifield, :], marker=markers[ifield % len(markers)], linestyle='None', label=mycolumns[ifield])
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0-box.width*0.05,box.y0,box.width*1.10,box.height*1.06])
ax.legend(loc='center left', bbox_to_anchor=(0.65, 0.8))
plt.savefig("rvalues.png")

#plt.show()