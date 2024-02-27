import os
from pathlib import Path

def organize_directory(directory):
    for item in os.listdir(directory):
        item_path = Path(directory) / item
        if item_path.is_file():
            file_type = item.split('.')[-1].upper()
            directory_path = Path(directory) / file_type
            if not directory_path.exists():
                directory_path.mkdir()
            item_path.rename(directory_path / item)
            print(f"Moved: {item} to {directory_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        organize_directory(sys.argv[1])
    else:
        print("Usage: python organize.py [directory_path]")