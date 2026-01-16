def create_patient_index(daily_schedule):
    return {patient['ssn']: patient['patient_name'] for patient in daily_schedule}

def audit_check_ins(patient_index, arrived_ssns):
    scheduled_ssns = set(patient_index.keys())
    arrived_set = set(arrived_ssns)

    missed_appointments = scheduled_ssns - arrived_set
    walk_in_patients = arrived_set - scheduled_ssns

    return missed_appointments, walk_in_patients

def list_no_shows(patient_index, missed_set):
    report = [f"NO-SHOW: {patient_index[ssn].upper()}" for ssn in missed_set]
    report.sort()
    return report
schedule = [
    {'ssn': 11122, 'patient_name': "John Doe"},
    {'ssn': 33344, 'patient_name': "Jane Smith"},
    {'ssn': 55566, 'patient_name': "Emily Blunt"}
]

arrived = [11122, 55566, 77788]

patient_index = create_patient_index(schedule)
missed, walk_ins = audit_check_ins(patient_index, arrived)
report = list_no_shows(patient_index, missed)

print(f"Missed Appointments: {missed}")
print(f"Walk-ins: {walk_ins}")
print(f"Report: {report}")
