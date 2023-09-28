import matplotlib.pyplot as plt

# Data
steps = ['Step 1', 'Step 2', 'Step 3', 'Step 4']
ieee_papers = [79, 19, 16, 13]
acm_papers = [50, 10, 8, 6]
springer_papers = [572, 117, 31, 11]

# Define custom colors for each source
colors = ['#51ACF6', '#D9AEE4', '#BBCB98']

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Set the width of the bars
bar_width = 0.2

# Define the positions of bars on the x-axis
x = range(len(steps))

# Create bar plots for each source with custom colors
plt.bar(x, ieee_papers, width=bar_width, label='IEEE', color=colors[0])
plt.bar([i + bar_width for i in x], acm_papers, width=bar_width, label='ACM Digital Library', color=colors[1])
plt.bar([i + bar_width * 2 for i in x], springer_papers, width=bar_width, label='Springer Link', color=colors[2])

# Set the x-axis labels
ax.set_xticks([i + bar_width for i in x])
ax.set_xticklabels(steps)

# Add labels and title
plt.xlabel('Exclusion Criteria')
plt.ylabel('Number of Papers')
# plt.title('Number of Papers After Each Step')

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig('bar_graph.png')  # Change the file name and format as needed
plt.show()
