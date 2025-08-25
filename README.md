# Customer Churn Prediction

This project predicts customer churn by utilizing historical data and machine learning techniques. The goal is to provide an automated pipeline that ensures the effectiveness of the production model.

## Project Roadmap

This project is taking more time than I expected, so you can follow the plan and current status here.

---

| Step | Title                               | Target                                                                                                                                   | Status        |
|------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| 1    | Project Setup                       | Set up the project using `uv` / `make` / `ruff` and other tooling.                                                                       | Done          |
| 2    | Data Exploration                    | Problem understanding and exploratory data analysis (EDA).                                                                               | Done          |
| 3    | Preprocessing                       | Prepare and clean the data for model training and evaluation.                                                                            | In Progress   |
| 4    | Train Model                         | Train ML models (e.g., Logistic Regression / Random Forest) and log them with MLflow (optimize for F1-score).                            | ToDo          |
| 5    | Error Analysis                      | Evaluate model behavior using confusion matrix and misclassified examples for further improvements.                                      | ToDo          |
| 6    | Data Drift & Concept Drift Detection| Integrate Evidently to generate drift reports (HTML/JSON). (Still exploring how to implement this step.)                                | ToDo          |
| 7    | Periodic Retraining                 | 1. Load new incoming data (possibly via API).<br>2. Run `preprocessing.py`.<br>3. Retrain the model.<br>4. Evaluate & check for drift.<br>5. Register updated model in MLflow. | ToDo          |
| 8    | Model Deployment (API)              | Use FastAPI to serve the model. Plan to define separate routes for different tasks (e.g., prediction, drift report).                     | ToDo          |
| 9    | Dockerfile                          | Set up the Docker environment and push the image to Docker Hub.                                                                          | ToDo          |

---

## Project Structure

```plaintext
.
├── LICENSE
├── main.py
├── Makefile
├── pyproject.toml
├── README.md
├── uv.lock
├── artifacts
│   └── data
│       ├── customer_churn_mini.json
│       ├── customer_churn.json
│       ├── test_data.json   (generated from data_split.ipynb)
│       └── train_data.json  (generated from data_split.ipynb)
├── research
│   └── data_exploration.ipynb
└── src
    ├── __init__.py
    ├── assets
    │   └── state_to_region.json
    └── model
        ├── __init__.py
        └── preprocessing.py
```

## Requirements

- **Environment:**  
  The project runs with `make` and is only supported on Linux/macOS platforms.  
  If you are using another platform, check the `Makefile` content and run the instructions manually in your terminal.

- **Tools for Development:**  
  - **Ruff:** For linting and formatting.  
  - **Pre-commit:** For running hooks before commits.  

  Install these tools via:
  ```sh
  make precode
  ```

- **Dependencies:**  
  All dependencies are configured in [pyproject.toml](pyproject.toml). Install them with:
  ```sh
  make install
  ```
  This command synchronizes the required packages.

## How to Use

1. **Set Up Development Tools**  
   Install and configure the required tools (Ruff and pre-commit):
   ```sh
   make precode
   ```

2. **Install Dependencies**  
   Run the following command:
   ```sh
   make install
   ```

4. **Splitting the data**
   Download datafiles into `artifacts/data`, then run instructions inside:
   ```sh
   data_split.ipynb
   ```



5. **Running the Application**  
   Execute the main entry point:
   ```sh
   make run
   ```

## Additional Notes

- **Artifacts and Data:**  
  You need to download the dataset files into the `artifacts/data` directory.  
  They are not uploaded here due to GitHub storage limitations.

- **Code Quality and Formatting**  
   - Run the linter:
     ```sh
     make lint
     ```
   - Format the code:
     ```sh
     make format
     ```
   - Run pre-commit hooks:
     ```sh
     make precommit
     ```

- **Project Status:**  
  I will ensure finishing this project as soon as possible.  
  Feel free to provide feedback via email: **nooramerq0@gmail.com**
