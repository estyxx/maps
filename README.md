# Emilia-Romagna Provinces Map Project

This project provides a visual representation of the provinces in the Emilia-Romagna region of Italy using Python, GeoPandas, and Matplotlib. The map highlights each province within the region, providing a clear and detailed view.

## Project Setup

### Prerequisites

Ensure you have Python installed on your machine. This project uses `uv` for dependency management and Jupyter Notebook for running the script.

### Installation

1. **Clone the Repository**

   ```sh
   git clone git@github.com:estyxx/maps.git
   cd maps
   ```

2. **Install Dependencies**

   This project uses [uv](https://docs.astral.sh/uv) for dependency management. Install uv if you haven't already.

   Then, install the project dependencies:

   ```sh
   uv sync
   ```

### Download GADM Data

1. Visit the [GADM download page](https://gadm.org/download_country.html#google_vignette).

2. Select "Italy" from the list of countries.

3. Download the shapefiles for the desired administrative level. For this project, the second level (provinces) is used.

4. Extract the downloaded ZIP file to a known location on your computer.

### Running the Script

1. **Launch Jupyter Notebook**

   ```sh
   uv run jupyter notebook
   ```

2. **Open the Notebook**

   Open the notebook file provided in the repository.

3. **Update the Path**

   In the notebook, update the path to the GADM shapefile you downloaded and extracted.

   ```python
   provinces = gpd.read_file('path_to_your_shapefile.shp')
   ```

4. **Run the Notebook**

   Execute the cells in the notebook to generate the map of the Emilia-Romagna provinces.
