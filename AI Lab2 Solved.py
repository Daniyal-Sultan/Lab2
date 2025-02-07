import numpy as np
import matplotlib.pyplot as plt

# # Question 1:

# group_A = [12,15,14,13,16,18,19,15,14,20,17,14,15,40,45,50,62]
# group_B = [12,17,15,13,18,20,21,18,17,16,15,14,16,15]
# CumulativeData = [group_A, group_B]

# # Subplots for Group A and Group B:

# plt.subplot(1,2,1)
# plt.hist(group_A, bins=10)
# plt.title("Group A")
# plt.xlabel("Measurement Values")
# plt.ylabel("Frequency")
# plt.show()

# plt.subplot(1,2,2)
# plt.hist(group_B, bins=10)
# plt.title("Group B")
# plt.xlabel("Measurement Values")
# plt.ylabel("Frequency")
# plt.show()

# # Boxplots for Group A and Group B:

# plt.boxplot(group_B)
# plt.title("Boxplot of Group B")
# plt.ylabel("Measurement Values")
# plt.show()

# plt.boxplot(group_A)
# plt.title("Boxplot of Group A")
# plt.ylabel("Measurement Values")
# plt.show()

# # Question 2:

# file = open("genome.txt", "r")
# genome = file.read()
# file.close()
# x = list(genome)
# genome_length = len(genome)
# color_mapping = {'A': 'red', 'T': 'blue', 'G': 'green', 'C': 'yellow'}
# colors = [color_mapping[base] for base in x]

# t = np.linspace(0, 4*np.pi, genome_length)
# x = np.sin(t)
# y = np.cos(t)
# z = np.linspace(0, 5, genome_length)
# coordinates = np.column_stack([x,y,z])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for i in range(genome_length):
#     ax.scatter(x[i], y[i], z[i], c=colors[i])

# plt.title("3D Genome Visualization on a Helix")
# plt.show()

# # Question 3

# image = plt.imread("image.jpg")
# image_array = np.array(image)

# plt.imshow(image_array)
# plt.axis('off')
# plt.show()

# RotatedImage = np.rot90(image_array, 1)
# plt.imshow(RotatedImage)
# plt.axis('off')
# plt.show()

# FlippedImage = np.fliplr(image_array)
# plt.imshow(FlippedImage)
# plt.axis('off')
# plt.show()

# GrayScale = np.dot(image_array[...,:3], [0.299, 0.587, 0.114])
# plt.imshow(GrayScale, cmap='gray')
# plt.axis('off')
# plt.show()