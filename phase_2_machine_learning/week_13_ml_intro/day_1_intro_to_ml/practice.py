
print("\nMachine Learning Journey Started 🚀")

# 1. Learning (Data understanding)

features = [1, 2, 3, 4, 5]
labels = [2, 4, 6, 8, 10]

print("\n========== LEARNING ==========")

for i in range(len(features)):
    print(f"Data point -> Input: {features[i]} => Output: {labels[i]}")


# 2. Model (Prediction Logic)

def predict(x):
    return 2 * x

print("\n========== PREDICTION ==========")
print(f"Predicted output for 10: {predict(10)}")


# 3. Classification

def classify(message):
    if "offer" in message.lower():
        return "Spam"
    return "Not Spam"

print("\n========== CLASSIFICATION ==========")
print(classify("Special offer just for you"))
print(classify("Hello friend"))


# 4. User Interaction

try:
    user_input = int(input("\nEnter a number: "))

    print("\n========== INTERACTION ==========")
    print(f"Predicted output for {user_input}: {predict(user_input)}")

except:
    print("Invalid input")


# Final insight:
# ML = Learn pattern from data -> Use it to predict -> Apply in real-world