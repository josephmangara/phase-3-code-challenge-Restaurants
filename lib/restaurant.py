#!/usr/bin/env python3

class Restaurant:
    def __init__(self, name):
        self.name = name

    def restaurant_name(self):
        print(self.name)

teryaki = Restaurant("Teryaki Japanses Delicacies")
teryaki.restaurant_name()


class Customer:
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name

    
    def given_name(self):
        print(self.name)
    
    def last_name(self):
        print(self.family_name)

    def full_name(self):
        print(f"{self.name} {self.family_name}")

janet = Customer("Janet", "Hansel")
janet.given_name()
janet.last_name()
janet.full_name()


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def restaurant_rating(self, value):
         if isinstance (value, (int, float)):
            return value 
         else:
            return None
         
bad = Review("Janet", "Teriyaki", 4.5)
print(bad.restaurant_rating(2.1))