import os
import sys
sys.path.insert(0, 'D:\Text_Summarizer\src')
from logger import *
from exception import CustomException
from constants import *
from utils import *
from entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAM_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(config.root_dir,config.source_url,config.local_data_file,config.unzip_dir)
        return data_ingestion_config