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

Note: I did formatting last and I am running out of time, honestly could not refactor
some code  -> I truncated because the round function, even when specifying 2 decimal places,
would sometimes only return one decimal, could not fix in time after multiple testing
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
            "Sum": '{0:.2f}'.format(sum(current["loan_am"])),
            "Average": '{0:.2f}'.format(statistics.mean(current["loan_am"])),
            "Median": '{0:.2f}'.format(statistics.median(current["loan_am"])),
            "Minimum": '{0:.2f}'.format(min(current["loan_am"])),
            "Maximum": '{0:.2f}'.format(max(current["loan_am"])),
        },
        "SubjectAppraisedAmountSummary": {
            "Sum": '{0:.2f}'.format(sum(current["subject_am"])),
            "Average": '{0:.2f}'.format(statistics.mean(current["subject_am"])),
            "Median": '{0:.2f}'.format(statistics.median(current["subject_am"])),
            "Minimum": '{0:.2f}'.format(min(current["subject_am"])),
            "Maximum": '{0:.2f}'.format(max(current["subject_am"])),
        },
        "InterestRateSummary": {
            "Sum": '{0:.2f}'.format(sum(current["interest_rate"])),
            "Average": '{0:.2f}'.format(statistics.mean(current["interest_rate"])),
            "Median": '{0:.2f}'.format(statistics.median(current["interest_rate"])),
            "Minimum": '{0:.2f}'.format(min(current["interest_rate"])),
            "Maximum": '{0:.2f}'.format(max(current["interest_rate"])),
        },
    }

# print(by_state_summary)

monthlyByState_Braza = open(
    "C:/Users/VN MK3/Desktop/Silverworks_challenge/monthlyByState_Braza.json", "w", encoding="utf-8")

json.dump(by_state_summary, monthlyByState_Braza, ensure_ascii=False)

monthlyByState_Braza.close()
