import numpy as np
import matplotlib.pyplot as plt

# Create a sample matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Plot the matrix as an image
plt.imshow(matrix, cmap='gray')

# Add a title to show the matrix number
plt.title("Matrix [1]")

# Add square brackets to the image
plt.text(-0.5, -0.5, "[", fontsize=18, color='white')
plt.text(2.5, -0.5, "]", fontsize=18, color='white')
plt.text(-0.5, 2.5, "[", fontsize=18, color='white')
plt.text(2.5, 2.5, "]", fontsize=18, color='white')

# Add a color bar to show the values
plt.colorbar()

# Show the image
plt.show()

save_path = 'UFS02/matplotlib/immagine.png'
# Save the image
plt.savefig(save_path)

