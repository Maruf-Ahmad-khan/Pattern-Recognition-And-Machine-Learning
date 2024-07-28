import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class GaussianDistribution:
    def __init__(self, data_file, column):
        self.data_file = data_file
        self.column = column
        self.data = self.load_data()
        self.mean = self.calculate_mean()
        self.std_dev = self.calculate_std_dev()

    def load_data(self):
        """Load data from the Excel file"""
        df = pd.read_excel(self.data_file)
        print("Columns in the dataset:", df.columns)
        return df[self.column].dropna()

    def calculate_mean(self):
        """Calculate the mean of the data"""
        return self.data.mean()

    def calculate_std_dev(self):
        """Calculate the standard deviation of the data"""
        return self.data.std()

    def plot_distribution(self, output_file):
        """Plot the Gaussian distribution of the data and save to a file"""
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))

        # Plot the histogram and the density curve
        sns.histplot(self.data, bins=30, kde=True, color='Darkblue', stat='density')

        # Titles and labels
        plt.title("Gaussian Distribution (Normal Distribution)", fontsize=15, weight='bold')
        plt.xlabel("Value", fontsize=14)
        plt.ylabel("Density", fontsize=14)

        # Display the mean and std deviation
        plt.axvline(self.mean, color='red', linestyle='dashed', linewidth=2)
        plt.axvline(self.mean + self.std_dev, color='green', linestyle='dashed', linewidth=2)
        plt.axvline(self.mean - self.std_dev, color='green', linestyle='dashed', linewidth=2)

        # Save the plot to a file
        plt.savefig(output_file)
        plt.close()
