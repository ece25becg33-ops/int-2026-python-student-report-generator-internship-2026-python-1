"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
    from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students
)
def format_report(records):
    lines = []
    lines.append(f"Total records: {len(records)}")
    subjects = sorted(subjects_offered(records))
    lines.append("Subjects: " + ", ".join(subjects))
    lines.append("")
    lines.append("Average Scores:")
    averages = average_per_student(records)
    for name in sorted(averages):
        lines.append(f"  {name}: {averages[name]}")
    name, avg = top_scorer(records)
    lines.append("")
    lines.append(f"Top Scorer: {name} ({avg})")
    passed = passing_students(records)
    lines.append("Passing Students: " + ", ".join(passed))
    return "\n".join(lines)


