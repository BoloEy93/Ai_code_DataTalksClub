# Ai Dev Tools Bootcamp — DataTalksClub

This repository contains notes, exercises, and homework solutions for the Ai Dev Tools Bootcamp by DataTalksClub. It is organized to make it easy to follow the course, run examples, and track progress on assignments.

## Table of contents
- About
- Repository layout
- Getting started
- Environment & dependencies
- How to run notebooks and scripts
- Assignments & homeworks
- Coding conventions
- Contributing / submitting
- Resources & references
- License

## About
This folder stores coursework, lab notebooks, and homework submissions created while following the Ai Dev Tools Bootcamp from DataTalksClub. Use this README as the starting point to browse and run materials.

## Repository layout
Suggested structure:
- README.md — this file
- notebooks/ — course notebooks grouped by week/topic
- assignments/ — homework prompts and starter code
- solutions/ — reference solutions (if provided)
- data/ — small sample datasets (not large files)
- scripts/ — utility scripts (env setup, data prep)
- docs/ — notes, diagrams, and supplementary material

Example:
- notebooks/week-01-intro.ipynb
- assignments/week-01/
- solutions/week-01/

## Getting started
1. Clone the repository:
    git clone <repo-url>
2. Change to project directory:
    cd <repo-root>

## Environment & dependencies
Recommended:
- Python 3.9+ (use pyenv or conda)
- Virtual environment: venv or conda
- JupyterLab or Jupyter Notebook
- Common packages: pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter

Example using venv:
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
pip install -r requirements.txt

Include a requirements.txt in the repo with pinned versions used in the course.

## How to run notebooks and scripts
- Launch JupyterLab:
jupyter lab
- To run a notebook headless:
jupyter nbconvert --to notebook --execute notebooks/week-01-intro.ipynb --inplace

Run scripts:
python scripts/prep_data.py

## Assignments & homeworks
Each assignment folder should contain:
- README.md — assignment prompt & objectives
- starter_code/ — files to modify
- tests/ — optional unit tests (pytest)
- submission.md — instructions for submitting

Example assignments:
- week-01 — environment, basic Python, data handling
- week-02 — data ingestion & preprocessing
- week-03 — model training & evaluation
- week-04 — deployment basics & tooling
- week-05 — reproducibility, CI, and packaging

## Coding conventions
- Use clear, descriptive names.
- Keep notebooks linear and well-documented (explain intent and results).
- Add a brief summary cell at the top of each notebook.
- Prefer scripts/modules for reusable code; keep notebooks for exploration.

## Contributing / submitting
- Create a branch: git checkout -b feat/week-01-yourname
- Commit changes with clear messages.
- Open pull requests to merge into main.
- For homework submission, follow the assignment's submission.md (e.g., push to a branch or upload a zip).

## Resources & references
- DataTalksClub Bootcamp materials (official course pages)
- Jupyter documentation
- Python packaging & virtual environments
- Git & GitHub guides

## License
Add a LICENSE file if required (e.g., MIT). If this repo contains course materials that should not be distributed, add a note describing permitted use.

If you want, I can generate:
- a requirements.txt
- skeleton folders and example notebook templates
- a template assignment README

Which one would you like next?