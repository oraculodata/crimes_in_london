This project aims to assist those who plan to visit London or those who live in London. With this app, you can walk in the least risky areas to ensure your safety, avoiding places with higher security risks.

The data has been extracted from [https://data.police.uk/about](https://data.police.uk/data/archive/latest.zip), so they are real data.

![Page Street](page_street.png) "Street Map")


# Tables

I've created 3 tables: table_outcomes, table_street, and table_stop_and_search. Below are the DDLs:

```sql
CREATE TABLE outcomes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month TEXT,
    reported_by TEXT,
    falls_within TEXT,
    longitude TEXT,
    latitude TEXT,
    location TEXT,
    lsoa_code TEXT,
    lsoa_name TEXT,
    outcome_type TEXT,
    file_name TEXT
);
```

```sql
CREATE TABLE street (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month TEXT,
    reported_by TEXT,
    falls_within TEXT,
    longitude TEXT,
    latitude TEXT,
    location TEXT,
    lsoa_code TEXT,
    lsoa_name TEXT,
    crime_type TEXT,
    last_outcome_category TEXT,
    context TEXT,
    file_name TEXT
);
```

```sql
CREATE TABLE stop_and_search (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type TEXT,
    date DATE,
    part_of_a_policing_operation TEXT,
    policing_operation TEXT,
    latitude TEXT,
    longitude TEXT,
    gender TEXT,
    age_range TEXT,
    self_defined_ethnicity TEXT,
    officer_defined_ethnicity TEXT,
    legislation TEXT,
    object_of_search TEXT,
    outcome TEXT,
    outcome_linked_to_object_of_search TEXT,
    removal_of_more_than_just_outer_clothing TEXT,
    file_name TEXT
);
```

