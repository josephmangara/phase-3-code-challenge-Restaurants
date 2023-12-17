#!/usr/bin/env python3

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews_list = []

    def restaurant_name(self):
        return self.name
    
    def reviews(self):
        return self.reviews_list
    
    def customers(self):
        return list(set(review.customer for review in self.reviews_list))

class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self.reviews_list = []
        Customer.all_customers.append(self)
    
    def given_name(self):
        return self.name
    
    def last_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.name} {self.family_name}"
    
    def restaurants(self):
        return (list(review.restaurant for review in self.reviews_list))
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews_list.append(new_review)
        restaurant.reviews_list.append(new_review)
    @classmethod
    def all(cls):
        return cls.all_customers

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def restaurant_rating(self, value):
         if isinstance (value, (int, float)):
            return value 
         else:
            return "Enter a valid number"
        
    def __str__(self):
        return f"{self.customer.full_name()}, Restaurant: {self.restaurant} -> {self.rating}"

         
    @classmethod
    def all(cls):
        return cls.all_reviews
         

teryaki = Restaurant("Teryaki Japan")
instanoodles = Restaurant("Insta noodles")
print(teryaki.restaurant_name())

# Examples 
# customer names 
janet = Customer("Janet", "Hansel")
melanie = Customer("Melanie", "S")
bond = Customer("Bond", "J")
cray = Customer("Cray", "W")
matt = Customer("Matt", "D")

# customer reviews 
review_janet = Review(janet, "Teryaki Japan", 2)
review_melanie = Review(melanie, "Teryaki Japan", 4.0)
review_bond = Review(bond, "Insta noodles", 3.5)
review_cray = Review(cray, "Insta noodles", 4.8)
review_matt = Review(matt, "Teryaki Japan", 3.2)

# all customers and their reviews 
all_customers = Customer.all()
all_reviews = Review.all()

print("All customers:")
for customer in all_customers:
    print(customer.full_name())

print("\nCustomer reviews:")
for review in all_reviews:
    print(review)