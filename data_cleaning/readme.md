##  Data Cleaning Files

This project provides an automated data cleaning for CSV and Excel files. It simplifies the process of preparing datasets by handling missing values, duplicates, and standardising column names.

- ```import os```: Interact with the operating system for file & folder operations (create, delete, navigate directories)

- ```openpyxl```: Read and write Excel files using pandas

<b>How it works</b>

 - Run python file

```python
python data_cleaning.py
```

Input:

| name  | age | height | weight |
| ----- | --- | ------ | ------ |
| Joe   | 3   | 130    | 5      |
| Bob   |     | 107    |        |
|       | 30  |        | 70     |

Output:

| name    | age     | height  | weight  |
| ------- | ------- | ------- | ------- |
| Joe     | 3       | 130     | 55      |
| Bob     | Unknown | 107     | Unknown |
| Unknown | 30      | Unknown | 70      |
