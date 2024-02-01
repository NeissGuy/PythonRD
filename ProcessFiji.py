import subprocess
import os

def process_image(input_path, output_path):
    # Chemin vers le programme Fiji
    fiji_path = r"C:\Users\felix\OneDrive\Documents\ENSMA\R&D\Fiji.app\ImageJ-linux64"  # Assurez-vous que le chemin est correct

    # Construction des chemins complets pour l'entrée et la sortie
    input_image_path = os.path.abspath(input_path)
    output_image_path = os.path.abspath(output_path)

    # Script ImageJ Macro
    macro_script = """
        // Ouvrir l'image
        open('{}');

        // Appliquer un filtre de lissage (Gaussian Blur)
        run('Gaussian Blur...', 'sigma=2');

        // Sauvegarder l'image résultante
        saveAs('Tiff', '{}');

        // Fermer l'image originale
        close();
    """.format(input_image_path, output_image_path)

    # Chemin vers un fichier temporaire pour enregistrer le script ImageJ Macro
    macro_script_path = "temp_macro.ijm"

    try:
        # Écrire le script ImageJ Macro dans le fichier temporaire
        with open(macro_script_path, "w") as macro_file:
            macro_file.write(macro_script)

        # Commande complète pour exécuter Fiji avec le script inclus
        full_command = '{} --headless --console --run "{}"'.format(fiji_path, macro_script_path)

        # Exécutez la commande
        subprocess.run(full_command)

    finally:
        # Supprimer le fichier temporaire après exécution
        if os.path.exists(macro_script_path):
            os.remove(macro_script_path)

if __name__ == "__main__":
    # Remplacez ces chemins par les chemins appropriés vers votre image d'entrée et le lieu où vous souhaitez enregistrer l'image résultante
    input_image_path = r"C:\Users\felix\OneDrive\Documents\ENSMA\RD\SavesFiji\Result2.png"
    output_image_path = r"C:\Users\felix\OneDrive\Documents\ENSMA\RD\SavesFiji\TestFolderCode"

    # Exécutez la fonction pour traiter l'image
    process_image(input_image_path, output_image_path)
