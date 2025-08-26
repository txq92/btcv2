#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration example file for Advanced Crypto Signal Detector

Copy this file to config.py and update with your actual values.
"""

# ============== TELEGRAM CONFIGURATION ==============
# Get your bot token from @BotFather on Telegram
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

# Get your chat ID by messaging your bot and visiting:
# https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"

# ============== MONGODB CONFIGURATION ==============
# MongoDB connection string
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"

# Database and collection names
MONGO_DATABASE = "crypto_trading"
MONGO_COLLECTIONS = {
    "signals": "trading_signals",
    "results": "signal_results", 
    "market_data": "market_analysis"
}

# Enable/disable MongoDB features
ENABLE_MONGODB = True  # Set to False to run without MongoDB

# ============== TRADING PARAMETERS ==============
# Symbols to monitor
SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT", 
    "SUIUSDT",
    "SOLUSDT"
]

# Symbol-specific Risk/Reward settings
SYMBOL_SPECIFIC_RR = {
    "BTCUSDT": {
        "min_rr": 1.2,           # Minimum Risk:Reward ratio
        "risk_percent": 1.0,     # Risk percentage per trade
        "atr_sl_mult": 1.2,      # ATR multiplier for stop loss
        "atr_tp_mult": 2.5       # ATR multiplier for take profit
    },
    "ETHUSDT": {
        "min_rr": 1.5,
        "risk_percent": 0.8,
        "atr_sl_mult": 1.5,
        "atr_tp_mult": 3.0
    },
    "SUIUSDT": {
        "min_rr": 1.8,
        "risk_percent": 0.5,
        "atr_sl_mult": 1.8,
        "atr_tp_mult": 3.5
    },
    "SOLUSDT": {
        "min_rr": 1.8,
        "risk_percent": 0.5,
        "atr_sl_mult": 1.8,
        "atr_tp_mult": 3.5
    }
}

# ============== OPERATIONAL PARAMETERS ==============
# Time intervals and limits
INTERVAL = "3m"              # Primary timeframe
LIMIT = 120                  # Number of candles to fetch
LOOP_SLEEP_SECONDS = 15      # Sleep between main loops

# Filtering options
MTF_CONFIRM = True           # Require 15m timeframe confirmation
SEND_IMAGES = True           # Send chart images with signals
VOLUME_THRESHOLD = 1.2       # Volume ratio for confidence boost
VOLATILITY_THRESHOLD = 2.0   # High volatility threshold

# API timeouts and delays
API_TIMEOUT = 20             # Binance API timeout (seconds)
TELEGRAM_TIMEOUT = 10        # Telegram API timeout (seconds)
RETRY_DELAY = 10             # Wait time between retries (seconds)
SYMBOL_DELAY = 1             # Delay between processing symbols (seconds)

# ============== PERFORMANCE REPORTING ==============
# Send performance reports every N hours
PERFORMANCE_REPORT_INTERVAL = 6  # Hours

# Performance reporting periods
PERFORMANCE_REPORT_DAYS = 7      # Days to analyze for reports
