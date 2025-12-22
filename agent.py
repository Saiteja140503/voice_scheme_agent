from agent_state import agent_state
from eligibility_tool import check_eligibility
from scheme_tool import get_scheme_info

def agent_step(turn_id):
    state = agent_state

    # -------- TURN 0 : USER REQUEST --------
    if turn_id == 0:
        state["stage"] = "ASK_AGE"
        return "మీ వయస్సు ఎంత?"

    # -------- TURN 1 : AGE --------
    if turn_id == 1:
        state["memory"]["age"] = 65
        state["stage"] = "ASK_INCOME"
        return "మీ వార్షిక ఆదాయం ఎంత?"

    # -------- TURN 2 : INCOME --------
    if turn_id == 2:
        state["memory"]["income"] = 100000
        state["stage"] = "ASK_OCCUPATION"
        return "మీ వృత్తి ఏమిటి?"

    # -------- TURN 3 : OCCUPATION --------
    if turn_id == 3:
        state["memory"]["occupation"] = "farmer"
        state["stage"] = "EVALUATE"

        schemes = check_eligibility(state["memory"])

        response = (
            "మీ వివరాలను పరిశీలించాను.\n\n"
            "మీ వయస్సు అరవై ఐదు సంవత్సరాలు.\n"
            "మీ వార్షిక ఆదాయం ఒక లక్ష రూపాయలు.\n"
            "మీ వృత్తి రైతు.\n\n"
            "ఈ వివరాల ఆధారంగా మీరు ఈ ప్రభుత్వ పథకాలకి అర్హులు:\n"
        )

        for s in schemes:
            response += f"- {s}: {get_scheme_info(s)}\n"

        return response
