def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students = 0
    for star_period, finish_period in permanence_period:
        if isinstance(star_period, int) or isinstance(finish_period, int):
            return None
# Retorne a quantidade de estudantes presentes para uma entrada específica;
    if star_period <= target_time <= finish_period:
        students += 1
    # raise NotImplementedError
