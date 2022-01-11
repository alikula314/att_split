
ATTS
======

ATTS (Auto Train Test Splitter) splits the given dataframe to train and test without data leakage. It does this with xgboost running in the background. 

Calculates roc_auc scores for the given test size values. Creates a dataframe with these values.
Provides easier change visibility with chart.

## Install
LOFO Importance can be installed using
```
pip install atts
```

For a manual install get this package:

```
wget https://github.com/nikhilkumarsingh/mygmap/archive/master.zip
unzip master.zip
rm master.zip
cd mygmap-master
```

Install the package:
```
python setup.py install    
````

Example
=======

```python

from geo import locator

# get formatted address of any location
print locator.get_address("rohini, delhi")

# get co-ordinates of location
print locator.get_coordinates("delhi")
```    
    

Here is the output:
```
Rohini, New Delhi, Delhi, India
(28.7040592, 77.10249019999999)
```
    
