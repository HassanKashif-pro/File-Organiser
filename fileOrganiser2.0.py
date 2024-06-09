import os
import shutil

def organize_files(path):
    try:
        files = os.listdir(path)

        for file in files:
            if os.path.isfile(os.path.join(path, file)):  # Check if it's a file
                filename, extension = os.path.splitext(file)
                extension = extension[1:]  # Remove the dot from the extension

                if extension:  # Ensure there is an extension
                    extension_folder = os.path.join(path, extension.upper())
                    
                    if not os.path.exists(extension_folder):
                        os.makedirs(extension_folder)
                    
                    shutil.move(os.path.join(path, file), os.path.join(extension_folder, file))

        print("Files have been organized.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input("Enter Path: ").strip()
    if os.path.exists(path) and os.path.isdir(path):
        organize_files(path)
    else:
        print("The specified path does not exist or is not a directory.")
