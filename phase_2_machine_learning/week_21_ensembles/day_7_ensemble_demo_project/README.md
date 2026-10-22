# Ensemble Model Comparison

## Overview

This project compares four machine learning
classification algorithms:

1. Decision Tree
2. Random Forest
3. AdaBoost
4. Gradient Boosting

## Objective

Evaluate the models using a consistent experimental
setup and compare accuracy, precision, recall,
and F1-score.

## Dataset

Breast Cancer Wisconsin Diagnostic Dataset,
loaded using scikit-learn.

## Methodology

- Stratified train/test split
- Test size: 20%
- Random state: 42
- Identical training and test sets for all models
- Consistent evaluation metrics

## Project Structure

- `code.py`: Executable experiment
- `notebook.ipynb`: Interactive analysis
- `data/README.md`: Dataset documentation
- `notes/ensemble_model_comparison.md`: Project notes
- `outputs/`: Generated results and visualizations

## Results

Insert the actual model comparison table here.

## Key Findings

Summarize the measured results and trade-offs.

## Limitations

The experiment uses a single train/test split
and does not include systematic hyperparameter tuning.

The project is educational and is not intended
for medical diagnosis.

## How to Run

Install dependencies:

`pip install numpy pandas matplotlib scikit-learn jupyter`

Run:

`python code.py`

## Conclusion

Summarize which model best meets the selected
evaluation objective and explain why.