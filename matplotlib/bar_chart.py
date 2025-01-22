import matplotlib.pyplot as plt
import numpy as np

# Data for the bar plot
usn = ['USN1', 'USN2', 'USN3', 'USN4', 'USN5']
marks_math = [50, 70, 35, 28, 45]
marks_science = [60, 75, 40, 35, 55]
marks_english = [55, 65, 45, 30, 50]

# Setting up bar width and positions
bar_width = 0.25
index = np.arange(len(usn))

# Creating the grouped bar plot
plt.figure(figsize=(10, 6))
plt.bar(index, marks_math, width=bar_width, color='#a89e32', edgecolor='black', linewidth=2, label='Math')
plt.bar(index + bar_width, marks_science, width=bar_width, color='#2a9d8f', edgecolor='black', linewidth=2, label='Science')
plt.bar(index + 2 * bar_width, marks_english, width=bar_width, color='#e63946', edgecolor='black', linewidth=2, label='English')

# Adding labels and title
plt.xlabel('Students USN', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.title('Comparison of Students Marks in Different Subjects', fontsize=14, fontweight='bold')
plt.xticks(index + bar_width, usn)
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding data labels
for i in range(len(usn)):
    plt.text(index[i], marks_math[i] + 2, str(marks_math[i]), ha='center', fontsize=10, fontweight='bold')
    plt.text(index[i] + bar_width, marks_science[i] + 2, str(marks_science[i]), ha='center', fontsize=10, fontweight='bold')
    plt.text(index[i] + 2 * bar_width, marks_english[i] + 2, str(marks_english[i]), ha='center', fontsize=10, fontweight='bold')

# Display the plot
plt.show()
