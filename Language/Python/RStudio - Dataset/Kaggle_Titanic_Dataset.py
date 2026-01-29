# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np

# Set the path to the file you'd like to load
file_path = "Titanic-Dataset.csv"

# Load the latest version
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "yasserh/titanic-dataset",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

df
df.info()

# ------------------------------------------------------------------------

## types

### dtypes()
df.dtypes

dfn = df.convert_dtypes()
dfn
dfn.dtypes

### convert_dtypes()
s = pd.Series(["a","b",np.nan])
s
s.convert_dtypes()

## astype
"""
t1 = df['Name']
t1
t1.info()
t2 = df['Name'].astype('object')
t2
t2.info()
"""
t1 = df['Name'].astype("object")
t1.info()

"""
df.info()
Age 열의 dtype이 float 이므로, int로 변환해 메모리 절약을 시도하였다.

t2 = df['Age'].astype("int64")
결과는 nan 때문에 dtype 변환 불가

IEEE 754에 따라 부동소수점의 지수부 비트가 모두 1, 가수부가 0이 아니면 nan.
이는 지수부 최대값 255가 특수값 영역이며 그 중 nan을 규정한 내용.
따라서 float32/64의 Age를 int로 치환 불가하다.
"""

