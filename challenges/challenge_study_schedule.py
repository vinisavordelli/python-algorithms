def study_schedule(permanence_period, target_time):
    students_online = 0
    if target_time is None:
        return None
    for startingTime, endingTime in permanence_period:
        if not isinstance(startingTime, int) or not isinstance(
            endingTime, int
        ):
            return None
        if target_time >= startingTime and target_time <= endingTime:
            students_online += 1
    return students_online
