# ReportGeneration

- Generate findings, figures and conclusion based on raw data (excel) and business questions.
- A final report in markdown format will be generated.

## Features

- **Data Aggregation**: LLM performs data aggregation according to subtask of business question
- **Plot generation**: LLM generates plot using matplotlib or seaborn based on aggregated data
- **Finding Generation**: LLM generates findings and conclusion based on aggregated data or input findings.
- **Finding Refinement**: LLM will consolidate and refine findings for one round, in order to ensure cohesiveness and conciseness.

## Prerequisites

- Python 3.12+
- Docker and Docker Compose (for containerized deployment)


## Setup

### Local Setup

1. Clone the repository:
```bash
git clone 
cd ReportGenerationAsgn
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. Run the application:
```bash
python main.py
```

### Docker Setup

1. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
`````

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## Main Application Usage

1. Place raw_data in **input** directory. Add or remove business question in the **bs_question.txt**, where each line represents a business question.
2. Amend env file accordingly, especially the INPUT_FILENAME which refers to the filename of raw_data.
3. After executing main.py, the generated final report will be in **artifact/report** directory.


## Evaluation Usage

1. Bash run "python eval_exec.py". The result will be available in **eval/eval_result** directory.
2. The available metrics are ['coherence','conciseness','coverage','faithfulness'].
3. Report and subtask level evaluation are available. 
By default, faithfulness is evaluated at the subtask level, while coherence, conciseness, and coverage are evaluated at the report level. Have to modify eval_exec.py for other variation. 
4. The eval result for report level will be a list, where the first element being the score (1-5), and the second element being the justification. Whereas for The eval result for subtask level will be a list, where the fourth element being the score (1-5), the fifth element being the justification, and the first 3 elements being the metadata of subtask.

## Module Workflow

```
**Workflow1**
┌─────────────┐
│   Input     │──► raw data and business questions
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Planning   │──► Decompose business question into subtask
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Subtask Exec│──► Execute subtask, which involves data aggregation, plot generation, and insight generation
└──────┬──────┘
       │
       ▼
┌─────────────┐
│Finding Conso│──► Consolidate and re-organize all subtask findings into one coherent storyline that can address the business question
└──────┬──────┘
       │
       │
       ▼
 **Workflow2**
┌─────────────┐
│ Formatting  │──► Organize all previous findings in markdown format, and select relevant figures.
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Conclude   │──► Generate conclusion, (subjective) actionable insights and refine the storyline to be more cohesive
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Result    │──► Output report in markdown format
└──────┬──────┘
       │
       ▼  
   **Eval**
┌─────────────┐
│  Evaluation │──► Evaluate the report or subtask
└─────────────┘
```


# File System Structure
```
project/
├── artifact/       # Generated outputs and intermediate artifacts (dataframes, plots, reports)
│   ├── df/         # Saved aggregated data in pickle format
│   ├── plot/       # Saved figures and plots
│   ├── json/       # Intermediate and overall findings, and metadata
│   ├── report/     # **Final Report in markdown format**
├── eval/           # Evaluation test scripts
│   ├── eval_result/# Evaluation result files
├── input/          # Input data files
│   ├── business_question/  # **Business question to be addressed. Each line represents a business question**
│   ├── raw_data/   # **Raw Data**
├── logs/           # Logs
├── src/            # Source code
│   ├── agents/     # Primary Agents Source Code
│   ├── assets/     # Static resources (prompts, templates)
│   ├── configs/    # Configuration files and environmental variables
│   └── tools/      # Utility functions
└── tests/          # Test suites ongoing (boilerplate code)
```
