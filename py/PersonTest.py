import json

from py.Person import Person

if __name__ == '__main__':
    p1 = Person("Ansberry", "Anvil").__dict__
    print(json.dumps(p1))
    p2 = Person("Bixby", "Brighton").__dict__
    persons = {"A": p1, "B": p2}
    persons["C"] = Person("Clive", "Conton").__dict__
    print(json.dumps(persons))