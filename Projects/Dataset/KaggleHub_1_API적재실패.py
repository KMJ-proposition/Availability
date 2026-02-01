# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
# The previous path '/kaggle/input/apple-comprehensive-financial-dataset-1980-2026.csv' was incorrect.
# For kagglehub.dataset_load, file_path should be the relative path within the dataset.
# According to the Kaggle dataset page, the main CSV file is 'AAPL.csv'.
file_path = "aapl_master_enriched.csv"

# To find the correct file name, list the contents of the dataset directory:
print("Listing files in the dataset directory:")
!ls /kaggle/input/apple-comprehensive-financial-dataset-1980-2026

# Load the latest version
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "adamvakar/apple-comprehensive-financial-dataset-1980-2026",
  file_path,
  # Provide any additional arguments like
  # sql_query or pandas_kwargs. See the
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

# print("First 5 records:", df.head())
# df.info()
