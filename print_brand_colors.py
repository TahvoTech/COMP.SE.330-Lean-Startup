import matplotlib.pyplot as plt

# Define the color palette with hex codes and names
colors = {
    "Deep Blue": "#1A4C78",
    "Muted Green": "#5A7F67",
    "Warm Beige": "#E8DCC1",
    "Soft Gray": "#C2C5BB",
    "Bright Orange": "#F2994A",
    "Light Teal": "#A8DADC",
    "Off-White": "#F9F9F7",
    "Charcoal Gray": "#4A4A4A"
}

# Generate a horizontal palette visualization
fig, ax = plt.subplots(figsize=(12, 2))
for i, (name, hex_code) in enumerate(colors.items()):
    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=hex_code))
    ax.text(i + 0.5, -0.3, name, ha="center", va="center", fontsize=9, color="black")

# Clean up the visualization
ax.set_xlim(0, len(colors))
ax.set_ylim(0, 1)
ax.axis("off")

plt.show()