# DAY 6 --- AdaBoost + Gradient Boosting

## AdaBoost

Learn the basic idea:

> Later weak learners place more emphasis on examples that previous
> learners handled poorly.

Conceptually:

``` text
Weak Learner 1
      ↓
Errors identified
      ↓
Weak Learner 2 focuses more on difficult examples
      ↓
Weak Learner 3
      ↓
Combine learners
```

You do not need to derive every mathematical detail yet.

Understand the mechanism.

## Gradient Boosting

This is another major concept.

Instead of simply focusing on incorrectly classified examples, gradient
boosting builds models sequentially to reduce the current model's loss.

Conceptually:

``` text
Initial Prediction
      ↓
Calculate Error
      ↓
New Tree learns to reduce error
      ↓
Updated Prediction
      ↓
Calculate Remaining Error
      ↓
Another Tree
      ↓
...
```

This concept becomes very important later when you encounter modern
gradient-boosted implementations.

# Phase 2 --- Week 21 --- Day 6

## AdaBoost + Gradient Boosting

**Language:** Fully English \| **Level:** Beginner to Intermediate \|
**Phase:** Machine Learning

Your Day 5 is completed. Today, we will continue Week 21: **Ensemble
Learning**, focusing on two important boosting algorithms:

1.  AdaBoost
2.  Gradient Boosting

Today's objective is to understand how boosting works, implement both
algorithms using Scikit-learn, compare their performance, and prepare
code that you can use in your Week 21 ensemble learning project.

------------------------------------------------------------------------

# 1. Today's Learning Objectives

By the end of Day 6, you should be able to:

-   Explain the fundamental concept of boosting.
-   Understand how AdaBoost learns from previous mistakes.
-   Understand how Gradient Boosting reduces prediction errors.
-   Differentiate between Random Forest, AdaBoost, and Gradient
    Boosting.
-   Implement both boosting algorithms using Scikit-learn.
-   Evaluate models using accuracy, precision, recall, and F1-score.
-   Compare multiple ensemble algorithms experimentally.
-   Save your work in your Week 21 project repository.

**Estimated study time:** 3--4 hours.

------------------------------------------------------------------------

# 2. Part A --- Understanding Boosting

## 2.1 What Is Boosting?

Boosting is an ensemble learning technique that combines multiple weak
learners to create a stronger predictive model.

A weak learner is a model that performs only slightly better than a
simple baseline on a particular task.

Decision trees with limited depth are commonly used as weak learners in
boosting algorithms.

### Example

Suppose you are building a model to predict whether an email is spam.

Your first model makes several incorrect predictions.

Instead of building many independent models, a boosting algorithm builds
models sequentially, allowing later models to improve upon the current
ensemble.

The general process is:

``` text
Training Dataset
      |
      v
Initial Weak Learner
      |
      v
Identify Errors or Calculate Loss
      |
      v
Train Another Weak Learner
      |
      v
Update the Ensemble
      |
      v
Repeat the Process
      |
      v
Final Stronger Model
```

The exact mechanism depends on the boosting algorithm.

**Important:** Boosting models are trained sequentially, unlike the
independently trained trees in a conventional Random Forest.

------------------------------------------------------------------------

# 3. Part B --- AdaBoost

## 3.1 What Is AdaBoost?

AdaBoost stands for **Adaptive Boosting**.

It combines multiple weak learners while adapting the training process
to emphasize examples that previous learners handled poorly.

A common implementation uses shallow decision trees called decision
stumps.

A decision stump is a decision tree with a maximum depth of one.

## 3.2 How AdaBoost Works

Consider a dataset containing 100 training examples.

Initially, the examples receive weights that determine their relative
importance during training.

The algorithm then follows this general process:

``` text
Step 1: Initialize Example Weights
      |
      v
Step 2: Train the First Weak Learner
      |
      v
Step 3: Measure Its Classification Error
      |
      v
Step 4: Calculate the Learner's Importance
      |
      v
Step 5: Update Example Weights
      |
      v
Step 6: Train the Next Weak Learner
      |
      v
Step 7: Combine the Weak Learners
      |
      v
Step 8: Produce the Final Prediction
```

Misclassified examples generally receive more emphasis in subsequent
training rounds.

The final prediction combines the weak learners according to their
assigned importance.

### Important concepts

  -----------------------------------------------------------------------
  Concept                             Meaning
  ----------------------------------- -----------------------------------
  Weak learner                        A relatively simple predictive
                                      model

  Sample weight                       A weight representing an example's
                                      importance during training

  Classification error                The proportion or weighted
                                      proportion of incorrect predictions

  Learner weight                      The influence of a weak learner on
                                      the final prediction

  Sequential learning                 Training learners one after another

  Final ensemble                      The combined prediction from
                                      multiple learners
  -----------------------------------------------------------------------

