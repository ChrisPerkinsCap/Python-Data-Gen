import os
from pathlib import Path

source_dir = "/Users/chris/Dev/Python-Data-Gen/CSV/"

# with os.scandir(source_dir) as files:
#     for file in files:
#         print(file.name)

files = Path(source_dir)
for file in files.iterdir():
    print(file.name)