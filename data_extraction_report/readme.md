##  Data Extraction Report

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline. Data is extracted from sqlite, transformed, and loaded into google sheets for reporting.

<b>How it works</b>

 - Run python file

```python
data_extraction_report.ipynb
```

Input:

    - Sqlite database (it_tickets.db)
    - Data: TicketID, DepartmentID, Status, Priority, ResolutionHours, CreatedDate

Output:

    Google Sheets:

    - Tickets by Department
    - Status & Priority
    - Average Resolution Time