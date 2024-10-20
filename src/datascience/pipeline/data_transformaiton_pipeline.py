from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = " Data Transformation Stage "

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_data_transformation(self):
        #we are intrigating try except here to check ([-1] means true value in status file) if validation properly done


        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
                print(status)
            if status=="True":    
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                # Calling the funciton from data_transformation.py 
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")    
        except Exception as e:
            print(e)    