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

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews_list)
        total_reviews = len(self.reviews_list) 
        if total_reviews == 0:
            return 0
        average = total_ratings / total_reviews
        return average


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

    def num_reviews(self):
        return len(self.reviews_list)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        else:
            return None
    
    @classmethod
    def find_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name() == given_name]

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
  
# Examples 
    
teryaki = Restaurant("Teryaki Japan")
instanoodles = Restaurant("Insta noodles")

# customer names 
janet = Customer("Janet", "Hansel")
melanie = Customer("Melanie", "S")
bond = Customer("Bond", "J")
cray = Customer("Cray", "W")
matt = Customer("Matt", "D")

review_janet = janet.add_review(teryaki, 3.8)
review_janet = janet.add_review(instanoodles, 3)
review_melanie = melanie.add_review(teryaki, 4.0)
review_bond = bond.add_review(instanoodles, 3.5)
review_cray = cray.add_review(instanoodles, 4.5)
review_cray = cray.add_review(teryaki, 3.8)
review_matt = matt.add_review(teryaki, 4.6)

# all customers and their reviews 
all_customers = Customer.all_customers
all_reviews = Review.all_reviews

print("All customers:")
for customer in all_customers:
    print(customer.full_name())

print("\nCustomer reviews:")
for review in all_reviews:
    print(review)

print("\nTeryaki Japan Restaurant reviews:")
for review in teryaki.reviews():
    print(review)

print("\nCustomers who reviewed Teryaki Japan:")
for customer in teryaki.customers():
    print(customer.full_name())

print("\nCustomers who reviewed Instanoodles:")
for customer in instanoodles.customers():
    print(customer.full_name())

print(f"\nNumber of reviews by Janet: {janet.num_reviews()}")

found_customer = Customer.find_by_name("Janet Hansel")
print(found_customer.full_name())

print(teryaki.average_star_rating())
print(instanoodles.average_star_rating())