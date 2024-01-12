def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

        max_lines = max(len(file1_lines), len(file2_lines))
        j=0
        for i in range(max_lines):
            line1 = file1_lines[i].strip() if i < len(file1_lines) else None
            line2 = file2_lines[i].strip() if i < len(file2_lines) else None
            if line1 != line2:
                j+=1
                print(f"Ligne {i+1}:")
                print(f"Fichier 1: {line1}")
                print(f"Fichier 2: {line2}")
        print(j)

# Exemple d'utilisation
compare_files('eliza_test_results.txt', 'eliza_test_results_bis.txt')
