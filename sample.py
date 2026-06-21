def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        return average(self.scores)

    def report(self):
        return f"{self.name}: avg={self.average_score()}, max={find_max(self.scores)}"


if __name__ == "__main__":
    students = [
        Student("Alice", [90, 85, 95]),
        Student("Bob", []),
    ]
    for s in students:
        print(s.report())
