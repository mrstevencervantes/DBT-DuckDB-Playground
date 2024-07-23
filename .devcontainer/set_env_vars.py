import os
import subprocess
from pathlib import Path
from typing import Union, Final

from dotenv import load_dotenv

def load_env_vars(env_file: str=".devcontainer/.env.devcontainer", 
        profile: str="~/.bashrc", 
        dbt_workspace:str | None=None,
        db_name: str | None=None,
    ):
    # Set variables for later use
    found: bool = False
    # Check if env_file exists
    if Path(env_file).exists():
        found = True
        print("Environment settings file found, continue processing.")
    else:
        print("Environment settings file was not found, unable to set variables.")
        
    if found:
        print("Start setting environment variables...")
        load_dotenv(env_file, override=True)

        # Set environment variables
        env_vars: dict[str, Union[str, Path]] = {
            "DB_NAME": os.environ.get("DBNAME", db_name),
            "DBT_PROFILES_DIR": Path.cwd()
        }

        BASH_PROFILE: Final[str] = os.path.expanduser(profile)

        for key, value in env_vars.items():
            subprocess.run(
                f'echo "export {key}={value}" >> {BASH_PROFILE}', shell=True, check=True
            )

        subprocess.run(f". {BASH_PROFILE}", shell=True, check=True)
        print("Environment variables set successfully.")
    
if __name__ == '__main__':
    print("Starting file...")
    load_env_vars()
    print("File complete.")
