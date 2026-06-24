import json

def find_schemes(user_data):

    with open(
        "data/schemes.json",
        "r",
        encoding="utf-8"
    ) as file:

        schemes = json.load(file)

    eligible = []

    for scheme in schemes:

        occupation_match = (
            scheme["occupation"] == "Any"
            or
            scheme["occupation"] ==
            user_data["occupation"]
        )

        income_match = (
            user_data["income"]
            <=
            scheme["max_income"]
        )
        age_match = (
        user_data["age"] >= scheme["min_age"]
        and
        user_data["age"] <= scheme["max_age"]
        )
        gender_match = (
        scheme["gender"] == "Any"
        or
        scheme["gender"] == user_data["gender"]
        )

        category_match = (
            scheme["category"] == "Any"
            or
            scheme["category"] == user_data["category"]
        )

        age_match = (
            user_data["age"] >= scheme["min_age"]
            and
            user_data["age"] <= scheme["max_age"]
        )

        print("User Occupation:", user_data["occupation"])
        print("Scheme:", scheme["name"])
        print("Occupation Match:", occupation_match)
        print("Income Match:", income_match)
        print("----------------")
        if occupation_match and income_match and age_match and gender_match and category_match:

            eligible.append(scheme)

    return eligible