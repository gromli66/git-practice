import pandas as pd
import logging
from dotenv import load_dotenv
import os

load_dotenv()
DATA_RAW_DIR = os.getenv("DATA_RAW_DIR", "data/raw")


logger = logging.getLogger(__name__)

def load_csv(path):
    logger.debug(f'Attenpting')
    logger.info('Ladding')
    df = pd.read_csv(path, parse_dates=['timestamp'])
    logger.info(f'download {len(df)} rows')
    return df


