from Random import GaussianSampler
mean = 0
std_dev = 1
sample_size = 1000
output_file = r"C:\personal\Pattern Recognition And Machine Learning\gaussian_samples.png"  

sampler = GaussianSampler(mean, std_dev, sample_size)
sampler.plot_samples(output_file)

print("Generated samples (first 10):", sampler.samples[:10])
