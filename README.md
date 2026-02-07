# Business Sales Forecasting Engine

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Prophet](https://img.shields.io/badge/Prophet-1.1-red.svg)](https://facebook.github.io/prophet/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade sales forecasting engine** leveraging Facebook Prophet for accurate time-series predictions. This repository provides a scalable service for ingesting historical sales data, accounting for seasonality and holidays, and generating reliable revenue forecasts.

## 🚀 Features

- **Advanced Forecasting**: Utilizes Prophet's additive regression model for non-linear trends with yearly, weekly, and daily seasonality.
- **Seasonality Handling**: Automatically detects and adjusts for holiday effects and custom business cycles.
- **API-First Design**: REST API for submitting sales history and retrieving future projections.
- **Interactive Visualization**: Generates plot components for trend, weekly, and yearly seasonality analysis.
- **Robust Preprocessing**: Handles missing data and outliers in time-series datasets.
- **Containerized**: Deployable via Docker for consistent forecasting environments.

## 📁 Project Structure

```
business-sales-forecasting-engine/
├── src/
│   ├── forecasting/  # Prophet model wrapper
│   ├── api/          # FastAPI route handlers
│   └── main.py       # Application entrypoint
├── data/             # Sample sales timeseries (CSV)
├── tests/            # Model accuracy and API tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/business-sales-forecasting-engine.git

# Install
pip install -r requirements.txt

# Run API
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## 📄 License

MIT License
