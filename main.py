import argparse
import logging
from src.model.Preprocessing import Preprocessing

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


def main(train_path: str, test_path: str):
    df_train = Preprocessing(train_path).preprocess_data()
    df_test = Preprocessing(test_path).preprocess_data()
    df_train.to_json("processed_train_data.json", lines=True, orient="records")
    df_test.to_json("processed_test_data.json", lines=True, orient="records")
    logging.info("Prepared data saved successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Customer churn pipeline")
    parser.add_argument(
        "--train", type=str, required=True, help="Path to the train data file"
    )
    parser.add_argument(
        "--test", type=str, required=True, help="Path to the test data file"
    )

    args = parser.parse_args()
    main(args.train, args.test)
