
Su Zhang Pandas Project - IDS706 Week2 Assignment
This project is aimed to analyze dataset on patients healthcare records, which includes patient age, gender, blood type, medical condition, billing amount, medication etc . Please note that these data are not real-world data and just for descriptive data practice. This project primarily used Pandas and Matplotlib packages to analyze the distribution of billing amount, summary statistics (mean, median, max, standard variation) of billing amount and age. For the categorical variables, such as blood type, medical condition, admission type, and test resultsm, this project also showcased the distribution of subcategories in tables. 

Source of data: https://www.kaggle.com/datasets/prasad22/healthcare-dataset/data

Project Structure

├── .devcontainer/
│   ├── devcontainer.json   # Set up development environment in Github Codespace.
│   └── Dockerfile          # Defines the base environment (such as what tools and libraries are installed).
├── .github/
│   └── workflows/cicd.yml  # Describes the steps and jobs that GitHub should run automatically. In this project, this includes installing dependencies and packages, lint, format, and test.
├── main.py                 # Main application script: read the input data csv and create functions to print out first few rows of dataset, summarize the key statistics, build histogram for specific data category
├── test_main.py            # Tests if the functions defined in main.py work normally
├── requirements.txt        # Specify Python dependencies needed for this project. For this project, added packages of pandas and matplotlib.
├── Makefile                # Build automation commands: in this project, commands mainly include install, format, lint, and test.
├── healthcare_dataset.csv  # Input dataset on patients healthcare records
├── Billing_Amount_Hist.png # Output histogram graph demonstrating the distribution of billing amount
├── Data_Summary.pdf        # Output pdf generated from Jupyter Notebook to showcase the analysis output
└── README.md               # Project documentation to offer an overview of the project
