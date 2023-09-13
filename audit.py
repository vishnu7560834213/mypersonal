import os
import shutil
from datetime import datetime
from pathlib import Path

source_dir = "/path/to/source/directory"
archive_dir = "/path/to/audit/directory"
current_date = datetime.now().strftime("%Y%m%d")

source_path = Path(source_dir)
archive_path = Path(archive_dir)

for source_file in source_path.glob("*.logs"):
    application_name = source_file.stem.split("_logs_")[0]
    new_file = f"archive_{application_name}_logs_{current_date}.logs"
    dest_file = archive_path / new_file

    try:
        source_file.rename(dest_file)
        print(f"Moved and renamed: {source_file} -> {dest_file}")
    except Exception as e:
        print(f"Error moving {source_file}: {str(e)}")

