# PHASE 2 --- MACHINE LEARNING

## WEEK 20 --- DECISION TREES 🌳

### DAY 1 --- DECISION TREE FUNDAMENTALS

**Week 20 Core Focus:** Decision Trees\
**Skill Output:** Decision Tree fundamentals\
**Project Output:** Tree model\
**Language:** English only GB

------------------------------------------------------------------------

# 🎯 DAY 1 OBJECTIVE

By the end of today, you should be able to:

1.  Explain what a Decision Tree is.
2.  Understand root, decision node, branch, leaf, split, depth, parent,
    and child.
3.  Trace a prediction through a tree manually.
4.  Understand why a tree repeatedly splits data.
5.  Draw simple Decision Trees without using code.
6.  Explain the difference between a classification tree and a
    regression tree.
7.  Understand why tree depth matters.

------------------------------------------------------------------------

# 1. What Is a Decision Tree?

A Decision Tree is a machine-learning model that makes predictions by
repeatedly asking questions about the input features.

Think of it as a sequence of decisions:

``` text
                    Income > ₹50k?
                    /           \
                  Yes            No
                  /               \
             Age > 30?            No
              /     \
            Yes      No
             /        \
           BUY       MAYBE
```

The model follows one path from the top to the bottom.

For example:

``` text
Income = ₹70k
Age = 35

Prediction:

Income > ₹50k? → Yes
Age > 30?      → Yes
Prediction     → BUY
```

So a Decision Tree is essentially learning a set of if-then rules from
data.

------------------------------------------------------------------------

# 2. The Seven Terms You Must Know

## ① Root Node

The root node is the first decision in the tree.

``` text
Income > ₹50k?
```

There is only one root node.

------------------------------------------------------------------------

## ② Decision Node

A decision node asks a question and splits the data.

``` text
Income > ₹50k?
      /     \
    Yes      No
```

The question:

> "Is Income greater than ₹50k?"

is the decision.

------------------------------------------------------------------------

## ③ Branch

A branch represents the result of a decision.

``` text
Income > ₹50k?
      /     \
    Yes      No
```

Yes and No are branches.

------------------------------------------------------------------------

## ④ Leaf Node

A leaf node is the final prediction.

``` text
Age > 30?
   /    \
 BUY   MAYBE
```

BUY and MAYBE are leaf predictions.

A leaf does not make another decision.

------------------------------------------------------------------------

## ⑤ Split

A split divides the dataset into smaller groups.

Example:

``` text
Age > 30
```

could produce:

``` text
Age ≤ 30
Age > 30
```

The goal is to create groups that are more homogeneous with respect to
the target.

------------------------------------------------------------------------

## ⑥ Depth

Depth tells us how many levels of decisions exist from the root.

Example:

``` text
        Income?
           |
         Age?
        /    \
      BUY     NO
```

The deeper the tree becomes, the more complex its decision rules can
become.

------------------------------------------------------------------------

## ⑦ Parent and Child

Consider:

``` text
        Income > ₹50k?
          /        \
        Yes         No
         |
      Age > 30?
```

Income \> ₹50k? is the parent.

Age \> 30? is a child.

Every node below another node is its child.

------------------------------------------------------------------------

# 3. The Most Important Intuition

A Decision Tree tries to transform this:

``` text
MESSY DATA
    ↓
  split
    ↓
smaller groups
    ↓
split again
    ↓
more homogeneous groups
    ↓
prediction
```

Imagine customer data:

  Income     Age Purchased
  
  -------- ----- -----------
  80k         35 Yes

  75k         40 Yes

  25k         22 No

  30k         25 No

  90k         42 Yes

  20k         21 No

A tree might discover:

``` text
             Income > 50k?
                /      \
              Yes       No
               |         |
              YES        NO
```

The split separates the examples into relatively pure groups. \# 4.
Classification vs Regression

Decision Trees can solve both major supervised-learning tasks.

## Classification

Predict a category:

``` text
Spam / Not Spam
Buy / Not Buy
Disease / No Disease
Cat / Dog
```

Example:

``` text
             Income > 50k?
                /       \
              Yes        No
               |          |
             BUY      DON'T BUY
```

## Regression

Predict a continuous numerical value:

``` text
House price
Salary
Temperature
Demand
```

Example:

``` text
             Area > 1500?
                /       \
              Yes        No
               |          |
             ₹80L       ₹45L
```

The underlying tree structure is similar, but the prediction at the leaf
is different.

------------------------------------------------------------------------

