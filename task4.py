
# Examination Result and Grace-Mark Validation System

# Configurable examination policies
PASS_PERCENTAGE = 35
MAX_GRACE_PER_SUBJECT = 5
MAX_TOTAL_GRACE = 10
MAX_MARKS_PER_SUBJECT = 100


def validate_marks(marks, max_marks):
    """Validate marks against the subject maximum."""
    if marks < 0 or marks > max_marks:
        raise ValueError(
            f"Marks must be between 0 and {max_marks}."
        )


def process_results(subjects):
    """Apply grace marks and calculate final results."""
    results = []
    total_original = 0
    total_final = 0
    total_maximum = 0
    total_grace_used = 0
    all_subjects_passed = True

    for subject in subjects:
        name = subject["name"]
        marks = subject["marks"]
        maximum = subject["maximum"]
        pass_marks = subject["pass_marks"]

        validate_marks(marks, maximum)

        if pass_marks < 0 or pass_marks > maximum:
            raise ValueError(
                f"Invalid pass marks for {name}."
            )

        total_original += marks
        total_maximum += maximum

        # Grace marks are allowed only for a subject
        # where the student narrowly fails.
        deficit = max(0, pass_marks - marks)
        grace = 0

        if deficit > 0 and deficit <= MAX_GRACE_PER_SUBJECT:
            grace = deficit

        final_marks = min(marks + grace, maximum)

        # Check whether the student passes the subject.
        passed = final_marks >= pass_marks

        if not passed:
            all_subjects_passed = False

        total_grace_used += grace
        total_final += final_marks

        results.append({
            "name": name,
            "original": marks,
            "grace": grace,
            "final": final_marks,
            "maximum": maximum,
            "passed": passed
        })

    # Enforce the overall grace-mark limit.
    # If exceeded, remove grace marks from the last eligible
    # subjects first, then recalculate the final results.
    if total_grace_used > MAX_TOTAL_GRACE:
        excess = total_grace_used - MAX_TOTAL_GRACE

        for result in reversed(results):
            reduction = min(result["grace"], excess)
            result["grace"] -= reduction
            result["final"] -= reduction
            excess -= reduction

            if excess == 0:
                break

        # Recalculate totals and subject results.
        total_grace_used = 0
        total_final = 0
        all_subjects_passed = True

        for result, subject in zip(results, subjects):
            result["passed"] = (
                result["final"] >= subject["pass_marks"]
            )
            total_grace_used += result["grace"]
            total_final += result["final"]

            if not result["passed"]:
                all_subjects_passed = False

    percentage = (
        total_final / total_maximum * 100
        if total_maximum > 0 else 0
    )

    # Final classification
    if not all_subjects_passed:
        classification = "FAIL"
    elif percentage >= 75:
        classification = "DISTINCTION"
    elif percentage >= 60:
        classification = "FIRST CLASS"
    elif percentage >= 50:
        classification = "SECOND CLASS"
    else:
        classification = "PASS"

    return {
        "results": results,
        "total_original": total_original,
        "total_final": total_final,
        "total_maximum": total_maximum,
        "grace_used": total_grace_used,
        "percentage": percentage,
        "classification": classification
    }


def display_report(student_name, report):
    """Print the student's examination report."""
    print("\n========== EXAMINATION RESULT ==========")
    print(f"Student: {student_name}")
    print("-" * 72)
    print(
        f"{'Subject':<18}{'Original':>10}"
        f"{'Grace':>8}{'Final':>8}{'Maximum':>10}{'Status':>10}"
    )
    print("-" * 72)

    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"

        print(
            f"{result['name']:<18}"
            f"{result['original']:>10}"
            f"{result['grace']:>8}"
            f"{result['final']:>8}"
            f"{result['maximum']:>10}"
            f"{status:>10}"
        )

    print("-" * 72)
    print(f"Original total : {report['total_original']}")
    print(f"Final total    : {report['total_final']}")
    print(f"Maximum total  : {report['total_maximum']}")
    print(f"Grace marks    : {report['grace_used']}")
    print(f"Percentage     : {report['percentage']:.2f}%")
    print(f"Classification : {report['classification']}")
    print("=" * 72)


def main():
    print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty.")
        return

    try:
        count = int(input("Enter number of subjects: "))

        if count <= 0:
            raise ValueError("Subject count must be positive.")

        subjects = []
        seen_names = set()

        for i in range(count):
            print(f"\nSubject {i + 1}")
            name = input("Subject name: ").strip()

            if not name or name.casefold() in seen_names:
                raise ValueError(
                    "Subject names must be nonempty and unique."
                )

            seen_names.add(name.casefold())

            maximum = float(
                input("Maximum marks: ")
            )
            pass_marks = float(
                input("Minimum passing marks: ")
            )
            marks = float(
                input("Marks obtained: ")
            )

            if maximum <= 0:
                raise ValueError("Maximum marks must be positive.")

            if not 0 <= pass_marks <= maximum:
                raise ValueError(
                    "Passing marks must be within the maximum."
                )

            validate_marks(marks, maximum)

            subjects.append({
                "name": name,
                "marks": marks,
                "maximum": maximum,
                "pass_marks": pass_marks
            })

        report = process_results(subjects)
        display_report(student_name, report)

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
