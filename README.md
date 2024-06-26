This project aims to assist those who plan to visit City of London or those who live in City of London. With this app, you can walk in the least risky areas to ensure your safety, avoiding places with higher security risks.

The data has been extracted from [https://data.police.uk/about](https://data.police.uk/data/archive/latest.zip), so they are real data.

## Home
![Page Street](home.png)

## Street
![Page Street](page_street.png)
![Page Street Crimes Selected](page_street_crimes_selected.png)

## Stop and Search
![Page Street](page_stop_and_search.png)

> This project is currently under development. I will soon release the version with connections to MariaDB and Snowflake, along with the historical crime data loading routine.


## Running the application

````
git clone https://github.com/oraculodata/crimes_in_london.git
cd crimes_in_london
pip install -r requirements.txt
streamlit run 🛡️_Home.py
````
