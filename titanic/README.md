# Titanic
Download, explore, and wrangle the Titanic passenger manifest dataset with an eye toward developing a predictive model for survival.

This tutorial is based on the Kaggle Competition,["Predicting Survival Aboard the Titanic"](https://www.kaggle.com/c/titanic)

![RMS Titanic , Ocean Liner, (1912)](https://github.com/georgetown-analytics/XBUS-503-01.Data_Ingestion_and_Wrangling/titanic/blob/master/images/Cd51-1000g.gif)
_Licensed under CC BY-SA 3.0 via Wikimedia Commons: "Cd51-1000g" by Boris Lux_

## STEP ONE: EXPLORATORY ANALYSIS
Start by cloning this repository.

__Anaconda users__: you should have everything you need, but _if_ you find you are missing anything, type this into the command line:

    conda install <package>

**Windows users MUST install scikit-learn via conda install. DO NOT use pip install. It will fail.**

__Others__: make sure the required libraries are installed by using:

    pip install -r requirements.txt    

Then look inside the data folder and open ```train.csv``` to check out the dataset we'll be exploring today.  

To start the lab, open up the iPython Notebook file: ```titanic_wrangling.ipynb```.


### Things to think about
1. How to explore a new dataset?
2. What to look for in tabular data?
3. What visualization tools can you use to help you explore?
4. What is the end goal of data wrangling? Why are we even doing this?
5. What to clean and how to clean it?


See also:     
[Baby steps to performing exploratory analysis in Python](http://www.analyticsvidhya.com/blog/2014/08/baby-steps-python-performing-exploratory-analysis-python/)     
[Data munging using Pandas](http://www.analyticsvidhya.com/blog/2014/09/data-munging-python-using-pandas-baby-steps-python/)


## STEP TWO: MACHINE LEARNING FROM DISASTER
_(You will do this portion in the Machine Learning course.)_      

Welcome back! Navigate to your titanic folder in the command line and then type to get the latest adds to the repo

    git pull

__Anaconda users__: you already have Scikit-learn! _If_ you ever find you are missing anything, type this into the command line:

    conda install <package>

Everyone else, make sure Scikit-learn is installed:

__WINDOWS USERS__: 

    conda install scikit-learn

__MAC OSX USERS__: 

	pip install -U numpy scipy scikit-learn

__LINUX w/ Python 2__: 	

	sudo apt-get install build-essential python-dev python-setuptools \
                     python-numpy python-scipy \
                     libatlas-dev libatlas3gf-base
	sudo apt-get install python-matplotlib

__LINUX w/ Python 3__: 

 	sudo apt-get install build-essential python3-dev python3-setuptools \
 					 python3-numpy python3-scipy \
                     libatlas-dev libatlas3gf-base
    sudo apt-get install python-matplotlib


Problems with installation? Check out: http://scikit-learn.org/stable/install.html


### Key Concepts    
__Machine Learning__    

__Classification__    

__Cross-Validation__    
http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.train_test_split.html

__Model Evaluation__    
    -Classification reports    
    -Precision recall curves    
    -Mean squared error    
    -Coefficient of determination     

### Key Tools in Scikit-Learn    
__Linear Regression__    
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

__Random Forests__    
http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

__Support Vector Machines__    
http://scikit-learn.org/stable/modules/svm.html

### Sources
This tutorial is based on the following tutorials for Kaggle's titanic competition:
    - https://www.kaggle.com/mlchang/titanic/logistic-model-using-scikit-learn/run/91385
    - https://www.kaggle.com/c/titanic/details/getting-started-with-random-forests
    - https://github.com/savarin/pyconuk-introtutorial/tree/master/notebooks