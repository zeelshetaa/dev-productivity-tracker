def estimate_coding_hours(commits):

    hours_per_commit = 0.5
    estimated_hours = commits * hours_per_commit

    if estimated_hours < 5:
        level = "Low Activity"
    elif estimated_hours < 20:
        level = "Moderate Activity"
    else:
        level = "High Activity"

    return estimated_hours, level