**Key takeaway:** AdaBoost adapts the importance of training examples
based on the performance of previous learners.

------------------------------------------------------------------------

# 4. Part C — Gradient Boosting

## 4.1 What Is Gradient Boosting?

Gradient Boosting is an ensemble learning method that builds models sequentially to optimize a specified loss function.

Each new learner helps improve the current ensemble by moving its predictions in a direction that reduces the loss.

Decision trees are commonly used as the individual learners.

Unlike AdaBoost, Gradient Boosting is formulated around optimization of a loss function and can support different prediction tasks.

For example:

- Regression: Predicting house prices.
- Binary classification: Predicting whether a customer will leave a service.
- Multiclass classification: Classifying images into multiple categories.

## 4.2 How Gradient Boosting Works

Consider a model that predicts house prices.

The initial model might predict the average house price for every house.

Its predictions will be inaccurate for many individual properties.

Gradient Boosting then adds trees that help improve the predictions.

```text
Step 1: Initialize the Model
        |
        v
Step 2: Make Initial Predictions
        |
        v
Step 3: Calculate the Negative Loss Gradient
        |
        v
Step 4: Train a New Decision Tree
        |
        v
Step 5: Update the Current Predictions
        |
        v
Step 6: Recalculate the Loss
        |
        v
Step 7: Train Another Decision Tree
        |
        v
Step 8: Combine the Trees
        |
        v
Final Prediction
```

For squared-error regression, the residuals are closely related to the negative gradients of the loss.

For other loss functions, the relationship depends on the selected objective.

### Important concepts

| Concept | Meaning |
|---|---|
| Loss function | Measures how poorly predictions match the target values |
| Gradient | Indicates how the loss changes with respect to model predictions or parameters |
| Negative gradient | Indicates a direction for reducing the loss |
| Residual | The difference between an observed value and a prediction |
| Learning rate | Controls the contribution of each new learner |
| Number of estimators | Determines how many boosting stages are used |
| Tree depth | Controls the complexity of individual trees |

**Key takeaway:** Gradient Boosting adds learners that improve the ensemble by optimizing its loss function.

# 5. Part D — AdaBoost vs. Gradient Boosting

Understanding the differences between these algorithms is essential.

| Feature | AdaBoost | Gradient Boosting |
|---|---|---|
| Main idea | Adapt the importance of training examples | Optimize a loss function sequentially |
| Training process | Sequential | Sequential |
| Common weak learner | Decision stump | Decision tree |
| Learning mechanism | Reweights examples and combines learners | Fits learners to negative loss gradients |
| Classification | Supported | Supported |
| Regression | Supported | Supported |
| Loss optimization | Uses an adaptive boosting procedure | Explicitly optimizes a chosen loss function |
| Overfitting risk | Possible | Possible |
| Important parameters | Estimators, learning rate | Estimators, learning rate, tree depth |
| Typical applications | Classification and regression | Classification and regression |

## Remember this distinction

**AdaBoost:** Adapt the emphasis placed on training examples.

**Gradient Boosting:** Improve the ensemble by optimizing its loss function.

Both methods can be effective, but neither is guaranteed to outperform the other on every dataset.
# 6. Part E — Hands-On Implementation

Now you will implement both algorithms using Python and Scikit-learn.

We will use a built-in classification dataset so that you can focus on the algorithms without spending time collecting or cleaning external data.

## Step 1: Import the Required Libraries

Create a Python file named:

```text
adaboost_gradient_boosting.py
```

Add the required imports and implementation code to this file.

## What are these libraries for?

- `load_breast_cancer`: Loads a built-in binary classification dataset.
- `train_test_split`: Splits the dataset into training and testing sets.
- `AdaBoostClassifier`: Implements AdaBoost for classification.
- `GradientBoostingClassifier`: Implements Gradient Boosting for classification.
- `RandomForestClassifier`: Provides a baseline for comparison.
- `accuracy_score`: Calculates the proportion of correct predictions.
- `precision_score`: Measures the proportion of positive predictions that are correct.
- `recall_score`: Measures how many actual positive examples are identified.
- `f1_score`: Calculates the harmonic mean of precision and recall.
- `classification_report`: Produces a detailed classification report.
- `pandas`: Organizes the results into a table.

The dataset contains diagnostic measurements used to classify tumors as malignant or benign. We will use it strictly as a machine-learning learning exercise.

## Understand the code

`X` contains the input features.

