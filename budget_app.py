class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.balance = 0
    
    def __str__(self):
        title = self.category.center(30, '*') + '\n'
        items = ''
        for item in self.ledger:
            items += f'{item["description"][:23]:23}{item["amount"]:>7.2f}\n'
        total = f'Total: {self.balance}'
        return title + items + total
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.balance


# def create_spend_chart(categories):
#     chart = 'Percentage spent by category\n'
#     spent = []
#     total_spent = 0
#     for category in categories:
#         total = 0
#         for item in category.ledger:
#             if item['amount'] < 0:
#                 total -= item['amount']
#         spent.append(total)
#         total_spent += total
    
#     for category in categories:
#         percentage = spent[categories.index(category)] / total_spent
#         chart += f'| '
#         for i in range(100, -10, -10):
#             if percentage * 100 >= i:
#                 chart += 'o  '
#             else:
#                 chart += '   '
    
#     chart += ' '*4 + '-'*(len(categories)*3 + 1) + '\n'
    
#     for i in range(0, 15):
#         chart += ' '*5
#         for category in categories:
#             if len(category.category) > i:
#                 chart += category.category[i] + '  '
#             else:
#                 chart += '   '
#         if i != 14:
#             chart += '\n'
    
#     return chart
def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    spent = []
    total_spent = 0
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total -= item['amount']
        spent.append(total)
        total_spent += total
    
    percentages = [int((spend / total_spent) * 100) for spend in spent]
    
    for i in range(100, -10, -10):
        chart += f'{i:>3}| '
        for percentage in percentages:
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    
    chart += ' '*4 + '-'*(len(categories)*3 + 1) + '\n'
    
    max_length = max(len(category.category) for category in categories)
    for i in range(max_length):
        chart += ' '*5
        for category in categories:
            if len(category.category) > i:
                chart += category.category[i] + '  '
            else:
                chart += '   '
        if i != max_length - 1:
            chart += '\n'
    
    return chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))