# Day 5 - Gradient Descent (Most Important)

## What is Gradient Descent?
Gradient Descent is an optimization algorithm used to find the minimum of a function.

It works by taking small steps in the direction opposite to the gradient (slope).

---

## Core Idea
- Start from a random value
- Calculate gradient (derivative)
- Move in opposite direction of gradient
- Repeat until minimum is reached

---

## Formula
x = x - lr * gradient

Where:
- x = current value
- lr = learning rate (step size)
- gradient = derivative of function

---

## Example 1: f(x) = x²

Derivative:
f'(x) = 2x

Python Code:
x = 5  
lr = 0.1  

for i in range(10):  
    grad = 2*x  
    x = x - lr*grad  
    print(x)  

Observation:
- Value gradually moves toward 0
- Minimum of x² is at x = 0

---

## Example 2: f(x) = x² + 4x + 4

Derivative:
f'(x) = 2x + 4

Python Code:
x = 5  
lr = 0.1  

for i in range(10):  
    grad = 2*x + 4  
    x = x - lr*grad  
    print(x)  

Fact:
- Function = (x + 2)²
- Minimum at x = -2

---

## Learning Rate (lr)
- Small lr → slow but stable
- Large lr → fast but unstable
- Perfect lr → fast and stable convergence

---

## Key Insights
- Gradient shows direction of increase
- We move in opposite direction to minimize loss
- Closer to minimum → smaller steps
- Same concept works in ML models

---

## Why Important?
Gradient Descent is the backbone of:
- Machine Learning
- Neural Networks
- Deep Learning
- LLM Training

---

## Final Understanding
Gradient Descent automatically finds the minimum of a function step-by-step.

This is how machines "learn".