`y` contains the target labels.

The model learns patterns from `X` to predict `y`.

The dataset includes multiple numerical features, so scaling is not required for these particular tree-based models.

## Why split the dataset?

We need separate data for training and evaluation.

- Training data teaches the model.
- Testing data evaluates its performance on examples it did not use during training.

The `stratify=y` parameter helps preserve the class proportions in both sets.

The `random_state=42` parameter makes the split reproducible.

## Understand the parameters

### `n_estimators=100`

Uses 100 boosting stages for the boosting models or 100 trees for Random Forest.

### `learning_rate=0.5`

Controls the contribution of each boosting stage in AdaBoost.

### `learning_rate=0.1`

Controls the contribution of each boosting stage in Gradient Boosting.

### `max_depth=2`

Limits the depth of each individual tree in Gradient Boosting.

### `random_state=42`

Helps make the results reproducible.

The parameter choices are starting points for experimentation, not guaranteed optimal settings.

## What does this experiment accomplish?

It trains three different ensemble models using the same training and testing split.

It then compares their:

- Accuracy
- Precision
- Recall
- F1-score

The resulting table allows you to compare their performance on the same dataset.

**Do not assume that one algorithm will always win.** Your actual results will depend on the dataset, parameter settings, and evaluation procedure.
# 7. Part F — Understanding Evaluation Metrics

Suppose a model predicts whether an example belongs to the positive class.

Its predictions can be divided into four categories:

| Term | Meaning |
|---|---|
| True Positive | Correctly predicts a positive example |
| True Negative | Correctly predicts a negative example |
| False Positive | Incorrectly predicts a positive example |
| False Negative | Incorrectly predicts a negative example |

The metrics measure different aspects of performance.

## Accuracy

The proportion of all predictions that are correct.

\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]

## Precision

The proportion of predicted positive examples that are actually positive.

\[
\text{Precision} = \frac{TP}{TP + FP}
\]

## Recall

The proportion of actual positive examples correctly identified.

\[
\text{Recall} = \frac{TP}{TP + FN}
\]

## F1-score

The harmonic mean of precision and recall.

\[
F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
\]

## Which metric should you prioritize?

It depends on the problem.

For example, in a medical classification task, false negatives may have serious consequences. Recall may therefore deserve particular attention.

In a spam-filtering task, false positives may cause legitimate emails to be incorrectly marked as spam. Precision may be especially important.

**Professional lesson:** Never choose a model using accuracy alone without considering the problem's requirements.

## Experiment output

This creates a CSV file containing the evaluation results.

Your project now produces two useful outputs:

1. A Python implementation of the algorithms.
2. A model comparison report.

These outputs provide evidence of your understanding and implementation skills.

# 9. Part H — Create a Jupyter Notebook

Create a second file:

```text
adaboost_gradient_boosting.ipynb
```

Organize the notebook into these sections:

1. Project Title and Objective
2. Introduction to Boosting
3. AdaBoost Theory
4. Gradient Boosting Theory
5. Dataset Description
6. Data Preparation
7. AdaBoost Implementation
8. Gradient Boosting Implementation
9. Random Forest Baseline
10. Model Evaluation
11. Performance Comparison
12. Observations and Conclusion

Use Markdown cells for explanations and code cells for implementation.

Include the comparison table generated by your experiment.

Write your conclusions based on the results you actually obtain.

Do not invent performance numbers.

# 10. Part I — Practical Exercises

Complete these exercises after the initial implementation.

## Exercise 1: Change the Number of Estimators

Train AdaBoost with:

```python
n_estimators=25
n_estimators=50
n_estimators=100
n_estimators=200
```

Record the accuracy and F1-score for each configuration.

**Question:** Does increasing the number of estimators always improve performance?

## Experiment 1: Change the Number of Estimators

### 1. Objective

Understand how the number of estimators affects AdaBoost's performance.

In AdaBoost, `n_estimators` specifies the maximum number of boosting stages. Each stage adds a weak learner to the ensemble.

We will experiment with four configurations:

| Experiment | Number of Estimators |
|---|---:|
| Experiment 1 | 25 |
| Experiment 2 | 50 |
| Experiment 3 | 100 |
| Experiment 4 | 200 |

We will compare their accuracy and F1-score.

### Important implementation detail

We keep the following parameters constant:

- `learning_rate=0.5`
- `random_state=42`
- The training dataset
- The testing dataset

Only `n_estimators` changes.

This allows us to investigate the effect of the number of estimators without simultaneously changing other experimental settings.

### 3. Understand the Results

After running the code, you should see a table similar in structure to this:

