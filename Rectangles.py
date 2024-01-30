import cv2
import numpy as np

# Charger l'image binaire
image_binaire = cv2.imread("E:\logiciel\R&D\Result1 m.png", cv2.IMREAD_GRAYSCALE)

# Appliquer une opération de seuillage pour obtenir une image binaire claire
_, thresh = cv2.threshold(image_binaire, 128, 255, cv2.THRESH_BINARY)

# Trouver les contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Définir la taille minimale du contour à inclure
taille_minimale_contour = 2000  # Vous pouvez ajuster cette valeur en fonction de vos besoins

# Créer une image vide pour dessiner les contours
image_contours = np.zeros_like(image_binaire)

# Liste pour stocker les coordonnées des contours
coordonnees_contours = []

# Dessiner les contours sur l'image vide et extraire les coordonnées
for contour in contours:
    # Calculer la surface du contour
    surface_contour = cv2.contourArea(contour)
    
    # Exclure les contours de petite taille
    if surface_contour >= taille_minimale_contour:
        # Dessiner le contour sur l'image vide
        cv2.drawContours(image_contours, [contour], -1, (255, 255, 255), 2)
        
        # Extraire les coordonnées du contour et les ajouter à la liste
        coordonnees_contour = contour.reshape(-1, 2)  # Reshape pour obtenir une liste de coordonnées (X, Y)
        coordonnees_contours.append(coordonnees_contour)

# Calculer la dérivée du déplacement pour chaque point du contour
derivatives_contours = [np.diff(coordonnees, axis=0) for coordonnees in coordonnees_contours]

# Sauvegarder les coordonnées et les dérivées dans un fichier texte
with open('coordonnees_et_derivatives.txt', 'w') as file:
    for i, (coordonnees, derivatives) in enumerate(zip(coordonnees_contours, derivatives_contours)):
        file.write(f"Contour {i + 1} :\n")
        file.write("Coordonnées :\n")
        np.savetxt(file, coordonnees, fmt='%d', delimiter='\t')
        file.write("Dérivées :\n")
        np.savetxt(file, derivatives, fmt='%d', delimiter='\t')

# Afficher l'image originale et l'image avec les contours
cv2.imshow('Image originale', image_binaire)
cv2.imshow('Contours', image_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Coordonnées et dérivées des contours ont été sauvegardées dans le fichier 'coordonnees_et_derivatives.txt'.")

"""""
Backup du code de maxime
"""""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2 # Import librairy to use image and draw on it 
import matplotlib.pyplot as plt # For the plot function

# Open an image file
image_path = "Z:\projet\picture\ID_x10k.tif"
img = cv2.imread(image_path)
image = cv2.imread(image_path)

# Convert BGR to RGB (OpenCV reads images in BGR format by default)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(img_rgb)
plt.axis('off')  # Turn off axis labels
plt.show()

# Get the size (dimensions) of the image
height, width, channels = img.shape
height, width, channels = image.shape

# Display the size
print("Image size (width x height):", width, "x", height)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and help contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detector
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edged image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the detected contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('Contours', image)


# List to store aspect ratios
aspect_ratios = []

# Calculate and display the aspect ratio for each detected shape
for contour in contours:
    # Calculate the bounding box of the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Calculate the aspect ratio
    aspect_ratio = float(w) / h

    # Print or display the aspect ratio
    print("Aspect Ratio:", aspect_ratio)

    # Append the aspect ratio to the list
    aspect_ratios.append(aspect_ratio)

# Plot histogram of aspect ratios
plt.hist(aspect_ratios, bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Aspect Ratios of Detected Shapes')
plt.xlabel('Aspect Ratio')
plt.ylabel('Frequency')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
