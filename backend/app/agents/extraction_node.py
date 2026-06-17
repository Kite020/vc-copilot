from app.agents.deck_extraction_agent import extract_startup_info


def extraction_node(state):

    startup_info = extract_startup_info(
        state["raw_deck_text"]
    )

    state.update(startup_info)

    return state