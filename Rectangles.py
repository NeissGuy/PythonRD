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

def exemple(n):
    return "exemple"
