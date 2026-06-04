import os
import shutil

class BackupUtility:
    def __init__(self, source, backup):
        self.source = source
        self.backup = backup
        self.copied = set()

    def backup_files(self):
        os.makedirs(self.backup, exist_ok=True)

        log = open("backup.log", "w")

        try:
            files = os.listdir(self.source)

            for file in files:
                if file in self.copied:
                    continue

                src = os.path.join(self.source, file)
                dest = os.path.join(self.backup, file)

                try:
                    shutil.copy2(src, dest)
                    self.copied.add(file)
                    log.write(f"Copied: {file}\n")
                    print("Copied:", file)

                except FileNotFoundError:
                    log.write(f"Missing file: {file}\n")
                    print("File not found:", file)

                except PermissionError:
                    log.write(f"Permission denied: {file}\n")
                    print("Permission error:", file)

        finally:
            log.close()


# Example usage
source_folder = "source_files"
backup_folder = "backup_files"

backup = BackupUtility(source_folder, backup_folder)
backup.backup_files()