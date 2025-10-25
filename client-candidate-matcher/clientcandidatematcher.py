class Client:
    def __init__(self, name, required_skills):
        self.name = name
        self.required_skills = set(required_skills)

    def __str__(self):
        return f"Client: {self.name}, Skills Needed: {', '.join(self.required_skills)}"


class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = set(skills)

    def __str__(self):
        return f"Candidate: {self.name}, Skills: {', '.join(self.skills)}"


class StaffingAgency:
    def __init__(self):
        self.clients =[]
        self.candidates = []

    def add_client(self, name, required_skills):
        client = Client(name, required_skills)
        self.clients.append(client)
        print(f"Added {client}")

    def add_candidate(self, name, skills):
        candidate = Candidate(name, skills)
        self.candidates.append(candidate)
        print(f"Added {candidate}")

    def match_candidates(self):
        for client in self.clients:
            print(f"\nMatching candidates for {client.name}:")
            matched = False
            for candidate in self.candidates:
                if client.required_skills.issubset(candidate.skills):
                    print(f"  - {candidate.name} matches the requirements.")
                    matched = True
            if not matched:
                print("  No suitable candidates found.")


def main():
    agency = StaffingAgency()

    # Sample data
    agency.add_client("TechCorp", ["Python", "Django", "SQL"])
    agency.add_candidate("Ram", ["Python", "Django", "SQL", "AWS"])
    agency.add_candidate("Kavi", ["Java", "Spring", "SQL"])

    agency.match_candidates()


if __name__ == "__main__":
    main()
