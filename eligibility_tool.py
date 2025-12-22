def check_eligibility(profile):
    schemes = []

    if profile["age"] >= 60:
        schemes.append("వృద్ధాప్య పెన్షన్")

    if profile["income"] <= 200000:
        schemes.append("ఆరోగ్య శ్రీ")

    if profile["occupation"] == "farmer":
        schemes.append("రైతు భరోసా")

    return schemes
