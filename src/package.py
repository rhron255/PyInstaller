import argparse
import json
import os
import subprocess
import sys
import warnings

import pip

CONFIG_FILE_NAME = 'pyinstall_conf.json'
REQUIREMENTS_FILE_NAME = 'requirements.txt'


def make_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", default=".", help="The path of the project to package")
    return parser


def get_config(project_path: str):
    actual_path = os.path.abspath(project_path)
    with open(os.path.join(actual_path, CONFIG_FILE_NAME)) as conf_file:
        return json.load(conf_file)


def validate_project_dir(project_path: str):
    if not os.path.isdir(project_path):
        raise ValueError(f"The project path {project_path} does not exist or is not a directory!")
    project_files = [fileOrDir.name for fileOrDir in os.scandir(project_path) if fileOrDir.is_file()]
    if CONFIG_FILE_NAME not in project_files:
        raise FileNotFoundError(f"The configuration file {CONFIG_FILE_NAME} does not exist in project root!")
    if REQUIREMENTS_FILE_NAME not in project_files:
        warnings.warn(f"The requirements file {REQUIREMENTS_FILE_NAME} does not exist in project root, skipping "
                      f"dependency inclusion!")


def main(project_path: str):
    config = get_config(project_path)
    # subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])


if __name__ == '__main__':
    args = make_argparser().parse_args()
    main(args.project_path)
