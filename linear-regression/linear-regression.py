"""
This is a simple linear model used as an example at academiabigdata.com.br

The model tries to predict the length of a fish based on its age and the water temperature
The dataset can be found at http://people.sc.fsu.edu/~jburkardt/datasets/regression/x06.txt
"""
import pandas
import statsmodels.formula.api as sm
#Reads the dataset as a fixed width txt and skipping the first 37 rows
data = pandas.read_fwf("x06.txt", widths=[2,5,4,6], index_col=0, skiprows=37, header=None, names=["Age", "Temperature", "Length"])
#Fits a model with Length as a function of Age and Temperature
result = sm.ols(formula="Length ~ Age + Temperature", data=data).fit()
print "========= Model coefficients ========="
print result.params
print "========= Results Summary ========="
print result.summary()
