class Student:
    def __init__(self, student_id: str, full_name: str, department: str) -> None:
        self._student_id = student_id
        self._full_name = full_name
        self._department = department
        self._courses: list[str] = []

    def register_course(self, course_code: str) -> None:
        if course_code not in self._courses:
            self._courses.append(course_code)

    def get_course_count(self) -> int:
        return len(self._courses)

    def get_profile(self) -> str:
        return f"{self._student_id} | {self._full_name} | {self._department}"


if __name__ == "__main__":
    student = Student("1001", "Deniz Kaya", "Computer Information Systems")
    student.register_course("AII003")
    student.register_course("CIS386")

    print(student.get_profile())
    print(f"Registered courses: {student.get_course_count()}")
