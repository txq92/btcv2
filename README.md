# 🚀 Advanced Crypto Signal Detector

An intelligent cryptocurrency trend detection system with advanced technical analysis and automated Telegram notifications.

## 🌟 Features

- **Multi-timeframe Analysis**: 3-minute and 15-minute trend confirmation
- **Advanced Technical Indicators**: EMA, RSI, MACD, Stochastic RSI, Bollinger Bands, ATR
- **Signal Detection**: 
  - Break of Structure (BOS)
  - RSI Divergence  
  - Engulfing patterns
  - EMA/MACD crossovers
  - Bollinger Band breakouts/bounces
- **Volume Profile Analysis**: POC, Value Area, High Volume Nodes
- **Market Structure Analysis**: Swing patterns, confluence levels
- **Risk Management**: Dynamic Stop Loss/Take Profit with multiple levels
- **MongoDB Integration**: Signal storage and performance tracking
- **Telegram Notifications**: Real-time signals with detailed analysis

## 📊 Supported Symbols

- BTCUSDT
- ETHUSDT
- SUIUSDT
- SOLUSDT

## 🔧 Configuration

### Environment Variables
Update the following in `btc_trend_3m.py`:

```python
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# MongoDB Configuration (optional)
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
ENABLE_MONGODB = True  # Set to False to disable MongoDB
```

### Symbol-specific Risk/Reward Settings
```python
SYMBOL_SPECIFIC_RR = {
    "BTCUSDT": {"min_rr": 1.2, "risk_percent": 1.0},
    "ETHUSDT": {"min_rr": 1.5, "risk_percent": 0.8},
    "SUIUSDT": {"min_rr": 1.8, "risk_percent": 0.5},
    "SOLUSDT": {"min_rr": 1.8, "risk_percent": 0.5}
}
```

## 🚀 Running the Application

### Option 1: Direct Python
```bash
# Install dependencies
pip install -r requirements.txt

# Run the detector
python btc_trend_3m.py
```

### Option 2: Docker Compose (with MongoDB)
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f crypto-detector

# Stop services
docker-compose down
```

### Option 3: Docker (standalone)
```bash
# Build image
docker build -t crypto-detector .

# Run container
docker run -it --name crypto-detector crypto-detector
```

## 📈 Signal Types

### Long Signals
- **STRONG LONG**: bias_score ≥ 4, confidence 70-95%
- **LONG**: bias_score ≥ 2, confidence 60-85%

### Short Signals  
- **STRONG SHORT**: bias_score ≤ -4, confidence 70-95%
- **SHORT**: bias_score ≤ -2, confidence 60-85%

### Hold
- **HOLD**: Mixed signals, wait for clearer direction

## 📊 Signal Quality Filters

- **Risk/Reward Ratio**: Symbol-specific minimum thresholds
- **Multi-timeframe Alignment**: 3m and 15m trend confirmation
- **Enhanced Confidence**: Market structure + volume profile analysis
- **Volume Confirmation**: Above/below average volume analysis
- **Signal Confluence**: Multiple indicators alignment

## 💡 Telegram Message Format

```
🚨 BTCUSDT BOS Signal
📊 Direction: LONG | Confidence: 85%
⏰ 2024-01-26 18:45:00

📈 TRADE SETUP:
💰 Entry: 45,250.00
🔴 Stop Loss: 44,800.00 (1.0%)
🎯 TP1: 46,200.00 (+2.1%)
🎯 TP2: 46,800.00 (+3.4%) 
🎯 TP3: 47,500.00 (+5.0%)

📊 Risk:Reward = 1:2.11
🎯 Strategy: Enhanced_Swing_ATR

📈 MARKET ANALYSIS:
🕐 3m Trend: UPTREND | 15m: UPTREND
📋 Current: 45,250.00 | EMA50: 45,100.00 | RSI: 58.5
🔍 🔥 High Volume | 🏗️ EXCELLENT | 📊 Near POC
```

## 📁 Project Structure

```
btc_chart-main/
├── btc_trend_3m.py      # Main application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Multi-service setup
├── .gitignore          # Git ignore rules
├── start_server.png    # Startup notification image
└── README.md           # This file
```

## 🛡️ Security Notes

- Keep your Telegram bot token secure
- Use environment variables for sensitive data in production
- MongoDB connection should be secured in production environments

## 🔄 Performance Monitoring

The system automatically sends performance reports every 6 hours including:
- Overall win rate and R:R statistics
- Long vs Short signal performance
- Symbol-specific performance metrics
- Strategy recommendations

## ⚠️ Disclaimer

This tool is for educational and research purposes. Always do your own research and risk management before making trading decisions.
