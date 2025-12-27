"""
Main entry point for Result Evaluation
"""

import os
from dotenv import load_dotenv
import argparse
from src.config.settings import settings
from eval import report_evaluation,finding_evaluation
import json
import pandas as pd


REPORT_NAME = settings.REPORT_NAME
save_path__json = settings.JSON_DIR
INFO_NAME = save_path__json / 'info.json'
save_path__bs = settings.BS_DIR
save_path__eval = settings.EVAL_DIR

### These are choices of evaluation
l_metric=['coherence','conciseness','coverage','faithfulness']

if __name__ == "__main__":
    bs_name = save_path__bs / '''bs_question.txt'''
    with open(bs_name, 'r') as f:
        lines = f.readlines()
    # Remove newline characters
    l_business_question = [line.strip() for line in lines if len(line.strip()) >= 10]
    l_business_question = [f'{enum+1}, {i}' for enum,i in enumerate(l_business_question)]


    ### Report Evaluation
    if os.path.exists(REPORT_NAME):
        print("Report exists")
        human_input1 = 'The following is the report, please perform coherence evaluation:'
        report_coherence_eval_res = report_evaluation('coherence',human_input1)
        print(report_coherence_eval_res)
    #     human_input2 = 'The following is the report, please perform conciseness evaluation:'
    #     report_conciseness_eval_res = report_evaluation('conciseness', human_input2)
    #     human_input3 =  f'''The following are the business questions for coverage evaluation:\n{'\n'.join(l_business_question)}\n\nThe following  is the report, please perform coverage evaluation:'''
    #     report_coverage_eval_res = report_evaluation('coverage', human_input3)
    #
    #     with open(save_path__eval / 'report_coherence_eval.txt', "w") as file:
    #         file.write(report_coherence_eval_res)
    #     with open(save_path__eval / 'report_conciseness_eval.txt', "w") as file:
    #         file.write(report_conciseness_eval_res)
    #     with open(save_path__eval / 'report_coverage_eval.txt', "w") as file:
    #         file.write(report_coverage_eval_res)
    # else:
    #     print("Report does not exist")
    #
    # ### Finding Evaluation (Faithfulness)
    # if os.path.exists(INFO_NAME):
    #     print("info.json artifact exists")
    #
    #     with open(INFO_NAME, 'r') as f:
    #         _dict = json.load(f)
    #     l_report_faithfulness_eval_res = []
    #
    #     ### Perform evaluation for each subtask
    #     for k, v in _dict.items():
    #         bs = k
    #         l_subtask = v.get('subtask_artifact')
    #         for subtask in l_subtask:
    #             subtask_no = subtask.get('subtask_no')
    #             subtask_desc = subtask.get('subtask')
    #             finding = subtask.get('finding')
    #             df = pd.read_pickle(subtask.get('df'))
    #             human_input4 = f'''The following are the findings and relevant data. Please perform faithfulness evaluation.\n\n### Finding:\n{finding}\n\n### Data:\n{df}'''
    #             report_faithfulness_eval_res = finding_evaluation('faithfulness', human_input4)
    #             l_report_faithfulness_eval_res.append([bs, subtask_no, subtask_desc] + report_faithfulness_eval_res)
    #
    #     with open(save_path__eval / 'finding_faithfulness_eval.txt', "w") as file:
    #         file.write(l_report_faithfulness_eval_res)
    # else:
    #     print("info.json artifact does not exist")





