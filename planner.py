# planner.py

def planner(state):
    profile = state["user_profile"]

    if profile["age"] is None:
        return {"action": "ask_age"}

    if profile["income"] is None:
        return {"action": "ask_income"}

    if profile["occupation"] is None:
        return {"action": "ask_occupation"}

    return {"action": "check_eligibility"}
