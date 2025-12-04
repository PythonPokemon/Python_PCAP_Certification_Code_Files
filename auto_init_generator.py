import os

def create_init_files(root_path):
    print(f"Scanne Projekt: {root_path}\n")
    
    for folder, subfolders, files in os.walk(root_path):

        # Überspringe Systemordner (wie __pycache__)
        if "__pycache__" in folder:
            continue

        init_path = os.path.join(folder, "__init__.py")

        # Wenn keine __init__.py existiert → erstellen
        if not os.path.exists(init_path):
            with open(init_path, "w", encoding="utf-8") as f:
                f.write("# Erstellt automatisch, um Python-Paketstruktur zu aktivieren\n")
            print(f"[+] __init__.py erstellt in: {folder}")
        else:
            print(f"[OK] __init__.py existiert bereits in: {folder}")

    print("\nFertig! Alle Pakete sind jetzt korrekt initialisiert.")

# -----------------------------------------
# HIER DEIN PROJEKTPFAD!
# Beispiel für dein Projekt in OneDrive:
# r"C:/Users/Jakob.Derzapf/OneDrive/…/Python_PCAP_Certification_Code_Files"

project_path = r"C:/Users/Jakob.Derzapf/OneDrive/Amadeus Fire AG/Dokumente/Python_PCAP_Certification_Code_Files"

create_init_files(project_path)
