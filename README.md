 File Organizer CLI Tool

The File Organizer CLI Tool is a simple Python script that helps users to organize their files in a directory by sorting them into folders based on file type. This tool is particularly useful for cleaning up and organizing cluttered directories, such as downloads folders.

## Features

- **Simple and Lightweight**: No external dependencies are required.
- **Customizable**: Easily extendable to include more file types or different sorting criteria.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Getting Started

### Prerequisites

- Python 3.6 or newer

### Installation

No installation is necessary. Just download `organize.py` to your local machine.

### Usage

To use the File Organizer, navigate to the directory containing `organize.py` in your terminal or command prompt, and run:

```sh
python organize.py /path/to/your/target/directory

Replace /path/to/your/target/directory with the path to the directory you want to organize. The script will automatically create subdirectories based on file extensions and move the files into their respective folders.

How It Works
The File Organizer scans the specified directory for files (excluding other directories) and organizes them into folders based on their file extension. If the appropriate folder for a file type does not exist, it creates one. For example, all .jpg files will be moved to a "JPG" folder, .pdf files to a "PDF" folder, and so on.

Customization
You can customize the script to handle additional file types or to change the sorting criteria by modifying the organize_directory function in organize.py.

Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

License
This project is open-source and available under the MIT License. See the LICENSE file for more information.

Contact
If you have any questions or feedback, please don't hesitate to reach out.


