#!/bin/bash

# Activate your conda env
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh
conda activate test_webapp

# Run your Streamlit app
streamlit run /Users/samala2/Documents/test_webapp/plot_streamlit/main.py

