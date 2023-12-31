from main import deduplicate_employees, couple_employees


def test_no_employee_removed_when_employees_contains_no_duplications() -> None:
    employees = [
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        },
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 47
        }
    ]

    dedup_employees = deduplicate_employees(employees)
    assert dedup_employees == employees


def test_duplicate_employee_removed_when_employees_contains_duplications() -> None:
    employees = [
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        },
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        }
    ]

    result_employees = [
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        }
    ]
    dedup_employees = deduplicate_employees(employees)
    assert dedup_employees == result_employees


def test_couple_employee_when_employees_contains_2() -> None:
    employees = [
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        },
        {
            "department": "R&D",
            "name": "Saige Castro",
            "age": 48
        }
    ]

    expected_couples = [("Nikolas Porter", "Saige Castro")]
    couples = couple_employees(employees)
    assert couples == expected_couples


def test_couple_employee_when_employees_contains_less_then_2() -> None:
    employees = [
        {
            "department": "R&D",
            "name": "Nikolas Porter",
            "age": 46
        }
    ]

    expected_couples = None
    couples = couple_employees(employees)
    assert couples == expected_couples


def test_couple_employee_when_employees_contains_odd_number() -> None:
    employees = [
        {
            "department": "Sales",
            "name": "Wilson Medina",
            "age": 36
        },
        {
            "department": "Support",
            "name": "Justice Boyle",
            "age": 37
        },
        {
            "department": "Support",
            "name": "Mina Caldwell",
            "age": 44
        }
    ]

    expected_couples = [("Wilson Medina", "Justice Boyle"),
                        ("Justice Boyle", "Mina Caldwell"),
                        ("Mina Caldwell", "Wilson Medina")]

    couples = couple_employees(employees)
    assert couples == expected_couples


def test_couple_employee_when_employees_contains_even_number() -> None:
    employees = [
        {
            "department": "Sales",
            "name": "Wilson Medina",
            "age": 36
        },
        {
            "department": "Support",
            "name": "Justice Boyle",
            "age": 37
        },
        {
            "department": "Support",
            "name": "Mina Caldwell",
            "age": 44
        },
        {
            "department": "Sales",
            "name": "Dario Robertson",
            "age": 23
        }
    ]

    expected_couples = [("Wilson Medina", "Justice Boyle"),
                        ("Justice Boyle", "Mina Caldwell"),
                        ("Mina Caldwell", "Dario Robertson"),
                        ("Dario Robertson", "Wilson Medina")]

    couples = couple_employees(employees)
    assert couples == expected_couples
