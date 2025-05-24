#!/bin/bash

# Load Conda environment
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh
conda activate test_webapp

# Navigate to your app directory
cd /Users/samala2/Documents/test_webapp/plot_streamlit || exit

# Pull latest code
git pull origin main

# Kill any existing Streamlit app (optional but recommended)
pkill -f "streamlit run"

# Wait briefly to ensure it's stopped
sleep 2

# Restart the Streamlit app in background
nohup streamlit run main.py > streamlit.log 2>&1 &
