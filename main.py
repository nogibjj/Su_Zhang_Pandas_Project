import pandas as pd
import matplotlib.pyplot as plt

# Load the healthcare dataset
health_df = pd.read_csv("healthcare_dataset.csv")


# print the head of the datasets to showcase what variables do the dataset includes
def print_head():
    health_head = health_df.head()
    print(health_head)
    return health_head


# describe the dataset's discrete / continuous variables
def describe_stat():
    health_desc = health_df.describe()
    print(health_desc)
    return health_desc


# use value counts to summary the counts of categorical variables
def group_by(column_name):
    return health_df[column_name].value_counts()


# create a histogram of 'Billing Amount' column in healthcare dataset
def build_histogram():
    plt.hist(
        health_df["Billing Amount"],
        bins=20,
        edgecolor="white",
    )
    plt.xlabel("Billing Amount")
    plt.ylabel("Frequency")
    plt.title("Billing Amount Histogram")
    plt.savefig("Billing_Amount_Hist.png")
    plt.show()


# main to execute the functions.
if __name__ == "__main__":
    print_head()
    describe_stat()
    print(group_by("Blood Type"))
    print(group_by("Medical Condition"))
    print(group_by("Admission Type"))
    print(group_by("Test Results"))
    build_histogram()
