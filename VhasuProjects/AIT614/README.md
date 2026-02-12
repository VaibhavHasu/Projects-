
# Big Data Processing and Analysis - AIT 614 Project 

## Objective
The project focuses on applying Big Data techniques to process, analyze, and derive insights using Hadoop, PySpark, Spark MLlib, and DBFS environments on Databricks and Google Colab.

## System Requirements
- Google Colab (Free or Pro)
- Databricks Community Edition (or Enterprise)
- Python 3.8+
- Java 8+ (for Hadoop tasks)
- Apache Hadoop (Pre-installed in Databricks)
- Apache Spark 3.x (comes with Databricks)
- Libraries:
  - pyspark
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - folium (for map visualization)

## Dataset Link
Primary Dataset used:  
FHWA Bridge Conditions Dataset  
You can find similar datasets here:  
   https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm

Upload the CSV dataset to Google Colab / Databricks DBFS before running the notebooks.

## How to Set Up and Run the Project

### 1. Google Colab (Google_colab.ipynb)
- Open Google Colab
- Upload AIT614_003_Team4_Google_colab.ipynb
- Upload the dataset CSV file manually
- Install required libraries:
  ```python
  !pip install pyspark folium matplotlib seaborn scikit-learn
  ```
- Execute the notebook sequentially.

### 2. Hadoop (Hadoop.ipynb)
- Open Databricks
- Create a new cluster (Standard Single Node, Runtime: 12.2 LTS, Python 3).
- Upload AIT614-003_Team4_Hadoop.ipynb
- Load the dataset into DBFS (/FileStore/your_dataset_name.csv)
- Run the notebook.

### 3. DBFS (DBFS.ipynb)
- Open Databricks Workspace
- Upload AIT614-003_Team4_DBFS.ipynb
- Ensure dataset is available in /FileStore/
- Execute the notebook.

### 4. Spark MLlib (Spark_MLib.ipynb)
- Open Databricks
- Upload AIT614-003_Spark_MLib.ipynb
- Run the notebook:
  - Machine learning using Spark MLlib
  - Clustering, Decision Trees, Model Evaluation.

### 5. Spark with Python (Spark_with_Python.ipynb)
- Open Databricks
- Upload AIT614-003_Team4_Spark_with_Python.ipynb
- Run for:
  - Spark SQL queries
  - DataFrame operations
  - Feature Engineering
  - Basic EDA

## Folder Structure
/Project/

Google_colab/
   - AIT614_003_Team4_Google_colab.ipynb
Hadoop/
   - AIT614-003_Team4_Hadoop.ipynb
 DBFS/
   - AIT614-003_Team4_DBFS.ipynb
 Spark_MLib/
   - AIT614-003_Spark_MLib.ipynb
 Spark_with_Python/
   - AIT614-003_Team4_Spark_with_Python.ipynb
 Dataset/
   - (Upload FHWA bridge dataset manually)

## Notes
- Use Databricks clusters with 8GB RAM minimum.
- Start from data loading, ensure correct file paths.
- For map visualizations in Google Colab, ensure folium is installed.
- HTML files are exported notebooks for offline view.

## Troubleshooting
- Install missing libraries if you get ModuleNotFoundError.
- Restart Databricks cluster if needed.
- Check DBFS paths carefully.
