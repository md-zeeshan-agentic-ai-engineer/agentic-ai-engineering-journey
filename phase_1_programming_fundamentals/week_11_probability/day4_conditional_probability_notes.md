# Day 4 — Conditional Probability

## Definition

Conditional probability is the probability of an event **A occurring given that another event B has already occurred**.

---

## Formula

P(A | B) = P(A ∩ B) / P(B)

Where:

* P(A | B) = Probability of A given B
* P(A ∩ B) = Probability of both A and B
* P(B) = Probability of B

---

## Intuition

Conditional probability means **thinking with context**.

Instead of asking:

* "What is the chance of A?"

We ask:

* "What is the chance of A **when B is already true**?"

---

## Example 1: Cards

* Total cards = 52
* Red cards = 26
* Red Kings = 2

P(King | Red) = 2 / 26 = 1 / 13 ≈ 0.0769

---

## Example 2: Face Cards

* Total face cards (J, Q, K) = 12
* Kings = 4

P(King | Face Card) = 4 / 12 = 1 / 3 ≈ 0.333

---

## Real-Life Example

If it is raining:

* Probability of traffic increases

P(Traffic | Rain) > P(Traffic)

---

## AI Connection

Machine Learning models and LLMs work using conditional probability.

Example:

* Predict next word based on previous words

P(word | previous words)

The model selects the word with the highest probability.

---

## Python Example

```python
# Conditional probability example

# total red cards
red_cards = 26

# red kings
red_kings = 2

prob = red_kings / red_cards

print("P(King | Red) =", prob)
```

---

## Key Points

* Conditional probability = context-based prediction
* Core concept behind AI and ML models
* Used in language models, recommendation systems, and decision making

---

## Practice Task

1. Create 2 more real-life examples
2. Modify code for different conditions
3. Write intuition in your own words

---

## Summary

Conditional probability helps us make better predictions by using **available information (context)**.

AI systems = **probability machines working with context**
