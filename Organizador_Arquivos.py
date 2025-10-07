import os
import shutil
from pathlib import Path

def create_folder(folder_path):
    """Cria uma pasta se ela não existir"""
    if not folder_path.exists():
        folder_path.mkdir()
        print(f"📁 Pasta criada: {folder_path}")

def organize_files(directory):
    """Organiza os arquivos da pasta por tipo"""
    path = Path(directory)

    # Dicionário com categorias e extensões
    file_types = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Vídeos": [".mp4", ".avi", ".mkv"],
        "Áudios": [".mp3", ".wav"],
        "Compactados": [".zip", ".rar"],
        "Outros": []
    }

    for file in path.iterdir():
        if file.is_file():
            moved = False
            for folder_name, extensions in file_types.items():
                if file.suffix.lower() in extensions:
                    folder_path = path / folder_name
                    create_folder(folder_path)
                    shutil.move(str(file), folder_path / file.name)
                    print(f"✅ {file.name} → {folder_name}")
                    moved = True
                    break
            if not moved:
                folder_path = path / "Outros"
                create_folder(folder_path)
                shutil.move(str(file), folder_path / file.name)
                print(f"📦 {file.name} → Outros")

def main():
    print("=== ORGANIZADOR DE ARQUIVOS ===")
    folder = input("Digite o caminho da pasta que deseja organizar: ").strip()
    if not os.path.exists(folder):
        print("❌ Caminho inválido.")
        return
    organize_files(folder)
    print("\n🎉 Organização concluída!")

if __name__ == "__main__":
    main()
