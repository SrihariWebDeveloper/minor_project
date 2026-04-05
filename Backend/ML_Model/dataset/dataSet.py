from kaggle.api.kaggle_api_extended import KaggleApi

import pandas as pd

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    "pratikjadhav05/indian-weather-data",
    path="dataset",
    unzip=True
)

print("Dataset Downloaded")