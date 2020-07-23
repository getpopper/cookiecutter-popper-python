import os
import shutil

os_license = '{{ cookiecutter.license }}'
notebooks = '{{ cookiecutter['jupyter notebooks'] }}'
containers = '{{ cookiecutter.containers }}'

if os_license == "No license file":
    os.remove("LICENSE")

if notebooks == "No":
    shutil.rmtree("src/notebooks")