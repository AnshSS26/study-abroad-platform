import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]

EXCEL_FILE = BASE_DIR / "data" / "study_abroad_database.xlsx"


def clean_value(value):
    if pd.isna(value):
        return None
    return value


def get_recommendations(request):

    programs = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Programs"
    )

    universities = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Universities"
    )


    df = programs.merge(
        universities,
        on="University_ID",
        how="inner"
    )


    df = df[
        df["Country"]
        .astype(str)
        .str.contains(
            request.preferred_country,
            case=False,
            na=False
        )
    ]


    df = df[
        df["Program_Name"]
        .astype(str)
        .str.contains(
            request.preferred_course,
            case=False,
            na=False
        )
    ]


    results = []


    for _, row in df.head(10).iterrows():

        score = 0
        reasons = []


        # Course match
        score += 40
        reasons.append("Preferred course available")


        # IELTS check
        if "IELTS_Min" in row and not pd.isna(row["IELTS_Min"]):
            if request.ielts >= row["IELTS_Min"]:
                score += 20
                reasons.append("IELTS requirement satisfied")


        # CGPA check
        if "Minimum_GPA" in row and not pd.isna(row["Minimum_GPA"]):
            if request.cgpa >= row["Minimum_GPA"]:
                score += 20
                reasons.append("CGPA requirement satisfied")


        # Budget check
        if "Tuition_Fee" in row and not pd.isna(row["Tuition_Fee"]):
            if request.maximum_budget >= row["Tuition_Fee"]:
                score += 20
                reasons.append("Within your budget")


        results.append({

            "university": clean_value(row.get("University_Name")),

            "program": clean_value(row.get("Program_Name")),

            "country": clean_value(row.get("Country")),

            "city": clean_value(row.get("City")),

            "tuition_fee": clean_value(row.get("Tuition_Fee")),

            "currency": clean_value(row.get("Tuition_Currency")),

            "scholarship": clean_value(row.get("Scholarship_Available")),

            "match_score": score,

            "reasons": reasons

        })


    # highest score first
    results = sorted(
        results,
        key=lambda x: x["match_score"],
        reverse=True
    )


    return results