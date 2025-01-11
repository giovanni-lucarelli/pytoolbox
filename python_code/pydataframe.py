import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from typing import List, Optional, Union

import sys
sys.path.append('../build')
import data_frame

# Define additional methods
def to_pandas(self):
    data = self.get_data()
    df = pd.DataFrame({col: [row if row is not None else np.nan for row in col_data]
                       for col, col_data in zip(self.get_header(), data)})
    return df

def plot_histogram(self, column_name, bins=10, kde=True):
    if not self.is_numeric(column_name):
        raise ValueError(f"Column '{column_name}' is not numeric.")
    
    data = self.get_double_column(column_name)
    clean_data = [x for x in data if x is not None]
    sns.histplot(clean_data, bins=bins, kde=kde, color="blue")
    plt.title(f"Histogram of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.show()

def plot_correlation_matrix(self, column_names):

    corr_matrix = np.zeros((len(column_names), len(column_names)))
    for i, name1 in enumerate(column_names):
        for j, name2 in enumerate(column_names):
            corr_matrix[i, j] = self.correlation(name1, name2)

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=column_names, yticklabels=column_names)
    plt.title("Correlation Matrix")
    plt.show()

def scatter_plot(self, x_col, y_col):
    if not (self.is_numeric(x_col) and self.is_numeric(y_col)):
        raise ValueError(f"Both columns '{x_col}' and '{y_col}' must be numeric.")
    
    x_data = self.get_double_column(x_col)
    y_data = self.get_double_column(y_col)
    clean_data = [(x, y) for x, y in zip(x_data, y_data) if x is not None and y is not None]
    x_clean, y_clean = zip(*clean_data)

    sns.scatterplot(x=x_clean, y=y_clean)
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def advanced_stat(self, column_name):
    if not self.is_numeric(column_name):
        raise ValueError(f"Column '{column_name}' is not numeric.")
    
    data = np.array(self.get_double_column(column_name))
    clean_data = data[~np.isnan(data)]
    mean = np.mean(clean_data)
    std_dev = np.std(clean_data)
    skewness = norm.stats(loc=mean, scale=std_dev, moments='s')
    kurtosis = norm.stats(loc=mean, scale=std_dev, moments='k')
    return {
        "mean": mean,
        "std_dev": std_dev,
        "skewness": skewness,
        "kurtosis": kurtosis
    }

def __str__(self):
    return self.to_pandas().__str__()


def __len__(self):
    """
    Returns the number of rows in the DataFrame.
    """
    return self.shape()[0]

def __getitem__(self, column_name: str) -> List[Optional[Union[float, str]]]:
    """
    Allows Pythonic access to columns via indexing.
    """
    return self.get_column(self.find_idx(column_name))

def df_iter(self):
    begin = self.begin()
    end = self.end()
    while begin != end:
        row = begin.dereference()
        yield row
        begin.increment()  # Increment the iterator



# Access the class from the module
DataFrame = data_frame.DataFrame

# Add methods dynamically to the C++ class
DataFrame.to_pandas = to_pandas
DataFrame.plot_histogram = plot_histogram
DataFrame.plot_correlation_matrix = plot_correlation_matrix
DataFrame.scatter_plot = scatter_plot
DataFrame.advanced_stat = advanced_stat
DataFrame.__str__ = __str__
DataFrame.__len__ = __len__
DataFrame.__getitem__ = __getitem__
DataFrame.__iter__ = df_iter
