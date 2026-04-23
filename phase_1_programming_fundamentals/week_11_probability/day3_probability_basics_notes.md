# Day 3 — Probability Basics

## 1. What is Probability?

Probability means the **chance of an event happening**.

* Value range: **0 to 1**

  * 0 → Impossible event
  * 1 → Certain event

---

## 2. Formula

P(A) = Number of favorable outcomes / Total number of outcomes

---

## 3. Examples

### Example 1: Coin Toss

* Outcomes: Head (H), Tail (T) → Total = 2
* Favorable (Head) = 1

P(Head) = 1/2 = 0.5

---

### Example 2: Dice Roll

* Outcomes: 1,2,3,4,5,6 → Total = 6
* Favorable (Even numbers: 2,4,6) = 3

P(Even) = 3/6 = 0.5

---

### Example 3: Card Draw

* Total cards = 52
* Favorable (Ace) = 4

P(Ace) = 4/52 = 1/13

---

## 4. Key Concepts

* Probability is **not exact**, it is an **approximation**
* More experiments → more accurate result
* Randomness causes slight variation

---

## 5. Python Simulation (Coin Toss)

```python
import random

results = [random.choice(['H','T']) for _ in range(1000)]
print(results.count('H')/1000)
```

Expected output ≈ 0.5

---

## 6. Real-World Insight (ML/AI)

* Machine Learning models output **probabilities**
* Example:

  * Spam detection → 0.9 (90% spam)
  * LLM → predicts next word probability

AI = Probability-based system

---

## 7. Practice Problems

1. Find probability of getting an odd number on a dice
2. Find probability of getting a red card from a deck
3. Find probability of getting tail in coin toss

---

## 8. Conclusion

* Probability measures uncertainty
* It is the foundation of Machine Learning
* Understanding this is critical for AI systems
