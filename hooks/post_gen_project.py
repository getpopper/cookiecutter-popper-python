import os
import shutil

os_license = '{{ cookiecutter.license }}'
notebooks = '{{ cookiecutter['jupyter notebooks'] }}'
data_complexity = '{{ cookiecutter['data processing complexity'] }}'

if os_license == "No license file":
    os.remove("LICENSE")

if notebooks == "No":
    shutil.rmtree("src/notebooks")

if data_complexity == "Less":
    shutil.rmtree('src/data')
    shutil.rmtree('data/raw')
    shutil.rmtree('data/interim')
    shutil.rmtree('data/processed')