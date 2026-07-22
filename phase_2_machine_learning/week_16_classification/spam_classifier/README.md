# Spam Classifier using Logistic Regression

## Project Overview

This project is a simple Machine Learning application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using **Logistic Regression**. The text data is converted into numerical features using **CountVectorizer**, and the model is evaluated using standard classification metrics.

---

## Features

- Load SMS Spam Collection dataset
- Preprocess text labels
- Convert text into numerical features
- Train a Logistic Regression model
- Predict Spam or Ham messages
- Evaluate model performance
- Test custom messages

---

## Project Structure

```
spam-classifier/
│
├── notebooks/
│   └── spam_classifier.ipynb
│
├── datasets/
│   └── spam.csv
│
├── notes/
│   └── spam_classifier_notes.md
│
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

---

## Machine Learning Workflow

1. Import libraries
2. Load dataset
3. Convert labels
4. Split data
5. Convert text into numbers
6. Train Logistic Regression
7. Prediction
8. Evaluate model
9. Test your own message

---

## Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## Example Prediction

**Input:**

```
Congratulations! You have won a free prize.
```

**Output:**

```
Spam
```

**Input:**

```
Hi, are we meeting tomorrow?
```

**Output:**

```
Ham
```

---

## Future Improvements

- Use TF-IDF Vectorizer
- Try Naive Bayes and Support Vector Machine (SVM)
- Improve text preprocessing
- Deploy the model as a web application using Streamlit or Flask

---

## Conclusion

This project demonstrates how Logistic Regression can be used for binary text classification. It provides a complete workflow, from data preprocessing to model evaluation, and serves as a foundation for more advanced Natural Language Processing (NLP) projects.