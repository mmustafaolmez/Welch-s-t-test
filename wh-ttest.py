import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind
from matplotlib.lines import Line2D

# Data for Team 1
team1_num_of_assert = [18, 65, 34, 83, 31, 30, 54, 52]
team1_num_of_test = [12, 33, 32, 73, 20, 20, 31, 36]

# Data for Team 2
team2_num_of_assert = [0, 22, 0, 3, 12, 5, 3, 26, 20]
team2_num_of_test = [0, 12, 0, 2, 4, 14, 15, 16, 12]

# Perform Welch's t-test for assertions
t_statistic_assert, p_value_assert = ttest_ind(team1_num_of_assert, team2_num_of_assert, equal_var=False)

# Perform Welch's t-test for tests
t_statistic_test, p_value_test = ttest_ind(team1_num_of_test, team2_num_of_test, equal_var=False)

# Create a combined bar chart for assertions and tests
plt.figure(figsize=(7, 3))  # Smaller figure size

# Define soft red color
team2_color = '#FF6347'  # Tomato (Soft Red)

# Bar chart for assertions
bar_width = 0.35
index_assert = np.arange(2)
plt.subplot(1, 2, 1)
bars = plt.bar(index_assert, [np.mean(team1_num_of_assert), np.mean(team2_num_of_assert)],
               yerr=[np.std(team1_num_of_assert), np.std(team2_num_of_assert)],
               width=bar_width, tick_label=['', ''],
               capsize=5, color=['lightblue', team2_color])

# Remove frames and ticks
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().tick_params(axis='y', which='both', left=False, labelsize=8)

plt.ylabel('Number of Assertions Added (mean)', fontsize=10)
#plt.xticks(index_assert, ['Teams used test skeletons', 'Teams that did not use test skeletons'], fontsize=10, rotation=7)  # Rotate labels by 45 degrees
plt.text(0.5, max(np.mean(team1_num_of_assert), np.mean(team2_num_of_assert)) + 5,
         f'T-stat: {t_statistic_assert:.4f}\n p-value: {p_value_assert:.4f}', ha='center')


# Bar chart for tests
bar_width = 0.35
index_test = np.arange(2)
plt.subplot(1, 2, 2, sharey=plt.gca())  # Share y-axis with the first subplot
bars = plt.bar(index_test, [np.mean(team1_num_of_test), np.mean(team2_num_of_test)],
               yerr=[np.std(team1_num_of_test), np.std(team2_num_of_test)],
               width=bar_width, tick_label=[' ', ' '],
               capsize=5, color=['lightblue', team2_color])

# Remove frames and ticks
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().tick_params(axis='y', which='both', left=False, labelsize=8)

plt.ylabel('Number of Tests Added (mean)', fontsize=10)
#plt.xticks(index_test, [' ', ' '], fontsize=10, rotation=7)  # Rotate labels by 45 degrees

plt.text(0.5, max(np.mean(team1_num_of_test), np.mean(team2_num_of_test)) + 5,
         f'T-stat: {t_statistic_test:.4f}\n p-value: {p_value_test:.4f}', ha='center')


# Add legend with explicit colors
legend_labels = ['Teams used test skeletons', 'Teams that did not use test skeletons']
legend_colors = ['lightblue', team2_color]

# Create handles for each color and label pair
legend_handles = [Line2D([0], [0], color=color, label=label) for color, label in zip(legend_colors, legend_labels)]

legend_handles.append(plt.errorbar([], [], yerr=[], fmt='none', ecolor='black', capsize=5, label='Error Bars'))
# Add legend using the handles
plt.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1, 1),fontsize='small')

plt.tight_layout()

# Show the combined plot
plt.show()