| n_estimators | Accuracy | F1 Score |
|---:|---|---|
| 25 | Actual result | Actual result |
| 50 | Actual result | Actual result |
| 100 | Actual result | Actual result |
| 200 | Actual result | Actual result |

These are placeholders, not experimental results. Your Python program will calculate the actual values.

### What should you observe?

Compare the accuracy and F1-score across the four configurations.

Consider these possibilities:

- Performance improves as more estimators are added.
- Performance improves initially and then stops improving.
- Performance fluctuates as the number of estimators increases.
- A configuration with fewer estimators performs better on the test set.

Any of these outcomes can provide useful information about the model.

### 4. Answer the Main Question

**Question:** Does increasing the number of estimators always improve performance?

#### Expected conceptual answer

No. Increasing the number of estimators does not guarantee improved performance.

Adding more estimators can improve the ensemble by allowing it to learn additional patterns. However, the benefit depends on the dataset, learning rate, and other model characteristics.

Performance may eventually plateau or decline on unseen data. Additional estimators also increase training time and model complexity.

The correct approach is to evaluate different configurations using an appropriate validation procedure rather than assuming that more estimators always produce a better model.

**Your task:** Run the experiment and compare your actual results with this explanation.


# Experiment 2: Change the Learning Rate

Experiment with:

```python
learning_rate=0.01
learning_rate=0.1
learning_rate=0.5
learning_rate=1.0
```

Keep the other parameters fixed.

**Question:** How does the learning rate affect the results?

## 1. Objective

The learning rate controls the contribution of each weak learner to the AdaBoost ensemble.

We will experiment with four learning rates:

| Experiment | Learning Rate | Number of Estimators |
|---:|---:|---:|
| 1 | 0.01 | 100 |
| 2 | 0.1 | 100 |
| 3 | 0.5 | 100 |
| 4 | 1.0 | 100 |

**Important:** We will keep `n_estimators=100` and all other experimental settings fixed. Only the learning rate will change.

## 2. Understand the Learning Rate

Consider these three configurations:

- **Low learning rate:** Each weak learner contributes less to the ensemble.
- **Moderate learning rate:** Each learner makes a more substantial contribution.
- **High learning rate:** Each learner can have a greater influence on the ensemble.

A lower learning rate may require more estimators to achieve good performance. A higher learning rate may learn useful patterns faster, but it does not guarantee better generalization.

The best value depends on the dataset and the other hyperparameters.

## 4. Understand the Experimental Design

Notice that we keep these settings unchanged:

```python
n_estimators=100
random_state=42
test_size=0.20
```

Only this parameter changes:

```python
learning_rate=rate
```

This is important because changing multiple parameters simultaneously would make it harder to understand which change influenced the results.

## 5. Record Your Results

After running the code, you should obtain a table like this:

| Learning Rate | Accuracy | F1 Score |
|---:|---|---|
| 0.01 | Your result | Your result |
| 0.1 | Your result | Your result |
| 0.5 | Your result | Your result |
| 1.0 | Your result | Your result |

Do not fill in estimated numbers. Record the actual values produced by your program.

Your results will also be saved automatically to:

`adaboost_learning_rate_experiment.csv`

## 6. Answer the Main Question

**Question:** How does the learning rate affect the results?

Before running the experiment, understand the expected principle:

The learning rate determines how strongly each weak learner contributes to the AdaBoost ensemble. A smaller value reduces each learner's contribution, while a larger value increases it. A smaller learning rate may require more estimators, and neither a smaller nor a larger value guarantees better performance.

Your experiment will help you determine how the learning rate affects accuracy and F1-score on this particular dataset.

**Remember:** Results on one test split are evidence about that experiment, not proof that a learning rate is universally best.

# Experiment 3: Change the Gradient Boosting Tree Depth

Try:

```python
max_depth=1
max_depth=2
max_depth=3
```

Compare the models.

**Question:** What happens when the individual trees become more complex?

## 1. Objective

Understand how tree complexity affects:

- Accuracy
- F1-score
- Model learning capacity
- Overfitting and generalization

We will experiment with three values of `max_depth`.

| Experiment | `max_depth` | Tree complexity |
|---:|---:|---|
| 1 | 1 | Shallow |
| 2 | 2 | Moderate |
| 3 | 3 | Deeper |

**Important:** We will keep all other parameters fixed so that we can isolate the effect of tree depth.

## 2. Understand `max_depth`

The `max_depth` parameter controls the maximum depth of each decision tree.

### Example

#### Depth 1

```text
       Root
       /  \
    Leaf  Leaf
```

This tree can learn only simple decision rules.

