import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) ->ConfigBox:
    """Method use to open and read the yaml file.
    
    Args: 
        path_to_yaml(str): takes the path of the yaml file is present

    Raises:
        ValueError: if yaml file is empty
        e: empty

    Returns:
         ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_yaml) as file:
            content=yaml.safe_load(file)
            logger.info(f"yam file {path_to_yaml} is loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e
    
    @ensure_annotations
    def create_dictories(path_to_directories: list, vervose=True):
        """Create list of directories
        Args:
            path_to_directories: list of directories

        """
        for path in path_to_directories:
            os.makedirs(path, exist_ok= True)
            if vervose:
                logger.info(f"Created directories at {path}")
    
    @ensure_annotations
    def save_json(path: Path, data: dict):
        """Jsave son file/data
         Args:
            path: path to json file
            data: data/file you want to save 
        """
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

    @ensure_annotations
    def load_json(path: Path)->ConfigBox:
        """load the json file
        
        Args:
            path of the json file
        
        Retruns: the ConfigBox
        """
        with open(path) as file:
            content=json.load(file)
        
        logger.info("Json file is succesfully load")
        return ConfigBox(content)
    
    @ensure_annotations
    def save_bin(data: Any, path: Path):
        """Save as binary file
        Args:
            data(Any): data to be saved as binary
            path(Path): save in the directory
        """
        joblib.dump(value=data, filename=path)

    @ensure_annotations
    def load_bin(path: Path) -> Any:
        """Load binary data"""
        data=joblib.load(path)
        return data
    
    @ensure_annotations
    def get_size(path: Path)->str:
        """get file size in KB
        Args:
            path: path of the file
        Return: 
            get the file in KB
        """
        size_in_kb=round(os.path.getsize(path)/1024)
        return f'~{size_in_kb} kb'

    def decodeImage(imgstring, filename):
        imgdata=base64.b64decode(imgstring) 
        with open(filename,'wb') as file:
            file.write(imgdata)
            file.close()
    
    def encodeImageIntoBase64(croppedImagePath):
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())