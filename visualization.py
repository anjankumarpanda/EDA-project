import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):

    # Salary Distribution
    plt.figure(figsize=(6,4))
    sns.histplot(data["Salary"], bins=5)
    plt.title("Salary Distribution")
    plt.show()

    # Department Count
    plt.figure(figsize=(6,4))
    sns.countplot(x="Department", data=data)
    plt.title("Department Count")
    plt.show()

    # Age vs Salary
    plt.figure(figsize=(6,4))
    sns.scatterplot(x="Age", y="Salary", data=data)
    plt.title("Age vs Salary")
    plt.show()