# Cymatics
In this cymatics project library resonance patterns are analyzed versius various parameters. 
## Contents
- <a href="https://github.com/csanadm/cymatics/blob/main/analyze.py">analyze.py</a>: analyzing an Excel file with `DataFrame` (from `pandas`), by investigating dependence of the symmetry-fold on the parameters, and doing a linear regression to see r-values.
- <a href="https://github.com/csanadm/cymatics/blob/main/fit.py">fit.py</a>: perform an actual fit with `lmfit`, to see if there is a linear form based on the parameters that successfully predicts the symmetry-fold.
- <a href="https://github.com/csanadm/cymatics/blob/main/linreg_scikit.py">linreg_scikit.py</a>: perform ML-based linear regression with `scikit-learn`.
- <a href="https://github.com/csanadm/cymatics/blob/main/svr_scikit.py">svr_scikit.py</a>: perform Support Vector Regression with `scikit-learn`.

Here is an example output (omitting polynomial regression):
![svr_scikit](https://user-images.githubusercontent.com/38218165/225023498-530e1405-e29c-4292-b457-b2ec0c48b598.png)
