import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO )

project_name ='dsproject'
list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/dsproject/__init__",
    f"src/dsproject/components/data_ingestion.py",
    f"src/dsproject/components/data_transformation.py",
    f"src/dsproject/components/model_trainer.py",
    f"src/dsproject/components/data_monitoring.py",
    f"src/dsproject/pipelines/__init__.py",
    f"src/dsproject/pipelines/training_pipeline.py",
    f"src/dsproject/pipelines/prediction_pipeline.py",
    f"src/dsproject/exception.py",
    f"src/dsproject/logger.py",
    f"src/dsproject/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for teh file {filename}")

    if (not os.path.exists(filepath) )or( os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file :{filepath}")        
            
    else:
        logging.info(f"{filename} is already exists")