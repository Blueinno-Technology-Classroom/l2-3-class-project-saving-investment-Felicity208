##################################################
'''
Q1: 
'''

# TODO: Write your code here

currentBalance = 1000
interest= 0
deposit = 100
newBalance = 0

for i in range(1, 26):
    interest = currentBalance * 0.065
    newBalance = (currentBalance * 0.065) + currentBalance 
    print(f'{i:02d}. Current balance: {currentBalance:.2f}, interest: {interest:.2f}, deposit: {deposit}, new balance: {newBalance:.2f}')
    currentBalance = newBalance
    currentBalance += deposit 
    
##################################################
'''
Q2:
'''

# TODO: Write your code here

##################################################
'''
Q3:
'''

# TODO: Write your code here

##################################################
'''
Q4:
'''

# TODO: Write your code here

##################################################
'''
Q5:
'''

# TODO: Write your code here

##################################################
'''
Q6:
'''

# TODO: Write your code here

##################################################
