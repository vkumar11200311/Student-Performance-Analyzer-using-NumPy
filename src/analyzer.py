

import numpy as np

def student_average(scores):
    """
    Calculate average score of each student
    """
    return np.mean(scores, axis=1)


def subject_average(scores):
    """
    Calculate average score for each subject
    """
    return np.mean(scores, axis=0)


def top_performer(names, student_avg):
    """
    Identify the top performing student
    """
    index = np.argmax(student_avg)
    return names[index], student_avg[index]


def hardest_subject(subjects, subject_avg):
    """
    Find the subject with lowest average score
    """
    index = np.argmin(subject_avg)
    return subjects[index]


def pass_fail_analysis(scores, pass_marks=50):
    """
    Determine pass/fail status for students
    """
    pass_mask = scores >= pass_marks
    pass_count = np.sum(pass_mask, axis=1)
    return pass_count


def student_ranking(names, student_avg):
    """
    Rank students based on average scores
    """
    ranking = np.argsort(-student_avg)
    ranked_students = [(names[i], student_avg[i]) for i in ranking]
    return ranked_students


def grade_calculation(student_avg):
    """
    Assign grades using vectorized NumPy operations
    """
    grades = np.where(student_avg >= 90, "A",
             np.where(student_avg >= 80, "B",
             np.where(student_avg >= 70, "C",
             np.where(student_avg >= 60, "D", "F"))))
    
    return grades