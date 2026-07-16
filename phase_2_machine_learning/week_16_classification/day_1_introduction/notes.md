# Introduction to Classification

## 1. What is Classification

Classification is a Supervised Machine Learning technique that predicts categories or labels instead of numerical values.

### Simple Definition

Classification is the process of assigning an input to one of several predefined classes.

### Examples

### Input                       Output
Email                           Spam / Not Spam
Patient Report                  Healthy / Sick
Bank Transaction                Fraud / Genuine
Image                           Cat / Dog

Notice that every output is a category, not a number.


## 2. Regression vs Classification

### Regression                              Classification
Predicts continuous values                  Predicts categories
Output is numeric                           Output is a class label
Example: House Price                        Example: Spam Detection
Metrics: MAE, MSE, RMSE                     Metrics: Accuracy, Precision, Recall

### Example

### Regression

House Size -> $45,00,000

Output = Number

### Classification

Email -> Spam

Output = Category


## 3. Types of Classification

### A. Binary Classification

There are only two possible classes.

Examples:

- Spam / Not Spam
- Yes / No
- True / False
- Fraud / Genuine
- Healthy / Sick

### B. Multi-class Classification

More than two classes.

Examples

- Animal:
    Cat
    Dog
    Horse

- Handwritten Digits:
    0
    1
    2
    ...
    9

- Traffic Sign Recognition


## 4. Real-World Applications

### Email Filtering

Input

Congratulations!
You won $10,000.

Output

Spam


### Fraud Detection

Transaction -> Fraud   or  Normal


### Disease Prediction

Patient Data -> Healthy or Disease


### Face Recognition

Image -> Person Name


### Product Recommendation

Customer -> Interested or Not Interested

## 5. Why Classification is Important

Classification is one of most widely used Machine Learning techniques bacause many real-world problems require making decisions.

Examples:
- Gmail Spam Filter
- Medical Diagnosis
- Credit Approval
- Loan Prediction
- Face Unlock
- Fake News Detection
- Sentiment Analysis
- Malware Detection


## 6. Workflow of a Classification Model

Input Data -> Data Cleaning -> Feature Selection -> Train Classification Model -> Predict Class -> Evaluate Accuracy


