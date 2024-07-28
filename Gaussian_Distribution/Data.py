from Gauss import GaussianDistribution
import pandas as pd

data_file = r"C:\personal\Pattern Recognition And Machine Learning\Cuelinks FS may data.xls"
column = 'Commission'
output_file = r"C:\personal\Pattern Recognition And Machine Learning\gaussian_distribution.png"


gaussian = GaussianDistribution(data_file, column)
print("Mean of Commission:", gaussian.calculate_mean())
print("Standard Deviation of Commission:", gaussian.calculate_std_dev())
gaussian.plot_distribution(output_file)

