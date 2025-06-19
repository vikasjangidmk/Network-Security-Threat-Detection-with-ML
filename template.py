import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "networksecurity"

list_of_files = [
    ".github/workflows",
    "data_schema",
    "final_model",
    "Network_Data",
    f"{project_name}/cloud/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/main_utils/__init__.py",
    f"{project_name}/utils/ml_utils/metric/__init__.py",
    f"{project_name}/utils/ml_utils/model/__init__.py",
    "prediction_output",
    "templates",
    "valid_data"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != Path(""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not filepath.exists():
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
