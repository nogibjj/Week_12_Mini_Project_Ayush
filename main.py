# Importing required libraries
import mlflow
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def main():
    # Reading the data
    df = pandas.read_csv("C:\\Users\\ayush\\Week_12_Mini_Project_Ayush\\Master.csv")

    # Preprocessing the data
    df = df.dropna()
    df = df[df["price"] != "?"]
    df = df[df["engine-size"] != "?"]
    df = df[df["horsepower"] != "?"]

    # Selecting features and target
    features = df[["engine-size", "horsepower"]]
    target = df["price"]

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    # Fitting the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Making predictions
    y_pred = model.predict(X_test)

    # Calculating R-squared score
    r2 = r2_score(y_test, y_pred)

    # Logging the model and metrics usingn MLFlow
    with mlflow.start_run():
        mlflow.log_param("model", "LinearRegression")
        mlflow.log_param("data_path", "Data/Master.csv")

        mlflow.log_metric("R-Squared", r2)

        mlflow.sklearn.log_model(model, "mlruns/0")


if __name__ == "__main__":
    main()
