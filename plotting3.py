# Setting up the combined radar chart data for all states
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
colors = ["red", "green", "blue"]
state_labels = ["California", "Texas", "Oregon"]

# Plotting each state on the same radar chart
for state, color in zip(state_labels, colors):
    labels = list(percentage_change_states[state].keys())
    values = list(percentage_change_states[state].values())
    values += values[:1]  # Completing the loop for the radar chart
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]  # Closing the loop

    ax.fill(angles, values, color=color, alpha=0.25, label=f'{state} Change %')
    ax.plot(angles, values, color=color, linewidth=2)  # Plot data
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

# Add legend and title
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
plt.title('Racial Demographic Changes (2010 to 2019) in California, Texas, and Oregon', size=15)
plt.show()
