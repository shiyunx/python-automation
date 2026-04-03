##  Rename Images

This project automatically renames images in sequential order and supports multiple formats.

- ```import os```: Interact with the operating system for file & folder operations

- ```files = os.listdir("data")```: List all files & folders in the specified directory

<b>How it works</b>

 - Run python file

```python
python rename_images.py
```

Input:

    Images folder: /Users/name/Desktop/filename

<br>

    img_111.jpg
    img_222.jpeg
    img_333.png

Output:

    image1.jpg
    image2.jpeg
    image3.png