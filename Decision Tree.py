def decision_tree(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"

print(decision_tree(20))
