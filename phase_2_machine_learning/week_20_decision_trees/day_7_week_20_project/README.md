# Decision Tree Classification — Titanic Survival Prediction

## Project Overview

This project uses a Decision Tree classifier to predict whether a
Titanic passenger survived.

## Problem

Binary classification.

Target:
`Survived`

## Dataset

Titanic passenger dataset.

## Machine Learning Workflow

1. Data loading
2. Data understanding
3. Data cleaning
4. Train/test split
5. Preprocessing
6. Baseline Decision Tree
7. Model evaluation
8. Hyperparameter experiments
9. Feature importance
10. Final model

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Hyperparameter Experiment

Several `max_depth` values were compared to study model complexity,
underfitting, overfitting, and generalization.

## Feature Importance

The Decision Tree's feature importance values were analyzed to
understand which transformed features contributed most to the model's
splitting decisions.

Feature importance is not equivalent to causality.

## Key Learning

Decision Trees are powerful and interpretable models, but unrestricted
tree growth can lead to overfitting.

Model complexity should therefore be controlled and evaluated using
unseen data.