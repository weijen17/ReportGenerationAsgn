
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import init_chat_model
import os
import pandas as pd
from pathlib import Path
import json
from pydantic import BaseModel, Field
from typing import List

from src.config.settings import settings
from src.assets.prompts import system_prompt__data_desc,system_prompt__python_exec,system_prompt__python_plot,system_prompt__planner,system_prompt__subtask_finding,system_prompt__finding_consolidation,system_prompt__plot_selection,system_prompt__report_generation


save_path__df = settings.DF_DIR
save_path__plot = settings.PLOT_DIR
save_path__json = settings.JSON_DIR
save_path__report = settings.REPORT_DIR
save_path__raw_data = settings.RAW_DATA_DIR

REPORT_NAME = settings.REPORT_NAME

llm = init_chat_model(model=settings.MODEL_NAME, model_provider=settings.MODEL_PROVIDER, temperature=settings.TEMPERATURE,top_p=settings.TOP_P)

########################################################################################################################
### Phase1: Task Planning

class PlannerOutput(BaseModel):
    tasks: List[str] = Field(description="List of tasks to perform")


def planner_module(var_bs_question):
    # llm_with_structure  = llm.with_structured_output(PlannerOutput)
    planner_response = llm.invoke([SystemMessage(content=system_prompt__data_desc),
                                   SystemMessage(content=system_prompt__planner),
                                   HumanMessage(content=var_bs_question)])

    l_task = planner_response.content
    l_task = eval(l_task)
    return l_task


def subtask_module(task,task_enum,bs_no,l_subtask_artifact):
    task_no = task_enum
    task_response = llm.invoke([SystemMessage(content=system_prompt__data_desc),
                           SystemMessage(content=system_prompt__python_exec),
                           HumanMessage(content=task)])
    task_cmd = task_response.content

    ##################################################################
    ### Phase2: Compute required data for subtask, and save it as pickle
    def execute_llm_query(query):
        # Initialize namespace with required imports
        namespace = {'pd': pd, '__builtins__': __builtins__}
        # Execute the query
        exec(query, namespace)
        # Extract all DataFrames created (filter out imports and builtins)
        results = {}
        for var_name, var_value in namespace.items():
            if not var_name.startswith('_') and var_name != 'pd':
                results[var_name] = var_value
        return results

    tmp_table_name = task_cmd.split(';')[-1].split('=')[0].strip()
    save_df_name = save_path__df / f'''bs{bs_no}_task{task_no}.pkl'''
    save_df_name=save_df_name.as_posix()

    task_cmd2 = task_cmd + f'''; {tmp_table_name}.to_pickle("{save_df_name}")'''

    query_res = execute_llm_query(task_cmd2)
    # Access results dynamically
    for var_name, var_value in query_res.items():
        print(f"{var_name}: {(var_value)}")

    plot_df_name = var_name
    plot_df_value = var_value

    ##################################################################
    ### Phase3: Plot graph for subtask, and save it

    plot_input = f'''The dataframe name is {plot_df_name}, please use this dataframe name as your data. The exact table is as follows: \n{plot_df_value}'''
    plot_response = llm.invoke([SystemMessage(content=system_prompt__python_plot),
                            HumanMessage(content=plot_input)])
    plot_cmd = plot_response.content
    plot_cmd2=plot_cmd.replace(';','\n')
    # print(plot_cmd2)

    save_plot_name = save_path__plot / f'''bs{bs_no}_task{task_no}.png'''
    save_plot_name=save_plot_name.as_posix()
    full_plot_cmd = task_cmd+';'+plot_cmd+f';plt.savefig("{save_plot_name}", dpi=300, bbox_inches="tight")'+';plt.close()'

    plot_res = execute_llm_query(full_plot_cmd)
    for var_name, var_value in plot_res.items():
        print(f"{var_name}: {(var_value)}")

    ##################################################################
    ### Phase4: Generate finding for subtask
    subfinding_input = f'The task is {task}. \n\n The corresponding data is as follows:\n {plot_df_value}'
    subfinding_response = llm.invoke([SystemMessage(content=system_prompt__data_desc),
                                SystemMessage(content=system_prompt__subtask_finding),
                                HumanMessage(content=subfinding_input)])
    subfinding_res = subfinding_response.content
    l_subtask_artifact.append({'subtask_no':task_no,'subtask':task,'finding':subfinding_res,'df':save_df_name,'plot':save_plot_name})
    return l_subtask_artifact



