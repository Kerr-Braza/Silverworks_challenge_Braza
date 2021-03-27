import json
import statistics  # Used in median and average below, my pref for Py3

silv_loans = open(
    "C:/Users/VN MK3/Desktop/Silverworks_challenge/loans.json", "r", encoding="utf-8")
loans = json.load(silv_loans)
silv_loans.close()

'''
While I thought of separating the three arrs as values in a single dictionary, for general
summaries, I thought doing the operations on three separate arrays to be quicker
'''
loan_am = []
subject_am = []
interest_rate = []

for entry in loans:
    loan_am.append(entry["LoanAmount"])
    subject_am.append(entry["SubjectAppraisedAmount"])
    interest_rate.append(entry["InterestRate"])

'''
Focused on readability below, copying the structure in the readme file
and doing the operations line by line.
'''

summary = {
    "LoanAmountSummary": {
        "Sum": sum(loan_am),
        "Average": statistics.mean(loan_am),
        "Median": statistics.median(loan_am),
        "Minimum": min(loan_am),
        "Maximum": max(loan_am),
    },
    "SubjectAppraisedAmountSummary": {
        "Sum": sum(subject_am),
        "Average": statistics.mean(subject_am),
        "Median": statistics.median(subject_am),
        "Minimum": min(subject_am),
        "Maximum": max(subject_am),
    },
    "InterestRateSummary": {
        "Sum": sum(interest_rate),
        "Average": statistics.mean(interest_rate),
        "Median": statistics.median(interest_rate),
        "Minimum": min(interest_rate),
        "Maximum": max(interest_rate),
    }
}

answer_1 = open(
    "C:/Users/VN MK3/Desktop/Silverworks_challenge/answer_1_Braza.txt", "w", encoding="utf-8")

json.dump(summary, answer_1, ensure_ascii=False)

answer_1.close()
