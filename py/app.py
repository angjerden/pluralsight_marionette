#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask

from py.Person import Person

app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps(persons)


if __name__ == '__main__':
    persons = {}
    p1 = Person("Ansberry", "Anvil").__dict__
    p2 = Person("Bixby", "Brighton").__dict__
    persons = {"A": p1, "B": p2}
    persons["C"] = Person("Clive", "Conton").__dict__

    app.run()



