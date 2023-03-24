import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from lmfit import minimize, Parameters, Parameter, fit_report, report_fit

def mychi2fun(params, df, columns):
    values = np.array(list(params.valuesdict().values()))
    residuals = df.apply(lambda row: (np.dot(values, np.nan_to_num(row[columns],nan=0)) - row['Symm1'])**2, axis=1)
    return residuals
  

df = pd.read_excel("Baseline_ALL_202303.xlsx", sheet_name="ALL")

#columns = df.columns
#print(columns)
#yvector = df["Symm1"]
#Nrows = len(yvector)
mycolumns = ["Duration [min]", "Humidity [%]", "Air pressure [mb]", "Water temp. [⁰C]", "Air temp. [⁰C]", "Moon illumination", "V1Min", "V1Max", "V2Min", "V2Max", "V3Min", "V3Max"]
Ncolumns = len(mycolumns)

params = Parameters()
for field in mycolumns:
  paramname = field.split(' ')[0]
  if(len(field.split(' '))>2):
    paramname += "_" + field.split(' ')[1]
  paramname = paramname.replace('.','')
  paramname += "_multiplier"
  params.add(paramname, value = 0.0)
params.pretty_print()

result = minimize(mychi2fun, params, args=(df,mycolumns,), method='leastsq')
result.params.pretty_print()

print("fcncalls = %i"      % (result.nfev))
print("chi2 = %.3e"        % (result.chisqr))
print("NDF = %i - %i = %i" % (result.ndata,result.nvarys,result.ndata-result.nvarys))
for name in params.keys():
  print("%s = %f +- %f"       % (name, float(result.params[name].value), float(result.params[name].stderr)))

for index, row in df.iterrows():
  meas = row['Symm1']
  calc = np.dot(np.array(list(params.valuesdict().values())), row[mycolumns])
  resid = meas - calc
  chi2 = resid**2
  print("%i:   %.2f  ---   %i    (resid = %.2f, chi2 = %.2f)" % (index, calc, meas, resid, chi2))
  