##  Organise Files

This project automatically organises files into folders based on their file types, including images, documents, text files, and other formats.

- ```import os```: Interact with the operating system for file & folder operations (create, delete, navigate directories)

- ```import shutil```: Moves files and folders

- ```os.path.join```: Combine folders and filenames into a full path

- ```(os.path.expanduser("~")```: Find home folder and go to Desktop

<b>How it works</b>

 - Run python file

```python
python organise_files.py
```

Input:

    image.png
    document1.docx
    document2.pdf
    document3.txt

Output:

    Moved image.png → Image 
    Moved document1.docx → Document
    Moved document2.pdf → Document
    Moved document3.txt → Document