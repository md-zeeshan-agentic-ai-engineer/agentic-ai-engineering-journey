import json

# Step 1: Create Data
data = {
    "name": "Zeeshan",
    "skills": ["Python", "Git", "JSON"],
    "week": 4,
    "day": 2
}

# Step 2: Save to JSON file
with open("agent_memory.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved successfully!")

# Step 3: Load Data
with open("agent_memory.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded Data:", loaded_data)

# Step 4: Add new skill
loaded_data["skills"].append("API")

# Step 5: Save updated data
with open("agent_memory.json", "w") as f:
    json.dump(loaded_data, f, indent=4)

print("Skill added successfully!")

# Step 6: Print skills
print("Skills List:")
for skill in loaded_data["skills"]:
    print("-", skill)