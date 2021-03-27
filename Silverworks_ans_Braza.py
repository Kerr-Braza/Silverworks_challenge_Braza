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

Note: I did formatting last and I am running out of time, honestly could not refactor
some code -> I truncated because the round function, even when specifying 2 decimal places,
would sometimes only return one decimal
'''

summary = {
    "LoanAmountSummary": {
        "Sum": '{0:.2f}'.format(sum(loan_am)),
        "Average": '{0:.2f}'.format(statistics.mean(loan_am)),
        "Median": '{0:.2f}'.format(statistics.median(loan_am)),
        "Minimum": '{0:.2f}'.format(min(loan_am)),
        "Maximum": '{0:.2f}'.format(max(loan_am)),
    },
    "SubjectAppraisedAmountSummary": {
        "Sum": '{0:.2f}'.format(sum(subject_am)),
        "Average": '{0:.2f}'.format(statistics.mean(subject_am)),
        "Median": '{0:.2f}'.format(statistics.median(subject_am)),
        "Minimum": '{0:.2f}'.format(min(subject_am)),
        "Maximum": '{0:.2f}'.format(max(subject_am)),
    },
    "InterestRateSummary": {
        "Sum": '{0:.2f}'.format(sum(interest_rate)),
        "Average": '{0:.2f}'.format(statistics.mean(interest_rate)),
        "Median": '{0:.2f}'.format(statistics.median(interest_rate)),
        "Minimum": '{0:.2f}'.format(min(interest_rate)),
        "Maximum": '{0:.2f}'.format(max(interest_rate)),
    }
}

# print(summary)

monthlySummary_Braza = open(
    "C:/Users/VN MK3/Desktop/Silverworks_challenge/monthlySummary_Braza.json", "w", encoding="utf-8")

json.dump(summary, monthlySummary_Braza, ensure_ascii=False)

monthlySummary_Braza.close()
