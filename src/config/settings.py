"""Configuration settings for the two-agent system"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """Application settings"""

    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    # Model Configuration
    MODEL_NAME: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    MODEL_PROVIDER: str = os.getenv("MODEL_PROVIDER", "openai")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.1"))
    TOP_P: float = float(os.getenv("TOP_P", "0.1"))

    # Paths
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    PLOT_DIR: Path = BASE_DIR / "artifact/plot"
    DF_DIR: Path = BASE_DIR / "artifact/df"
    JSON_DIR: Path = BASE_DIR / "artifact/json"
    REPORT_DIR: Path = BASE_DIR / "artifact/report"
    RAW_DATA_DIR: Path = BASE_DIR / "input/raw_data"
    BS_DIR: Path = BASE_DIR / "input/business_question"
    EVAL_DIR: Path = BASE_DIR / "eval/eval_result"
    LOG_DIR: Path = BASE_DIR / "logs"

    # Input
    INPUT_FILENAME: str = os.getenv("INPUT_FILENAME", "BMW_processed_data_v1.0.xlsx")
    INPUT_NAME: Path = RAW_DATA_DIR / INPUT_FILENAME

    # Output
    OUTPUT_REPORT_NAME: str = os.getenv("OUTPUT_REPORT_NAME", "final_report.md")
    REPORT_NAME: Path = REPORT_DIR / OUTPUT_REPORT_NAME

    # Agent Configuration
    RESEARCH_AGENT_VERBOSE: bool = True
    ANALYST_AGENT_VERBOSE: bool = True

    def __init__(self):
        """Initialize settings and create necessary directories"""
        self.PLOT_DIR.mkdir(exist_ok=True)
        self.DF_DIR.mkdir(exist_ok=True)
        self.JSON_DIR.mkdir(exist_ok=True)
        self.REPORT_DIR.mkdir(exist_ok=True)

        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

settings = Settings()

