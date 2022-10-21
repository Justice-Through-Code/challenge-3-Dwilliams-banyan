
def stock_purchases():
    stocks = {
        'Amazon': 3000,
        'Apple': 100,
        'Fb': 250,
        'Google': 1400,
        'Msft': 200
    }

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    client = input('What is your name? ')
    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    investing_amount = input("How much would you like to invest? $")
    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")
    
    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    if stock_name == 'Amazon':
        shares = int(investing_amount) / stocks['Amazon']
    elif stock_name == 'Apple':
        shares = int(investing_amount) / stocks['Apple']
    elif stock_name == 'Facebook':
        shares = int(investing_amount) / stocks['Fb']
    elif stock_name == 'Google':
        shares = int(investing_amount) / stocks['Google']
    elif stock_name == 'Microsoft':
        shares = int(investing_amount) / stocks['Msft']
    else:
        print(f'Could not find {stock_name} please try again.')


    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
    shares = int(shares)
    print(f'{client} has ${investing_amount} to invest and can buy {shares} shares of {stock_name} at the current price of ${stocks[stock_name]}.')
# stock_purchases()