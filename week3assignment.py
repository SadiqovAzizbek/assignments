class Prescription:
    def __init__(self, medication_name, price_per_pill, pill_count):
        self.medication_name = medication_name
        self.price_per_pill = price_per_pill
        self.pill_count = pill_count
    def __str__(self):
        return f"{self.medication_name}: {self.pill_count} pill(s) at ${self.price_per_pill}"
    def __repr__(self):
        return f"Prescription('{self.medication_name}', {self.price_per_pill}, {self.pill_count})"
    def __add__(self, other):
        if isinstance(other, Prescription):
            if self.medication_name == other.medication_name:
                return Prescription(self.medication_name, self.price_per_pill, self.pill_count + other.pill_count)
            else:
                return NotImplemented
        elif isinstance(other, int):
            return Prescription(self.medication_name, self.price_per_pill, self.pill_count + other)
        else:
            return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Prescription):
            return self.medication_name == other.medication_name and self.price_per_pill == other.price_per_pill
        else:
            return NotImplemented
    def __bool__(self):
        return self.pill_count > 0
    
script1 = Prescription("Amoxicillin", 1.2, 30)
script2 = Prescription("Amoxicillin", 1.2, 15)
script3 = Prescription("Ibuprofen", 0.8, 0)

print(str(script1))
print(repr(script1))
print(script1 + script2)
print(script1 + 10)
print(script1 == script2)
print(bool(script1))
print(bool(script3))