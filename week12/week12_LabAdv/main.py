# week12/week12_LabAdv/main.py
import os
import sys

project_dir = os.path.join(os.path.dirname(__file__), "Week_12_LabX_ADV_Agentic_Communication_Workflows_Advanced_Email_And_SMS-main")
sys.path.insert(0, project_dir)
sys.path.insert(0, os.path.join(project_dir, "src"))

os.chdir(project_dir)
from main import main

if __name__ == "__main__":
    main()
