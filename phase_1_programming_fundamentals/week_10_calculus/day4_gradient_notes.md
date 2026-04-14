# Day 4 — Gradient (AI Core)

## What is Gradient?

The gradient is a vector of partial derivatives of a multi-variable function.
It points in the direction of the **maximum increase** of the function.

---

## Formula

∇f(x, y) = (∂f/∂x, ∂f/∂y)

* ∇ (nabla): Gradient operator
* ∂f/∂x: Partial derivative w.r.t x
* ∂f/∂y: Partial derivative w.r.t y

---

## Intuition

* Gradient shows the direction where the function increases fastest
* Negative gradient (−∇f) shows the direction of fastest decrease
* Think of it like climbing a hill:

  * Gradient → go up
  * Negative gradient → go down (towards minimum)

---

## Example

Function:
f(x, y) = x² + y²

Partial derivatives:
∂f/∂x = 2x
∂f/∂y = 2y

Gradient:
∇f = (2x, 2y)

---

## Python Demo

```python
def grad(x, y):
    return 2*x, 2*y

x, y = 3, 4
gx, gy = grad(x, y)

print("Gradient:", gx, gy)
```

Output:
Gradient: 6 8

---

## ML Connection

* Gradient is used to update model parameters
* Helps in minimizing loss functions
* Core idea behind optimization algorithms

---

## Key Takeaways

* Gradient = vector of partial derivatives
* Points to direction of maximum increase
* Negative gradient is used for optimization
* Foundation of Gradient Descent and Deep Learning
