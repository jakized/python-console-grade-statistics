# Student Results Statistics

This Python program is part of MOOC Helsinki course. Application collects and analyzes student results. It calculates and displays statistics based on exam points and completed exercises.

## How It Works

1. **Input**: Enter exam points (0-20) and number of exercises completed (0-100) for each student. Each entry should be on a new line in the format: `exam_points exercises_completed`.

2. **Processing**: The program will:
   - Convert exercise completion into exercise points (0-10).
   - Calculate the total points for each student.
   - Determine the final grade based on the total points.
   - Keep accepting inputs until an empty line is entered.

3. **Output**: The program prints:
   - **Average Points**: The average of all student points.
   - **Pass Percentage**: The percentage of students who passed.
   - **Grade Distribution**: The distribution of grades (0-5) as a bar chart.

## Grade Calculation

- **Final Grade** is determined based on total points:
  - 0-14: Fail
  - 15-17: Grade 1
  - 18-20: Grade 2
  - 21-23: Grade 3
  - 24-27: Grade 4
  - 28-30: Grade 5