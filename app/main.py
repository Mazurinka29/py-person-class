class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_new_persons = []
    for person_dict in people:
        new_person = Person(person_dict["name"], person_dict["age"])
        list_of_new_persons.append(new_person)
    for person_dict in people:
        if person_dict["wife"] is not None:
            Person.people[person_dict["name"]].wife \
                = Person.people[person_dict["wife"]]
        elif person_dict["husband"] is not None:
            Person.people[person_dict["name"]].wife \
                = Person.people[person_dict["husband"]]
    return list_of_new_persons
