# Cymatics
In this cymatics project library resonance patterns are analyzed versius various parameters. 
## Contents
- <a href="https://github.com/csanadm/cymatics/blob/main/analyze.py">analyze.py</a>: analyzing an Excel file with `DataFrame` (from `pandas`), by investigating dependence of the symmetry-fold on the parameters, and doing a linear regression to see r-values.
- <a href="https://github.com/csanadm/cymatics/blob/main/fit.py">fit.py</a>: perform an actual fit with `lmfit`, to see if there is a linear form based on the parameters that successfully predicts the symmetry-fold.
- <a href="https://github.com/csanadm/cymatics/blob/main/linreg_scikit.py">linreg_scikit.py</a>: perform ML-based linear regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/svr_scikit.py">svr_scikit.py</a>: perform Support Vector Regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/frequency_plot.py">frequency_plot.py</a>: Plot symmetry-fold vs frequency in various groupings.
- <a href="https://github.com/csanadm/cymatics/blob/main/amp_plots.py">amp_plots.py</a>: Plot amplitudes vs frequency in various groupings.
- <a href="https://github.com/csanadm/cymatics/blob/main/resistance_plots.py">resistance_plots.py</a>: Plot symmetryfold vs resistance in various groupings.

Here is an example plot for the linear fit (two methods: lmfit and scikit/sklearn):

<img alt="fit_residuals" src="https://user-images.githubusercontent.com/38218165/232236561-4d180456-c91a-4e3a-855f-806b7bbf5dcd.png" width="350" /> <img alt="ML_fit_residuals" src="https://user-images.githubusercontent.com/38218165/232236617-15a0535a-f31b-47df-8f22-746e21f05230.png" width="350" />

Here is an example output for the SVR code:

<img alt="scikit_RBF" src="https://user-images.githubusercontent.com/38218165/232236734-217e7816-9af9-46a9-b806-e4feb8756a96.png" width="350" />

Here is an amplitude vs frequency plot, showing boxes from amplitude minimum to amplitude maximum, at each frequency:

<img alt="amplitude_vs_frequency" src="https://user-images.githubusercontent.com/38218165/232236888-b2bc9a55-72f8-4d28-adc8-847ee231c6dd.png" width="350" />

And the amplitudes vs frequency, grouped by symmetryfold:

<img alt="V1min_vs_frequency_by_symm" src="https://user-images.githubusercontent.com/38218165/232236981-8fc7a6e6-aeaf-46fe-b244-7036b53c1fcf.png" width="350" /><img alt="V1Max_vs_frequency_by_symm" src="https://user-images.githubusercontent.com/38218165/232236974-7d01fa1c-0bf3-40e2-996c-9867a5a7b63c.png" width="350" />
