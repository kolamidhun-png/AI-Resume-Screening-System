import csv
import os
import re


def load_skills():
    """
    Load skills from the project's skills.csv file.
    """
    skills_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "skills.csv"
    )

    skills = []

    with open(
        skills_path,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            skill = row.get("skill", "").strip().lower()

            if skill:
                skills.append(skill)

    return skills


def extract_skills(text):
    """
    Extract technical skills from resume or job-description text.
    """

    text = text.lower()

    skills = load_skills()

    found_skills = []

    for skill in skills:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill)
            + r"(?!\w)"
        )

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(found_skills)