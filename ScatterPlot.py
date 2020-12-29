import numpy as np
from matplotlib import pyplot as plt

# arrange graph co-ordinates and plot graph
college_exam_results = (90, 60, 80, 50 , 40, 30, 100)
student_age = (27, 24, 30, 21, 19, 21, 35)
plt.title("Exam results")
plt.xlabel("College exam grade")
plt.ylabel("Student Age")
plt.scatter(college_exam_results, student_age, alpha=0.8)
plt.show()