# Pokémon Obtainability Database

A Streamlit app that shows which Pokémon are obtainable in each Pokémon game.

## Live Demo

Check out the app here: [Pokémon Obtainability Database](https://pokefinderdb.streamlit.app/)

## Screenshots:
<img width="1815" height="757" alt="image" src="https://github.com/user-attachments/assets/8bd6960a-eca1-4a56-92a4-1be109a217d3" />
<img width="1898" height="845" alt="image" src="https://github.com/user-attachments/assets/436d489a-1af0-4a90-8ce4-7560cd9a9d28" />

## Features
- Search Pokémon by name
- Search by National Dex number
- Filter Pokémon by game
- View obtainable Pokémon data

## Built With
- Python
- Pandas
- Streamlit


## Data Sources

The database was created by collecting and combining Pokémon availability data from publicly available Pokémon resources.
### DataSets Created Using:
- BeautifulSoup
- Python
- Pandas
- Requests
- Playwright
  
#### Web Scrappers 
The web scrapers were used during the data collection and preparation phase to gather and clean Pokémon availability data. The Streamlit application uses the finalized dataset rather than scraping websites every time it runs, which improves speed, reliability, and consistency.

## Installation

Clone the repository:
```bash
git clone https://github.com/propup/List-of-Pokemon-per-Game-Obtainability.git
```
Navigate into the project folder:
```bash
cd List-of-Pokemon-per-Game-Obtainability
```
Create a virtual environment:
```bash
python -m venv .venv
```
Activate the virtual environment:

Windows:
```bash
.venv\Scripts\activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## Running the Application

Run the Streamlit application:
```bash
streamlit run app.py
```
The application will open in your browser.

## Project Structure

List-of-Pokemon-per-Game-Obtainability/
- app.py - Streamlit application
- requirements.txt - Python dependencies
- CSVs/ - Pokémon datasets
- README.md - Project documentation

## How the Data Was Created

The dataset was created through a multi-step data collection and cleaning process:

1. **Data Collection**
   - Pokémon availability data was collected from publicly available Pokémon resources using Python web scraping tools.
   - BeautifulSoup and Playwright were used to extract data from web pages with different structures.

2. **Data Cleaning**
   - The collected data was cleaned and standardized using Pandas.
   - Data inconsistencies, duplicate entries, and formatting issues were corrected to create a consistent dataset.

3. **Dataset Creation**
   - Individual datasets were combined into a master CSV file containing Pokémon availability information across different games.
   - The final dataset was structured to allow searching and filtering by Pokémon, National Dex number, and game.

4. **Application**
   - The Streamlit application reads the finalized CSV dataset and provides an interactive interface for exploring Pokémon availability.


## Author
Pro Pup

## Notes:
This is a first project there will likely be errors.
