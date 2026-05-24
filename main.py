from src.load_data import load_dataset
from src.cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import visualize_data

# Step 1: Load Dataset
data = load_dataset()

# Step 2: Clean Dataset
data = clean_data(data)

# Step 3: Analyze Dataset
analyze_data(data)

# Step 4: Visualize Dataset
visualize_data(data)