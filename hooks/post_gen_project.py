import os
import shutil

os_license = '{{ cookiecutter.license }}'
notebooks = '{{ cookiecutter['jupyter notebooks'] }}'

if os_license == "No license file":
    os.remove("LICENSE")

if notebooks == "No":
    shutil.rmtree("src/notebooks")