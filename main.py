"""
Main entry point for the LLM Report System
"""

import os
from dotenv import load_dotenv
import argparse
from src.config.settings import settings
from src.agents import main_workflow1,main_workflow2

save_path__bs = settings.BS_DIR

if __name__ == "__main__":

    # Remove prior artifacts
    l_path = [settings.PLOT_DIR, settings.DF_DIR, settings.JSON_DIR]
    for folder_path in l_path:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    bs_name = save_path__bs / '''bs_question.txt'''
    with open(bs_name, 'r') as f:
        lines = f.readlines()
    # Remove newline characters
    l_business_question = [line.strip() for line in lines if len(line.strip()) >= 10]

    for enum,_bs in enumerate(l_business_question):
        enum=enum+1
        # Try for 3 times. This is due to there could be a bug due to plot generation.
        for attempt in range(3):
            try:
                main_workflow1(_bs,enum)
                break  # success → stop retrying
            except Exception as e:
                if attempt == 2:  # after 3rd try, re-raise or handle
                    raise
    main_workflow2()


