import json
import requests

def convert_to_put(portfolio, deductible):
    #get total $ portfolio value
    total_value = 0
    for i, record in enumerate(portfolio):
        spot_price = get_price(record['coin'])
        portfolio[i]['spot_price'] = spot_price
        total_value += (spot_price * record['amount'])

    #finding weights of each asset to determine deductible proportion, then determining the necessary put option conversion
    for i, record in enumerate(portfolio):
        asset_amount = record['amount']
        asset_value = spot_price * asset_amount
        weight = asset_value / total_value
        portfolio[i]['deductible_proportion'] = asset_deductible = weight * deductible

        #determine necessary put option strike price
        minimum_threshold = 1 - (asset_deductible / asset_value)
        spot_price = portfolio[i]['spot_price']
        unadjusted_strike_price = minimum_threshold * spot_price
        portfolio[i]['unadjusted_strike'] = unadjusted_strike_price

    return portfolio


def get_price(coin):
    url = 'https://ftx.us/api/markets/{}/usd'.format(coin.lower())
    last = float(json.loads(requests.get(url).content)['result']['last'])
    return last

def get_portfolio_value(portfolio):
    total_value = 0
    for record in portfolio:
        spot_price = get_price(record['coin'])
        total_value += (spot_price * record['amount'])
    return total_value

def execute():
    records = []
    print('Hello! We\'ll be quoting an insurance contract for your portfolio.\n')
    print('First coin in your portfolio:')
    coin = input()
    print('\nAmount of {} held:'.format(coin))
    amount = input()
    records.append({'coin':coin, 'amount':float(amount)})
    print('\nDo you have any other coins you would like to add? (y/n)')
    answer = input()
    if answer.lower() == 'y':
        while True:
            print('\nCoin:')
            coin = input()
            print('\nAmount of {} held:'.format(coin))
            amount = input()
            records.append({'coin': coin, 'amount': float(amount)})
            print('\nDo you have any other coins you would like to add? (y/n)')
            answer = input()
            if answer == 'n':
                break
    portfolio_value = get_portfolio_value(records)
    print('\nYou have a total portfolio value of ${}!\n'
          'What would you like your deductible to be? This is the maximum amount your portfolio can dip by before receiving an insurance payout.\n'
          'For example, if your portfolio is worth $1000, you choose a $200 deductible, and your portfolio value drops to $500, you will be eligble for a $300 payout.\n'
          'Just like normal insurance, the higher the deductible, the less you have to pay in premiums!'.format(int(portfolio_value)))
    print('\nEnter amount:')
    deductible = input()
    put_portfolio = convert_to_put(records, float(deductible))

    setup_conclusion = '\n\nThanks! From the information you have given us, we can construct your desired portfolio insurance policy by purchasing:\n'
    print(setup_conclusion)
    record = put_portfolio[0]
    length = len(put_portfolio)
    if length > 1:
        l = 's'
        f = ''
    else:
        l = ''
        f = 'a '
    string = 'Put {}option{} for '.format(f, l) + record['coin'] + ' at strike price ' + str(int(record['unadjusted_strike']))
    if length > 1:
        for record in put_portfolio[1:]:
            string = string + ', ' + record['coin'] + ' at strike price ' + str(int(record['unadjusted_strike']))
    print(string)


