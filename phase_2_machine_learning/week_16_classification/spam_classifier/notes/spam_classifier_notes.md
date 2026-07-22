# Spam Classifier Notes

## What is a Spam Classifier?

A Spam Classifier is a machine learning model that classifies a text message as either:

- Spam (Unwanted or promotional message)
- Ham (Normal or legitimate message)

It is a Binary Classification problem because there are only two possible classes.

---

# Dataset

Dataset: SMS Spam Collection

Columns:

- label
  - ham
  - spam

- message
  - Text content of the SMS

Example:

| Label | Message |
|-------|---------|
| Ham | Hi, how are you? |
| Spam | Congratulations! You won a free prize. |

---

# Workflow

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

# Text Vectorization

Machine learning models cannot understand text directly.

CountVectorizer converts text into numerical vectors by counting the occurrence of each word.

Example:

Messages:

- "Free prize"
- "Free money"

Vocabulary:

Free, Prize, Money

Vector Representation:

Free Prize Money

Message 1 → 1 1 0

Message 2 → 1 0 1

---

# Logistic Regression

Logistic Regression is a supervised learning algorithm used for binary classification.

It predicts the probability that a message belongs to the Spam class.

If probability ≥ 0.5 → Spam

If probability < 0.5 → Ham

---

# Model Evaluation

The following metrics were used:

- Accuracy Score
- Confusion Matrix
- Classification Report

These metrics help measure how well the model performs on unseen data.

---

# Advantages

- Easy to implement
- Fast training
- Good accuracy for text classification
- Works well for binary classification problems

---

# Limitations

- Performance depends on data quality
- Does not understand sentence meaning
- May misclassify unseen or ambiguous messages

---

# Applications

- Email spam detection
- SMS spam filtering
- Fraud message detection
- Customer support ticket classification
- Social media content filtering

---

# Libraries Used

- pandas
- numpy
- scikit-learn

Main modules:

- CountVectorizer
- LogisticRegression
- train_test_split
- accuracy_score
- confusion_matrix
- classification_report

---

# Conclusion

In this project, a Spam Classifier was built using Logistic Regression and CountVectorizer. The model successfully classified SMS messages as Spam or Ham and was evaluated using standard classification metrics.