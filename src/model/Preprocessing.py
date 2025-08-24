import pandas as pd
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class Preprocessing:
    def __init__(self, data_path: str):
        logging.info(f"Loading data from {data_path}...")
        self.df = pd.read_json(data_path, lines=True)
        logging.info(f"Data loaded: {len(self.df)} rows.")

    def convert_location(self, location: str):
        return self.state_to_region.get(location, None)

    def convert_user_agent(self, ua: str):
        ua = ua.lower()
        if "edg" in ua:
            return "Edge"
        elif "msie" in ua or "trident" in ua:
            return "Internet Explorer"
        elif "firefox" in ua:
            return "Firefox"
        elif "chrome" in ua or "crios" in ua or "chromium" in ua:
            return "Chrome"
        elif "safari" in ua:
            return "Safari"
        else:
            return "Other"

    def feature_extraction(self, data: pd.DataFrame):
        logging.info("Starting feature extraction...")
        data["region"] = data["location"].apply(self.convert_location)
        data["userAgent_processed"] = data["userAgent"].apply(self.convert_user_agent)
        
        cols_to_drop = ["first_name", "last_name", "user_agent", "location"]
        data.drop(columns=[c for c in cols_to_drop if c in data.columns], inplace=True)

        data = data.sort_values(["userId", "ts"])
        data = (
            data.groupby("userId")
            .agg(
                gender=("gender", "first"),
                registration=("registration", "first"),
                region=("region", "last"),
                user_agent=("userAgent_processed", "last"),
                initial_level=("level", "first"),
                final_level=("level", "last"),
                total_sessions=("sessionId", "nunique"),
                total_errors=("status", lambda x: (x >= 400).sum()),
                like_count=("page", lambda x: (x == "Thumbs Up").sum()),
                dislike_count=("page", lambda x: (x == "Thumbs Down").sum()),
                avg_listen_time=("length", "mean"),
                label=("page", lambda x: int(x.isin(["Cancellation Confirmation"]).any())),
            )
            .reset_index()
        )
        data["like_ratio"] = data["like_count"] / (data["like_count"] + data["dislike_count"] + 1e-5)
        data.drop(columns=["like_count", "dislike_count"], inplace=True)
        logging.info("Feature extraction completed.")
        return data

    def clean_data(self, data: pd.DataFrame):
        logging.info("Cleaning data...")
        user_info_cols = ["location", "userAgent", "lastName", "firstName", "registration", "gender"]
        data = data.dropna(subset=user_info_cols)
        data["length"].fillna(0, inplace=True)
        data["artist"].fillna("Unknown", inplace=True)
        data["song"].fillna("Unknown", inplace=True)
        data = data.drop_duplicates()
        logging.info(f"Data cleaned: {len(data)} rows remaining.")
        return data

    def preprocess_data(self):
        logging.info("Loading state to region mapping...")
        with open("assets/state_to_region.json", "r") as f:
            regions = json.load(f)
        self.state_to_region = {state: region for region, states in regions.items() for state in states}
        logging.info(f"Mapping loaded: {len(self.state_to_region)} states.")

        self.df = self.clean_data(self.df)
        self.df = self.feature_extraction(self.df)
        logging.info("Preprocessing completed.")
        return self.df
