# Student Class Diagram to Code

This project maps a Student UML class diagram to Python.

## Student Class Diagram

```
+ -------------------------------------------------- +
|  Student                                           |
+ -------------------------------------------------- +
|  - _student_id: str                                |
|  - _full_name: str                                 |
|  - _department: str                                |
|  - _courses: list[str]                             |
+ -------------------------------------------------- +
|  + __init__(student_id, full_name, department)     |
|  + register_course(course_code): None              |
|  + get_course_count(): int                         |
|  + get_profile(): str                              |
+ -------------------------------------------------- +
```

## Run the program

`python student.py`
