# Cymatics
In this cymatics project library resonance patterns are analyzed versius various parameters. 
## Contents
- <a href="https://github.com/csanadm/cymatics/blob/main/analyze.py">analyze.py</a>: analyzing an Excel file with `DataFrame` (from `pandas`), by investigating dependence of the symmetry-fold on the parameters, and doing a linear regression to see r-values.
- <a href="https://github.com/csanadm/cymatics/blob/main/fit.py">fit.py</a>: perform an actual fit with `lmfit`, to see if there is a linear form based on the parameters that successfully predicts the symmetry-fold.
- <a href="https://github.com/csanadm/cymatics/blob/main/linreg_scikit.py">linreg_scikit.py</a>: perform ML-based linear regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/svr_scikit.py">svr_scikit.py</a>: perform Support Vector Regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/frequency_plot.py">frequency_plot.py</a>: Plot symmetry-fold vs frequency in various groupings.
- <a href="https://github.com/csanadm/cymatics/blob/main/amp_plots.py">amp_plots.py</a>: Plot amplitudes vs frequency in various groupings.

Here is an example output for the SVR code:
![svr_scikit](https://user-images.githubusercontent.com/38218165/225572229-496f2b5a-cd59-49ed-859b-f907a83b351b.png)

Here is an amplitude vs frequency plot:
![amplitude_vs_frequency](https://user-images.githubusercontent.com/38218165/226633584-140a9453-701e-43c8-b66d-0e3a9e493c3e.png)

And the amplitudes vs frequency, grouped by symmetryfold:
![V1min_vs_frequency_by_symm](https://user-images.githubusercontent.com/38218165/226633683-6bf20da3-9bf8-4ac3-8422-e44c51e07c87.png)
![V1Max_vs_frequency_by_symm](https://user-images.githubusercontent.com/38218165/226633674-ce7b1f56-1a13-4283-b80b-3cb1a044974a.png)
