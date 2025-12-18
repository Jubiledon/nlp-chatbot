from core.similarity import find_best_match

# Finds the most likely entitiy mentioned in the user input
# E.g. user_input: "I want to fly to London"
#      entities: ["New York", "London", "Paris",...]
#      returns: "London"
def extract_entity_from_text(user_input, entities):
    idx, score = find_best_match(user_input, entities)
    if score < 0.3:
        return None
    return entities[idx]