def overall_finding_module(l_subtask_artifact,var_bs_question):
    ##################################################################
    ### Phase5: Consolidate and sort out subtasks' findings
    overall_finding_input = f'### {var_bs_question} '
    for enum,_ in enumerate(l_subtask_artifact):
        subtask = _.get('subtask')
        finding = _.get('finding')
        overall_finding_input+=f'## Subtask{enum+1} : {subtask} \n\nFinding : {finding} \n\n\n'

    overall_finding_response = llm.invoke([SystemMessage(content=system_prompt__data_desc),
                                SystemMessage(content=system_prompt__finding_consolidation),
                                HumanMessage(content=overall_finding_input)])
    overall_finding_res = overall_finding_response.content
    return overall_finding_res

def save_module(overall_finding_res,task_enum,l_subtask_artifact,bs_no,var_bs_question):
    ##################################################################
    ### Phase6: Load info.json file, perform update, and then save
    save_json_name = save_path__json / '''info.json'''
    overall_output = {}
    try:
        with open(save_json_name, 'r') as f:
            overall_output = json.load(f)
        print("JSON loaded successfully")
        print(overall_output)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Invalid JSON format")
    except Exception as e:
        print(f"Error loading JSON: {e}")

    overall_output[f'bs{bs_no}'] = {'bs_qs': var_bs_question,
                                    'main_finding': overall_finding_res,
                                    'total_subtask': task_enum,
                                    'subtask_artifact': l_subtask_artifact}

    with open(save_json_name, 'w') as f:
        json.dump(overall_output, f, indent=4)


def main_workflow1(var_bs_question,bs_no):
    l_task = planner_module(var_bs_question)
    l_subtask_artifact=[]
    for task_enum,task in enumerate(l_task):
        task_enum=task_enum+1
        l_subtask_artifact=subtask_module(task, task_enum, bs_no, l_subtask_artifact)
    overall_finding_res = overall_finding_module(l_subtask_artifact,var_bs_question)
    save_module(overall_finding_res, task_enum, l_subtask_artifact,bs_no,var_bs_question)
    return f'All subtasks completed for business question {bs_no}'


########################################################################################################################
########################################################################################################################
########################################################################################################################
### Phase7: Report Generation

def generate_markdown_and_plot_module(overall_output):
    ### Phase7a: markdown format + plot selection
    findings_markdown=''
    _counter=1
    for k,v in overall_output.items():
        bs_qs = v.get('bs_qs','')
        main_finding = v.get('main_finding', '')
        subtask_artifact  = v.get('subtask_artifact', '')
        subtask_artifact = [{i:j for i,j in _dict.items() if i in ['subtask_no','subtask','plot']} for _dict in subtask_artifact]

        plot_selection_input = f'''Business Question : {bs_qs}\n\nMain Finding : {main_finding}\n\nSubtask and Plots : {subtask_artifact}'''
        plot_selection_response = llm.invoke([SystemMessage(content=system_prompt__plot_selection),
                                              HumanMessage(content=plot_selection_input)])
        plot_selection_res = plot_selection_response.content

        findings_markdown +=(f'## **Business Question {_counter}**\n'
                        f'{bs_qs}\n\n'
                        f'### **Main Finding**\n'
                        f'{main_finding}\n\n')
        findings_markdown +=plot_selection_res
        findings_markdown +='\n\n\n'
    return findings_markdown

def conclusion_and_report_output_module(findings_markdown):
    ### Phase7b: final report that contains generated conclusion and actionable insight
    conclusion_input = f'''Please find the business questions and findings of markdown file as follows:/n/n{findings_markdown}'''
    conclusion_response = llm.invoke([SystemMessage(content=system_prompt__report_generation),
                                          HumanMessage(content=conclusion_input)])
    conclusion_res = conclusion_response.content
    final_report = conclusion_res


    save_report_name = REPORT_NAME.as_posix()
    with open(save_report_name, "w", encoding="utf-8") as f:
        f.write(final_report)


def main_workflow2():
    save_json_name = save_path__json / '''info.json'''
    overall_output = {}
    try:
        with open(save_json_name, 'r') as f:
            overall_output = json.load(f)
        print("JSON loaded successfully")
        print(overall_output)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Invalid JSON format")
    except Exception as e:
        print(f"Error loading JSON: {e}")

    findings_markdown = generate_markdown_and_plot_module(overall_output)
    conclusion_and_report_output_module(findings_markdown)
    return f'{REPORT_NAME} completed'
