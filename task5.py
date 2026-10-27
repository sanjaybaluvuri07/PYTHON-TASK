# University Admission Decision Engine

applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nEnter details for applicant", i + 1)

    name = input("Enter name: ")
    course = input("Enter course (Engineering/Science/Commerce): ")

    maths = int(input("Enter Mathematics marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))
    commerce = int(input("Enter Commerce marks: "))

    aggregate = (maths + science + english + commerce) / 4

    if course == "Engineering":
        cutoff = 70
        eligible = maths >= 40 and science >= 40
    elif course == "Science":
        cutoff = 60
        eligible = science >= 40
    elif course == "Commerce":
        cutoff = 55
        eligible = commerce >= 40
    else:
        print("Invalid course!")
        continue

    eligible = eligible and aggregate >= cutoff

    applicants.append({
        "name": name,
        "course": course,
        "aggregate": aggregate,
        "maths": maths,
        "eligible": eligible
    })

# Sort eligible applicants by aggregate and Mathematics marks
ranked = sorted(
    [a for a in applicants if a["eligible"]],
    key=lambda a: (a["aggregate"], a["maths"]),
    reverse=True
)

print("\n--- Ranked List of Eligible Applicants ---")

if not ranked:
    print("No eligible applicants found.")
else:
    for rank, applicant in enumerate(ranked, start=1):
        print(
            rank, applicant["name"],
            applicant["course"],
            "Aggregate:", round(applicant["aggregate"], 2),
            "%"
        )

print("\n--- Ineligible Applicants ---")

for applicant in applicants:
    if not applicant["eligible"]:
        print(applicant["name"], "- Not Eligible")