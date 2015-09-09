# stocker

While the predictive results were unimpressive, this project implements the following:

[download_data.py](https://github.com/austinjalexander/stocker/blob/master/download_data.py): download multiple data sets from two sources, Quandl and Google Finance.

[convert_quandl_to_df.py](https://github.com/austinjalexander/stocker/blob/master/convert_quandl_to_df.py), [convert_goog_to_df.py](https://github.com/austinjalexander/stocker/blob/master/convert_goog_to_df.py): clean data sets, convert to Pandas data frames

[DataGen-GQ.ipynb](https://github.com/austinjalexander/stocker/blob/master/DataGen-GQ.ipynb): merge data frames, additional data processing, implement nn.py

[nn.py](https://github.com/austinjalexander/stocker/blob/master/nn.py): additional data processing (including optional label balancing, select K best, and feature scaling); also includes:
 - random search implementation to attempt various combinations of hyperparameters
 - forward propagation and backpropagation with various nonlinear activation function options
 - finite difference approximation to check behavior of backpropagation implementation 
 - L1 and L2 regularization options
 - 2-hidden layer neural network architecture
 - stochastic gradient descent
 - cross-validation via training, validation, and testing sets
 - randomized order of training examples for each epoch
 - prevention of consecutive identically labeled training examples
 