#### Depth 2

```text
          Root
         /    \
      Node    Node
      /  \    /  \
   Leaf Leaf Leaf Leaf
```

This tree can learn more complex patterns.

#### Depth 3

The tree can make additional splits, allowing it to represent more complicated relationships between features and target labels.

### Key concept

Increasing tree depth increases the complexity of the patterns an individual tree can learn.

However, a more complex tree does not automatically produce a better model.

## 4. Understand the Experimental Design

Notice that we keep these parameters fixed:

```python
n_estimators=100
learning_rate=0.1
random_state=42
```

Only `max_depth` changes:

```python
max_depth=depth
```

This is a controlled experiment because we change one parameter while keeping the others constant.

The same training and testing datasets are used for all three configurations.

## 5. Record Your Results

After running the code, your output will have this structure:

| Max Depth | Accuracy | F1-score |
|---:|---|---|
| 1 | Actual result | Actual result |
| 2 | Actual result | Actual result |
| 3 | Actual result | Actual result |

These are placeholders, not actual performance measurements. Your program will calculate the results.

The results will also be saved automatically to:

`gradient_boosting_depth_experiment.csv`

### Compare the models

Look for answers to these questions:

1. Which tree depth produces the highest accuracy?
2. Which tree depth produces the highest F1-score?
3. Does increasing the tree depth consistently improve performance?
4. Is there a configuration that performs worse despite having more complex trees?

Do not assume the deepest tree will win.

## 6. Answer the Main Question

**Question:** What happens when individual trees become more complex?

### Expected conceptual answer

As individual trees become deeper, they can learn more complex relationships and interactions between features.

This increased flexibility can improve predictive performance when the additional complexity captures useful patterns in the data.

However, deeper trees can also fit noise in the training data, increasing the risk of overfitting. Consequently, a deeper tree may perform better on training data but not necessarily on unseen data.

The appropriate tree depth depends on the dataset and the other model parameters.

**Important:** Your experiment uses a single train/test split. It can illustrate the effect of tree depth, but cross-validation would provide stronger evidence when selecting the best configuration.


# Experiment 4: Write Your Own Conclusion

Answer these questions in your notebook:

1. Which model achieved the highest accuracy?
2. Which model achieved the highest F1-score?
3. Did the model with the highest accuracy also have the highest recall?
4. Which configuration performed best in your experiments?
5. What did you learn about boosting?
6. What would you investigate next to improve the results?

# 11. Part J — Important Engineering Practices

Understanding an algorithm is only one part of building reliable machine-learning systems.

Follow these practices:

- Use a separate test set for final evaluation.
- Keep the test set out of hyperparameter tuning.
- Compare models on the same data split.
- Record the parameters used in each experiment.
- Use reproducible random seeds where appropriate.
- Avoid claiming that a model is superior based on one dataset.
- Use cross-validation when conducting systematic model selection.
- Investigate precision and recall when the consequences of classification errors differ.
- Save your experiments and explanations in your repository.

For today's experiment, a fixed test split is sufficient for learning the implementation. In a later week, you will study cross-validation and systematic hyperparameter tuning in greater depth.

# 13. Day 6 Completion Checklist

Before marking Day 6 as complete, verify the following:

| Task | Completion |
|---|---|
| Understand boosting | ☐ |
| Understand AdaBoost | ☐ |
| Understand Gradient Boosting | ☐ |
| Implement AdaBoost | ☐ |
| Implement Gradient Boosting | ☐ |
| Train the Random Forest baseline | ☐ |
| Evaluate all three models | ☐ |
| Save the comparison CSV | ☐ |
| Complete the Jupyter notebook | ☐ |
| Perform the parameter experiments | ☐ |
| Write your conclusions | ☐ |
| Update the Day 6 README | ☐ |
| Save the work in `repo-20` | ☐ |

# 14. Final Review — Test Your Understanding

Answer these questions without looking at the explanations above.

**Q1.** What is the main purpose of boosting?

**Q2.** How does AdaBoost adapt to examples that previous learners classified incorrectly?

**Q3.** What is the role of a loss function in Gradient Boosting?

**Q4.** Why are boosting algorithms trained sequentially?

**Q5.** What is the difference between AdaBoost and Gradient Boosting?

**Q6.** Why might a model with higher accuracy still be less suitable for a particular application?

**Q7.** What is the purpose of the learning rate?

**Q8.** Why should you evaluate models on data that was not used to train them?

**Q9.** Why is it useful to compare boosting algorithms with Random Forest?

**Q10.** Why should you avoid choosing a model based on a single metric?

Try to answer each question in two to four sentences.
