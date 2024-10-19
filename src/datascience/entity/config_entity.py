from dataclasses import dataclass
from pathlib import Path

# variables from Config yaml file 
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path