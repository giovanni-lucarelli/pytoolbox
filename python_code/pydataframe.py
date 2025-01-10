import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

import sys
sys.path.append('../build')
import data_frame as df

# Define additional methods
def to_pandas(self):
    data = self.get_data()
    df = pd.DataFrame({col: [row if row is not None else np.nan for row in col_data]
                       for col, col_data in zip(self.get_header(), data)})
    return df

def plot_histogram(self, column_name, bins=10):
    if not self.is_numeric(column_name):
        raise ValueError(f"Column '{column_name}' is not numeric.")
    
    data = self.get_double_column(column_name)
    clean_data = [x for x in data if x is not None]
    sns.histplot(clean_data, bins=bins, kde=True, color="blue")
    plt.title(f"Histogram of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.show()

def plot_correlation_matrix(self, column_names):
    data = {name: self.get_double_column(name) for name in column_names}
    df = pd.DataFrame(data)
    corr_matrix = df.corr()

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
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

# Access the class from the module
DataFrame = df.DataFrame

# Add methods dynamically to the C++ class
DataFrame.to_pandas = to_pandas
DataFrame.plot_histogram = plot_histogram
DataFrame.plot_correlation_matrix = plot_correlation_matrix
DataFrame.scatter_plot = scatter_plot
DataFrame.advanced_stat = advanced_stat

