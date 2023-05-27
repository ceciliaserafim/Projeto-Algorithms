def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    quantity_students = 0
    for init_time, final_time in permanence_period:
        if not isinstance(init_time, int) or not isinstance(final_time, int):
            return None
# Retorne a quantidade de estudantes presentes para uma entrada específica;
        if init_time <= target_time <= final_time:
            quantity_students += 1
    return quantity_students
