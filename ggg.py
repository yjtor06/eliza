def extract_keys(file_path):
    """Extrait les clés d'un fichier en supposant un format 'key: value'."""
    keys = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "key:" in line:
                key = line.split(':')[1].strip()
                keys.add(key)
    return keys

def compare_keys(file_path1, file_path2):
    """Compare les clés de deux fichiers et retourne les clés uniques à chaque fichier."""
    keys_file1 = extract_keys(file_path1)
    keys_file2 = extract_keys(file_path2)
    

    unique_to_file1 = keys_file1 - keys_file2
    unique_to_file2 = keys_file2 - keys_file1

    return unique_to_file1, unique_to_file2

# Chemins vers les fichiers
file_doctorbis_path = 'doctorbis.txt'
file_processed_full_path = 'sortie.txt'

# Comparaison des clés
unique_keys_doctorbis, unique_keys_processed_full = compare_keys(file_doctorbis_path, file_processed_full_path)

# Affichage des résultats
print("Clés uniques au fichier DoctorBis:", unique_keys_doctorbis)
print("Clés uniques au fichier Processed_Full:", unique_keys_processed_full)
