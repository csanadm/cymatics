# Cymatics
In this cymatics project library resonance patterns are analyzed versius various parameters. 
## Contents
- <a href="https://github.com/csanadm/cymatics/blob/main/analyze.py">analyze.py</a>: analyzing an Excel file with `DataFrame` (from `pandas`), by investigating dependence of the symmetry-fold on the parameters, and doing a linear regression to see r-values.
- <a href="https://github.com/csanadm/cymatics/blob/main/fit.py">fit.py</a>: perform an actual fit with `lmfit`, to see if there is a linear form based on the parameters that successfully predicts the symmetry-fold.
- <a href="https://github.com/csanadm/cymatics/blob/main/linreg_scikit.py">linreg_scikit.py</a>: perform ML-based linear regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/svr_scikit.py">svr_scikit.py</a>: perform Support Vector Regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/frequency_plot.py">frequency_plot.py</a>: Plot symmetry-fold vs frequency in various groupings.
- <a href="https://github.com/csanadm/cymatics/blob/main/amp_plots.py">amp_plots.py</a>: Plot amplitudes vs frequency in various groupings.

Here is an example plot for the linear fit (lmfit and scikit/sklearn):

<img alt="fit_residuals" src="https://user-images.githubusercontent.com/38218165/227724923-651c4013-a6cc-49ba-a7bf-9f7509f97b6b.png" width="350" /> <img alt="ML_fit_residuals" src="https://user-images.githubusercontent.com/38218165/227726975-b2a0ca6d-c78b-4fac-83dc-a0323db4f3ef.png" width="350" />

Here is an example output for the SVR code:

<img alt="svr_scikit" src="https://user-images.githubusercontent.com/38218165/225572229-496f2b5a-cd59-49ed-859b-f907a83b351b.png" width="700" />

Here is an amplitude vs frequency plot, showing boxes from amplitude minimum to amplitude maximum, at each frequency:

<img alt="amplitude_vs_frequency" src="https://user-images.githubusercontent.com/38218165/227138238-6a8ba41e-3ca7-4b22-b6bb-887d5983582b.png" width="350" />

And the amplitudes vs frequency, grouped by symmetryfold:

<img alt="V1min_vs_frequency_by_symm" src="https://user-images.githubusercontent.com/38218165/227894988-408af57a-7562-44aa-98d2-47b844241b7c.png" width="350" /><img alt="V1Max_vs_frequency_by_symm" src="https://user-images.githubusercontent.com/38218165/227894993-61742193-af75-4049-b925-be98e9c551dd.png" width="350" />
