import os
import shutil

# 1️⃣ Folder path (CHANGE THIS)
folder_path = r"C:\Users\hp\Desktop\TestFolder"

# 2️⃣ File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# 3️⃣ Organize files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()

        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                target_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {folder_name}")
                break

print("✅ File organization completed!")
