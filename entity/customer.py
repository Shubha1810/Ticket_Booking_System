class Customer:
    def __init__(self, name, email, phone):
        self.customer_name = name
        self.email = email
        self.phone_number = phone

    def __eq__(self, other):
        return isinstance(other, Customer) and self.email == other.email

    def __hash__(self):
        return hash(self.email)

    def display_customer_details(self):
        print(f"{self.customer_name} | {self.email} | {self.phone_number}")
