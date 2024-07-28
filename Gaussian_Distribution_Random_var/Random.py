import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class GaussianSampler:
    def __init__(self, mean, std_dev, sample_size):
        self.mean = mean
        self.std_dev = std_dev
        self.sample_size = sample_size
        self.samples = self.generate_samples()

    def generate_samples(self):
        """Generate random samples from a Gaussian distribution."""
        return np.random.normal(self.mean, self.std_dev, self.sample_size)

    def plot_samples(self, output_file=None):
        """Plot the histogram of the samples and save to a file if specified."""
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))

        # Plot the histogram and the density curve
        sns.histplot(self.samples, bins=30, kde=True, color='Darkblue', stat='density')

        # Titles and labels
        plt.title("Random Samples from Gaussian Distribution", fontsize=15, weight='bold')
        plt.xlabel("Value", fontsize=14)
        plt.ylabel("Density", fontsize=14)

        # Display the mean and std deviation
        plt.axvline(self.mean, color='red', linestyle='dashed', linewidth=2)
        plt.axvline(self.mean + self.std_dev, color='green', linestyle='dashed', linewidth=2)
        plt.axvline(self.mean - self.std_dev, color='green', linestyle='dashed', linewidth=2)

        # Save the plot to a file if output_file is provided
        if output_file:
            plt.savefig(output_file)
            plt.close()
        else:
            plt.show()


