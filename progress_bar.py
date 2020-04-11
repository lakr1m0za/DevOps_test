#progress bar
#pip install tqdm

from tqdm import tqdm
from time import sleep

fir i in tqdm(range(10)):
    sleep(0.2)