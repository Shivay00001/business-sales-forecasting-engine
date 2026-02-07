import pandas as pd
from prophet import Prophet
import logging

class SalesForecaster:
    def __init__(self):
        self.model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
        self.is_fitted = False

    def fit(self, df):
        """
        Fits the Prophet model.
        df must have 'ds' (date) and 'y' (value) columns.
        """
        try:
            if not {'ds', 'y'}.issubset(df.columns):
                raise ValueError("DataFrame must contain 'ds' and 'y' columns")
            
            self.model.fit(df)
            self.is_fitted = True
        except Exception as e:
            logging.error(f"Error fitting model: {e}")
            raise

    def predict(self, periods=30):
        """Generates forecasts for the next N days."""
        if not self.is_fitted:
            raise RuntimeError("Model is not fitted. Call fit() method first.")
            
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast
