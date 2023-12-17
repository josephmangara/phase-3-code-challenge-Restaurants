#!/usr/bin/env python3

class Restaurant:
    def __init__(self, name):
        self.name = name


class Customer:
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name

    
    def given_name(self):
        print(self.name)
    
    def last_name(self):
        print(self.family_name)

    def full_name(name, family_name):
        print(f"{name} {family_name}")

janet = Customer("Janet", "Hansel")

janet.given_name()
janet.last_name()
Customer.full_name("Janet", "Hansel")


class Review:
    def __init__(self):
        pass