# cookiecutter-popper-python

Cookiecutter template for research projects in Python on the 
[Popper](https://github.com/getpopper/popper) workflow execution engine. 

The goal is to provide a  structure for developing 
reproducible projects in computational research (machine learning, statistics, bioinformatics, ...)
following best practices in a container-native environment.

Resource:
- A guide for developing Python workflows for computational research with Popper is available in the
 [Popper documentation](https://popper.readthedocs.io/en/latest/sections/guides.html).
- An example project following this structure is available at [popper-examples](https://github.com/getpopper/popper-examples/tree/master/workflows/comp-research/python).

## Requirements

- Python >= 3.5
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/advanced/directories.html) >= 1.1

Additionally, to run the generated project:

- Popper
- Docker

## Generated project structure

```
├── LICENSE
├── README.md                       <- The top-level README.
├── data                            <- Data used in workflow.
├── paper                           <- Generated paper as PDF, LaTeX.
├── containers                      <- Definitions of containers used in workflow
|   └── exploration                 <- Container used for exploratory work. 
|       ├── exploration.dockerfile  <- Default dockerfile used in workflow.
|       └── exploration_env.yml     <- Defines conda environment used by container.
├── results
|   ├── models                      <- Model predictions, serialized models, etc.        
|   └── figures                     <- Graphics created during workflow.
└── src                             <- Source code for this project.
    ├── notebooks                   <- Jupyter notebooks.
    ├── data                        <- Scripts to download or generate data.
    ├── models                      <- Scripts used to generate models.
    └── figures                     <- Scripts to generate graphics.
```

This project takes inspiration from Driven Data's 
[cookiecutter-data-science](https://drivendata.github.io/cookiecutter-data-science/), adapting their approach for use with Popper.