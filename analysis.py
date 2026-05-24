def analyze_data(data):

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nDataset Information:")
    print(data.info())

    print("\nStatistical Summary:")
    print(data.describe())

    print("\nCorrelation:")
    print(data.corr(numeric_only=True))