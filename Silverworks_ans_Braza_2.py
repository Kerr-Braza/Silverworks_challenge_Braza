import json
import statistics  # Used in median and average below, my pref for Py3

silv_loans = open(
    "C:/Users/VN MK3/Desktop/Silverworks_challenge/loans.json", "r", encoding="utf-8")
loans = json.load(silv_loans)
silv_loans.close()

'''
In contrast to the general summary of the previous,
to make the state grouping dynamic to the json data, I had to create
the dictionary here to organize and then calculate by state below
At least O(2n), linear to shift through, organize, and present by state
and I used optimal Python built-in functions and stats library for calculations on iterables
'''
by_state = dict()

for entry in loans:
    current = entry["SubjectState"]
    if(current not in by_state):
        by_state[current] = {
            "loan_am": [entry["LoanAmount"]],
            "subject_am": [entry["SubjectAppraisedAmount"]],
            "interest_rate": [entry["InterestRate"]],
        }

    else:
        by_state[current]["loan_am"].append(entry["LoanAmount"])
        by_state[current]["subject_am"].append(entry["SubjectAppraisedAmount"])
        by_state[current]["interest_rate"].append(entry["InterestRate"])


by_state_summary = dict()


for state in by_state:
    # The current state we are looking at in the dict
    current = by_state[state]

    by_state_summary[state] = {
        "LoanAmountSummary": {
            "Sum": sum(current["loan_am"]),
            "Average": statistics.mean(current["loan_am"]),
            "Median": statistics.median(current["loan_am"]),
            "Minimum": min(current["loan_am"]),
            "Maximum": max(current["loan_am"]),
        },
        "SubjectAppraisedAmountSummary": {
            "Sum": sum(current["subject_am"]),
            "Average": statistics.mean(current["subject_am"]),
            "Median": statistics.median(current["subject_am"]),
            "Minimum": min(current["subject_am"]),
            "Maximum": max(current["subject_am"]),
        },
        "InterestRateSummary": {
            "Sum": sum(current["interest_rate"]),
            "Average": statistics.mean(current["interest_rate"]),
            "Median": statistics.median(current["interest_rate"]),
            "Minimum": min(current["interest_rate"]),
            "Maximum": max(current["interest_rate"]),
        },
    }

# print(by_state_summary)

answer_2 = open(
    "C:/Users/VN MK3/Desktop/Silverworks_challenge/answer_2_Braza.txt", "w", encoding="utf-8")

json.dump(by_state_summary, answer_2, ensure_ascii=False)

answer_2.close()