# 5. How Does a Tree Choose a Question?

This is one of the most important concepts for later in Week 20.

Suppose we have:

``` text
Age
Income
Credit Score
```

The algorithm has many possible questions:

``` text
Age > 25?
Age > 30?
Age > 40?

Income > 40k?
Income > 50k?
Income > 70k?

Credit Score > 600?
Credit Score > 700?
```

The algorithm searches for splits that produce better-separated groups.

For classification, common measures include:

-   Gini Impurity
-   Entropy
-   Information Gain

Do not try to memorize the formulas today.

Your Day 1 goal is to understand:

> A Decision Tree searches for useful questions that make the resulting
> groups more homogeneous.

------------------------------------------------------------------------

# 6. Why Not Just Make an Extremely Deep Tree?

Consider:

``` text
Feature A?
    |
Feature B?
    |
Feature C?
    |
Feature D?
    |
Feature E?
    |
...
```

A very deep tree can memorize the training data.

This is called:

## Overfitting

The model performs extremely well on training examples but may perform
poorly on unseen data.

Conceptually:

``` text
Too shallow
    ↓
Underfitting

Good depth
    ↓
Useful generalization

Too deep
    ↓
Overfitting
```

You will study this more deeply later.

------------------------------------------------------------------------

# 🔴 DAY 1 CORE CONCEPT

Memorize this idea:

> A Decision Tree recursively splits data using feature-based questions
> until it reaches useful prediction nodes.

And remember the flow:

``` text
ROOT
  ↓
QUESTION
  ↓
SPLIT
  ↓
BRANCHES
  ↓
CHILD NODES
  ↓
MORE SPLITS
  ↓
LEAF
  ↓
PREDICTION
```

------------------------------------------------------------------------

# 🏃 DAY 1 HANDS-ON TASK

Task: Draw 3 Decision Trees manually

Use paper and draw the following.

## Tree 1 --- Student Result

Create a tree predicting:

``` text
PASS / FAIL
```

Use:

``` text
Study Hours
Attendance
```

Example structure:

``` text
              Study Hours > 4?
                /          \
              Yes           No
               |             |
        Attendance > 75?     FAIL
            /      \
          Yes       No
           |         |
         PASS       FAIL
```

You may design your own thresholds.

------------------------------------------------------------------------

## Tree 2 --- Loan Approval

Predict:

``` text
APPROVE / REJECT
```

Use:

``` text
Income
Credit Score
Existing Debt
```

Draw at least 2 levels.

------------------------------------------------------------------------

## Tree 3 --- Product Purchase

Predict:

``` text
BUY / DON'T BUY
```

Use:

``` text
Age
Income
Previous Purchases
```

Draw at least 2--3 levels. \# 🧠 THINKING EXERCISE

For your third tree, take this customer:

``` text
Age = 32
Income = ₹70,000
Previous Purchases = 5
```

Then manually trace:

``` text
ROOT
  ↓
Branch
  ↓
Decision
  ↓
Branch
  ↓
Leaf
```

Write the complete path.

Example:

``` text
Income > ₹50,000
        ↓
       YES
        ↓
Age > 30
        ↓
       YES
        ↓
Previous Purchases > 3
        ↓
       YES
        ↓
       BUY
```

------------------------------------------------------------------------

# ✅ DAY 1 COMPLETION CHECKLIST

Before marking Day 1 complete, you should be able to answer YES to all
of these:

-   [ ] I can define a Decision Tree.
-   [ ] I know what a root node is.
-   [ ] I know what a decision node is.
-   [ ] I know what a branch is.
-   [ ] I know what a leaf node is.
-   [ ] I understand a split.
-   [ ] I understand tree depth.
-   [ ] I understand parent vs child.
-   [ ] I understand classification trees.
-   [ ] I understand regression trees.
-   [ ] I can manually trace a prediction through a tree.
-   [ ] I drew 3 Decision Trees on paper.
-   [ ] I created `decision_trees_fundamentals.md`.
-   [ ] I understand that excessively deep trees can overfit.

------------------------------------------------------------------------

# 🧠 DAY 1 MINDSET

Do not learn Decision Trees as:

> "another sklearn algorithm."

Learn them as:

> A model that converts data into a hierarchy of decisions.

Today = intuition + vocabulary + manual reasoning.

Tomorrow we can move from "what is a tree?" → "how does a tree decide
the best split?"

**Week 20 target remains:** by the end of the week, you should be able
to build, interpret, tune, evaluate and explain Decision Tree
models---not merely call the sklearn API.
