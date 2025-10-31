def calculate_study_points(subject_type, hours_studied, difficulty_level):
    hours_studied = int(hours_studied)
    if subject_type == 'mathematics' or subject_type == 'MATHEMATICS':
        if difficulty_level == 'low' or difficulty_level == 'LOW':
            return 12 * hours_studied
        if difficulty_level == 'medium' or difficulty_level == 'MEDIUM':
            return 18 * hours_studied
        if difficulty_level == 'high' or difficulty_level == 'HIGH':
            return 25 * hours_studied

    elif subject_type == 'sciences' or subject_type == 'SCIENCES':
        if difficulty_level == 'low' or difficulty_level == 'LOW':
            return 10 * hours_studied
        if difficulty_level == 'medium' or difficulty_level == 'MEDIUM':
            return 15 * hours_studied
        if difficulty_level == 'high' or difficulty_level == 'HIGH':
            return 20 * hours_studied

    elif subject_type == 'languages' or subject_type == 'LANGUAGES':
        if difficulty_level == 'low' or difficulty_level == 'LOW':
            return 8 * hours_studied
        if difficulty_level == 'medium' or difficulty_level == 'MEDIUM':
            return 12 * hours_studied
        if difficulty_level == 'high' or difficulty_level == 'HIGH':
            return 16 * hours_studied
    else:
        print('Please check your input (Try one of these: mathematics, sciences, languages)')

def calculate_mastery_index(semester_count, baseline_score, current_score):
    expected_score = 1000 + (semester_count * 100)
    score_range = expected_score - baseline_score
    mastery_percentage = (current_score - baseline_score) / score_range * 100
    return mastery_percentage

def determine_progress_tier(mastery_percent):
    if mastery_percent < 50:
        return 'Foundation Tier'
    elif mastery_percent <= 60:
        return 'Development Tier'
    elif mastery_percent <= 70:
        return 'Proficiency Tier'
    elif mastery_percent <= 85:
        return 'Excellence Tier'
    else:
        return 'Mastery Tier'

def calculate_achievement_score(points, hours, tier_modifier):
    base_score = points * 0.05 + hours * 2

    if tier_modifier == 'Foundation Tier':
        tier_multi = 0.5
    elif tier_modifier == 'Development Tier':
        tier_multi = 1.0
    elif tier_modifier == 'Proficiency Tier':
        tier_multi = 1.2
    elif tier_modifier == 'Excellence Tier':
        tier_multi = 1.5
    elif tier_modifier == 'Mastery Tier':
        tier_multi = 1.8
    else:
        tier_multi = 1.0
    return round(base_score * tier_multi, 1)

def needs_tutoring(study_weeks, total_hours, avg_mastery):
    if study_weeks >= 6 and avg_mastery < 50:
        return 'Yes'
    elif total_hours < 100 and avg_mastery < 60:
        return 'Yes'
    elif study_weeks >= 4 and avg_mastery < 40:
        return 'Yes'
    else:
        return 'No'
    
def generate_progress_report(student, subject_type, hours, difficulty_level, semester_count, baseline_score, current_score, study_weeks):

    print('ACADEMIC PROGRESS TRACKER')
    print('=' * 40)
    print(f"Progress Report for: {student}")
    print('-' * 40)
    print(f"Subject Type: {subject_type}")
    print(f"Hours Studied: {hours}")
    print(f"Difficulty Level: {difficulty_level}")

    points = calculate_study_points(subject_type, hours, difficulty_level)
    mastery = calculate_mastery_index(semester_count, baseline_score, current_score)
    tier = determine_progress_tier(mastery)
    achievement = calculate_achievement_score(points, hours, tier)
    tutoring = needs_tutoring(study_weeks, hours, mastery)

    print(f"Study Points: {points}")
    print("Mastery Analysis:")
    print(f"  Semesters: {semester_count}, Baseline: {baseline_score}, Current Score: {current_score}")
    print(f"  Mastery: {mastery:.1f}%")
    print(f"  Progress Tier: {tier}")
    print(f"Achievement Score: {achievement}")
    print(f"Study Weeks: {study_weeks}")
    print(f"Tutoring Needed: {tutoring}")

generate_progress_report('Parker', 'mathematics', 45, 'high', 3, 800, 1150, 3)
print()
generate_progress_report('Riley', 'sciences', 60, 'medium', 5, 900, 1300, 5)
print()
generate_progress_report('Cameron', 'languages', 30, 'low', 8, 850, 950, 7)