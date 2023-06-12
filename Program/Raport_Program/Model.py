from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score


# Create a StandardScaler object for feature scaling
SCALER = StandardScaler()


# Function to split the dataset into features and target variables
def split_datasets(dataset):
    results_cols = ['lifeexpectancy']
    prediction_cols = [col for col in dataset.columns if col not in results_cols]
    return dataset[prediction_cols], dataset[results_cols]


# Function to scale the features using the StandardScaler
def scale_features(dataset):
    return SCALER.fit_transform(dataset.astype(float))


# Function to run different regression models and compare their performance
def run_models(X_train, y_train, X_test, y_test):
    # Linear Regression
    regression = LinearRegression()
    regression.fit(X_train, y_train)
    y_pred = regression.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print("Linear Regression:", r2)

    # Random Forest Regression
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print("Random Forest:", r2)

    # MLP Regressor (Neural Network)
    mlp = MLPRegressor(max_iter=5000)
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print("Sieć neuronowa:", r2)

    # Prepare data for plotting
    models = ["Linear Regression", "Random Forest", "Sieć neuronowa"]
    r2_scores = [r2_score(y_test, regression.predict(X_test)),
                 r2_score(y_test, rf.predict(X_test)),
                 r2_score(y_test, mlp.predict(X_test))]
    colors = ["blue", "green", "orange"]

    # Create a bar plot to compare model performance
    plt.bar(models, r2_scores, color=colors)
    plt.xlabel("Model")
    plt.ylabel("Jakość przewidywań")
    plt.title("Porównanie modeli")
    plt.ylim(0.5, 1.0)
    for i, score in enumerate(r2_scores):
        plt.annotate(f"{score:.3f}", (i, score + 0.005), ha='center')
    plt.savefig("Models_scores.jpg")
    plt.show()


if __name__ == "__main__":
    # Define the paths to the train and test data folders
    train_data_folder = Path("2010-2016 (train)/Data_processing")
    test_data_folder = Path("2017 (test)/Data_processing")

    # Read the train and test datasets from CSV files
    train_df = pd.read_csv(train_data_folder / "relevant_data.csv")
    test_df = pd.read_csv(test_data_folder / "relevant_data.csv")

    datasets = [train_df, test_df]

    # Split the train and test datasets into features and target variables
    X_train, y_train = split_datasets(train_df)
    y_train = y_train.values.ravel()

    X_test, y_test = split_datasets(test_df)
    y_test = y_test.values.ravel()

    # Scale the features using the StandardScaler
    X_train = scale_features(X_train)
    X_test = scale_features(X_test)

    # Run the regression models and compare their performance
    run_models(X_train, y_train, X_test, y_test)
