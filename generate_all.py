import shutil
from dotenv import load_dotenv
import os
import pathlib
from tqdm import tqdm

if __name__ == "__main__":
    load_dotenv()

    # Read cluster info from environment
    data_directory = os.getenv("DATA_DIR")
    source_directory = pathlib.Path(os.getcwd(), data_directory)
    destination_directory = pathlib.Path(os.getcwd(), "smalltravelsample/docs")

    # Delete existing files from the destination_directory
    print("Deleting existing files in the output folder")
    for file_to_delete in destination_directory.glob("*.json"):
        try:
            file_to_delete.unlink()
        except Exception as e:
            print(f"Failed to delete file {file_to_delete}", e)

    # Deleting archive if it exists
    destination_archive = pathlib.Path(destination_directory, "smalltravelsample.zip")
    if os.path.exists(destination_archive):
        os.unlink(destination_archive)

    print("Exporting documents")
    # Copy files from data_directory to destination_directory
    for file_to_copy in tqdm(list(source_directory.glob("inventory.*.json"))):
        # Change the destination scope to samples from inventory
        destination_file_name = file_to_copy.name.replace("inventory", "samples")
        try:
            shutil.copy(
                file_to_copy, pathlib.Path(destination_directory, destination_file_name)
            )
        except Exception as e:
            print(f"Exception while copying file {file_to_copy}", e)

    print("Exporting to archive")
    try:
        shutil.make_archive("smalltravelsample", "zip", "smalltravelsample")
    except Exception as e:
        print(f"Exception while creating the archive", e)

    print("Exported to smalltravelsample.zip")
