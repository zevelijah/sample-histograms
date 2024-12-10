
# Please Set eviroment variable: QT_QPA_PLATFORM=offscreen

# Re-import necessary libraries and re-define the function after reset
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to take random samples and save histograms as images
def save_histograms_as_images(csv_file, output_dir="graphs"):
    # Step 1: Read the CSV
    data = pd.read_csv(csv_file)
    
    # Check if it's a single-column CSV
    if data.shape[1] != 1:
        raise ValueError("The CSV must have only one column.")
    
    # Extract the column as a numpy array for processing
    values = data.iloc[:, 0].values
    
    # Step 2: Random Sampling
    sample_sizes = [1000, 200, 200, 200, 200, 20, 20, 20, 20, 5, 5, 5, 5]
    for val in sample_sizes:
        if val > values.size:
            raise ValueError("At least one of your graph request demand more values than provided.")
    samples = [np.random.choice(values, size=size, replace=False) for size in sample_sizes]
    
    # Step 3: Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Step 4: Save Histograms as Images
    for i, (sample, size) in enumerate(zip(samples, sample_sizes)):
        mean_value = np.mean(sample)
        std_dev = np.std(sample)
        # plt.text(-1, -1, f'Mean = {mean_value:.2f}', color='red', fontsize=10, ha='right', va='center', rotation=90)
        plt.figure(figsize=(6, 4))
        plt.hist(sample, bins='auto', color='maroon', alpha=0.7)
        plt.title(f"Sample {i+1} (n={size})")
        plt.xlabel("Height(Meters)")
        plt.ylabel("Frequency")

        plt.xlim(1.55, 1.85)

        text_x_position = min(sample) + (max(sample) - min(sample)) * 0.0001
        
        plt.ylim(top=plt.ylim()[1] * 1.2)
        plt.text(x=text_x_position, y=plt.ylim()[1] * 0.95, s=f'Mean = {mean_value:.2f}', color='maroon', fontsize=12, ha='left', va='center')
        plt.text(x=text_x_position, y=plt.ylim()[1] * 0.90, s=f'Standard Deviation = {std_dev:.2f}', color='maroon', fontsize=12, ha='left', va='center')

        # Save the plot
        output_path = os.path.join(output_dir, f"histogram_sample_{i+1}.png")
        plt.savefig(output_path)
        plt.close()

    print(f"Histograms have been saved in the '{output_dir}' directory.")

# Uncomment to use with a file
save_histograms_as_images('./data/human_heights.csv')
