from creditCardValueCalc import *

class CreditCard:
    def __init__(self, name, reward_structure, point_value=0.01):
        self.name = name
        self.reward_structure = reward_structure  # Dictionary mapping MCC codes/categories to reward rates
        self.point_value = point_value  # Dollar value of each point/mile
        
    def calculate_reward(self, amount, mcc):
        """
        Calculate the reward value for a transaction based on this card's reward structure.
        
        Parameters:
        amount (float): Transaction amount in dollars
        mcc (int or str): Merchant Category Code of the transaction
        
        Returns:
        float: Dollar value of the reward
        """
        creditCardcategories = [
            'default',
            'Dining - Restaurants',
            'Travel - Transportation',
            'Grocery - Supermarkets and Grocery Stores',
            'Shipping',
            'Internet, Cable, Phone Services',
            'Travel - Lodging',
            'Dining',
            'Bonus points for multiple transactions',
            'Travel - Airlines',
            'Miles match for first year',
            'Gas Stations',
            'Entertainment',
            'Highest spending category',
            'Rounded up points on purchases',
            'Mobile Wallet Purchases',
            'Streaming Services',
            'Retail - Miscellaneous',
            'Office Supply Stores',
            'Drugstores',
            'Quarterly Rotating Categories',
            'U.S. Supermarkets',
            'Flights',
            'Hotels',
            'Prepaid Hotels',
            'Advertising Purchases',
            'Airfare',
            'Rotating Categories',
            'Amazon.com',
            'Whole Foods',
            'Disney Purchases',
            'Starbucks Purchases',
            'Top 2 Business Categories',
            'Purchases over $5000',
            'First $50000 Spent Annually',
            'Hyatt Purchases',
            'IHG Purchases',
            'Marriott Purchases',
            'Delta Purchases',
            'Southwest Purchases',
            'United Purchases',
            'British Airways Purchases',
            'Aer Lingus Purchases',
            'Iberia Purchases',
            'Top Spending Category',
            'JetBlue Purchases',
            'Wyndham Purchases',
            'Amazon Business Purchases',
            'Choice Category',
            'Two Categories of Choice',
            'Korean Air Purchases',
            'REI Purchases',
            'Carnival Purchases',
            'Princess Cruises Purchases',
            'Holland America Purchases',
            'Barnes & Noble Purchases'
            ]
        
        
        # Default reward rate (usually 1% or 1x)
        try:
            for category in self.reward_structure:
                reward_rate = self.reward_structure.get(category, 0.01)
        except:
            reward_rate = 0
       
        if reward is points:
        # Calculate reward value (points or cash back)
            reward_points = amount * reward_rate

            # Convert to dollar value
            reward_value = reward_points * self.point_value
            
        else:
            reward_value = amount * reward_rate



        return reward_value
    

    









    

chase_freedom_flex = CreditCard(
    name="Chase Freedom Flex",
    reward_structure={
        'default': 1,  # 1% cash back on all purchases
        'Dining - Restaurants': 3,  # 3% cash back on dining
        'Travel - Transportation': 3,  # 3% cash back on transit
        'Grocery - Supermarkets and Grocery Stores': 3  # 3% cash back on groceries
    },
    point_value=0.01  # Cash back value
)

chase_ink_business_preferred = CreditCard(
    name="Chase Ink Business Preferred",
    reward_structure={
        'Travel - Transportation': 3,  # 3x points on travel
        'Shipping': 3,  # 3x points on shipping
        'Internet, Cable, Phone Services': 3,  # 3x points on these services
        'default': 1  # 1x points on everything else
    },
    point_value=0.0125  # Points worth 1.25 cents each when used for travel
)

chase_world_of_hyatt = CreditCard(
    name="Chase World of Hyatt",
    reward_structure={
        'Travel - Lodging': 4,  # 4x points on Hyatt stays
        'Dining - Restaurants': 2,  # 2x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.015  # Hyatt points valued at 1.5 cents each
)

# Remaining American Express Cards
amex_green = CreditCard(
    name="American Express Green Card",
    reward_structure={
        'Travel - Transportation': 3,  # 3x points on travel
        'Dining - Restaurants': 3,  # 3x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Amex points valued at 1 cent each
)

amex_everyday = CreditCard(
    name="American Express Everyday",
    reward_structure={
        'default': 1,  # 1x points on all purchases
        'Grocery - Supermarkets and Grocery Stores': 2,  # 2x points on groceries
        'Bonus points for multiple transactions': 2  # Additional points for multiple monthly transactions
    },
    point_value=0.01  # Amex points valued at 1 cent each
)

amex_everyday_preferred = CreditCard(
    name="American Express Everyday Preferred",
    reward_structure={
        'Grocery - Supermarkets and Grocery Stores': 3,  # 3x points on groceries
        'Dining - Restaurants': 2,  # 2x points on dining
        'Bonus points for multiple transactions': 3  # Additional points for multiple monthly transactions
    },
    point_value=0.01  # Amex points valued at 1 cent each
)

amex_cash_magnet = CreditCard(
    name="American Express Cash Magnet",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

# Discover Additional Cards
discover_it_miles = CreditCard(
    name="Discover it Miles",
    reward_structure={
        'Travel - Transportation': 1.5,  # 1.5x miles on all purchases
        'Miles match for first year': 2  # Implied miles match for first year
    },
    point_value=0.01  # Miles valued at 1 cent each
)

discover_it_chrome = CreditCard(
    name="Discover it Chrome",
    reward_structure={
        'default': 1,  # 1% cash back on all purchases
        'Dining - Restaurants': 2,  # 2% cash back on dining
        'Gas Stations': 2  # 2% cash back at gas stations
    },
    point_value=0.01  # Cash back value
)

# More Capital One Cards
capital_one_venture_x = CreditCard(
    name="Capital One Venture X",
    reward_structure={
        'Travel - Airlines': 2,  # 2x miles on travel
        'Travel - Lodging': 2,  # 2x miles on hotels
        'default': 1  # 1x miles on everything else
    },
    point_value=0.015  # Miles valued at 1.5 cents each
)

capital_one_savor = CreditCard(
    name="Capital One Savor",
    reward_structure={
        'Dining - Restaurants': 4,  # 4% cash back on dining
        'Entertainment': 4,  # 4% cash back on entertainment
        'Grocery - Supermarkets and Grocery Stores': 3,  # 3% cash back on groceries
        'default': 1  # 1% cash back on everything else
    },
    point_value=0.01  # Cash back value
)

capital_one_savorone = CreditCard(
    name="Capital One SavorOne",
    reward_structure={
        'Dining - Restaurants': 3,  # 3% cash back on dining
        'Entertainment': 3,  # 3% cash back on entertainment
        'Grocery - Supermarkets and Grocery Stores': 3,  # 3% cash back on groceries
        'default': 1  # 1% cash back on everything else
    },
    point_value=0.01  # Cash back value
)

# Citi Additional Cards
citi_premier = CreditCard(
    name="Citi Premier",
    reward_structure={
        'Travel - Transportation': 3,  # 3x points on travel
        'Dining - Restaurants': 3,  # 3x points on dining
        'Grocery - Supermarkets and Grocery Stores': 3,  # 3x points on groceries
        'Gas Stations': 3,  # 3x points on gas
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

citi_prestige = CreditCard(
    name="Citi Prestige",
    reward_structure={
        'Dining - Restaurants': 5,  # 5x points on dining
        'Travel - Transportation': 5,  # 5x points on travel
        'default': 1  # 1x points on everything else
    },
    point_value=0.015  # Points valued at 1.5 cents each
)

# Additional Credit Card Instances - Part 2

# Remaining Citi Cards
citi_custom_cash = CreditCard(
    name="Citi Custom Cash",
    reward_structure={
        'default': 1,  # 1% cash back on most purchases
        'Highest spending category': 5  # 5% cash back on top spending category (up to $500 per billing cycle)
    },
    point_value=0.01  # Cash back value
)

citi_rewards_plus = CreditCard(
    name="Citi Rewards+",
    reward_structure={
        'default': 1,  # 1x points on most purchases
        'Rounded up points on purchases': 2  # Points are rounded up to nearest 10 points
    },
    point_value=0.01  # Points valued at 1 cent each
)

# Additional Bank of America Cards
bank_of_america_travel_rewards = CreditCard(
    name="Bank of America Travel Rewards",
    reward_structure={
        'Travel - Transportation': 1.5,  # 1.5x points on travel
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

bank_of_america_unlimited_cash_rewards = CreditCard(
    name="Bank of America Unlimited Cash Rewards",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

bank_of_america_premium_rewards = CreditCard(
    name="Bank of America Premium Rewards",
    reward_structure={
        'Travel - Transportation': 2,  # 2x points on travel
        'Dining - Restaurants': 2,  # 2x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

# Wells Fargo Additional Cards
wells_fargo_autograph = CreditCard(
    name="Wells Fargo Autograph",
    reward_structure={
        'Travel - Transportation': 3,  # 3x points on travel
        'Dining - Restaurants': 3,  # 3x points on dining
        'Entertainment': 3,  # 3x points on entertainment
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

# U.S. Bank Additional Cards
us_bank_altitude_reserve = CreditCard(
    name="U.S. Bank Altitude Reserve",
    reward_structure={
        'Travel - Transportation': 3,  # 3x points on travel
        'Mobile Wallet Purchases': 3,  # 3x points on mobile wallet purchases
        'default': 1  # 1x points on everything else
    },
    point_value=0.015  # Points valued at 1.5 cents each
)

us_bank_altitude_go = CreditCard(
    name="U.S. Bank Altitude Go",
    reward_structure={
        'Dining - Restaurants': 4,  # 4x points on dining
        'Grocery - Supermarkets and Grocery Stores': 2,  # 2x points on groceries
        'Streaming Services': 2,  # 2x points on streaming
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

# Barclays Cards
barclays_arrival_plus = CreditCard(
    name="Barclays Arrival Plus",
    reward_structure={
        'Travel - Transportation': 2,  # 2x miles on travel
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

barclays_jetblue_plus = CreditCard(
    name="Barclays JetBlue Plus",
    reward_structure={
        'Travel - Airlines': 6,  # 6x points on JetBlue purchases
        'Dining - Restaurants': 2,  # 2x points on dining
        'Grocery - Supermarkets and Grocery Stores': 2,  # 2x points on groceries
        'default': 1  # 1x points on everything else
    },
    point_value=0.015  # Points valued at 1.5 cents each
)

# Other Bank Cards
hsbc_cash_rewards = CreditCard(
    name="HSBC Cash Rewards Mastercard",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

td_bank_double_up = CreditCard(
    name="TD Bank Double Up Credit Card",
    reward_structure={
        'default': 2  # 2% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

# Loyalty and Specialized Cards
usaa_rewards_visa = CreditCard(
    name="USAA Rewards Visa",
    reward_structure={
        'default': 1.25  # 1.25x points on all purchases
    },
    point_value=0.01  # Points valued at 1 cent each
)

navy_federal_cash_rewards = CreditCard(
    name="Navy Federal Credit Union cashRewards",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)


# Additional Credit Card Instances - Part 3

# Remaining Chase Cards
chase_ink_business_cash = CreditCard(
    name="Chase Ink Business Cash",
    reward_structure={
        'Office Supply Stores': 5,  # 5% cash back on office supplies
        'Internet, Cable, Phone Services': 5,  # 5% cash back on these services
        'Dining - Restaurants': 2,  # 2% cash back on dining
        'Travel - Transportation': 2,  # 2% cash back on travel
        'default': 1  # 1% cash back on everything else
    },
    point_value=0.01  # Cash back value
)

chase_ink_business_unlimited = CreditCard(
    name="Chase Ink Business Unlimited",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

chase_freedom_student = CreditCard(
    name="Chase Freedom Student",
    reward_structure={
        'default': 1  # 1% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

chase_ihg_rewards_premier = CreditCard(
    name="Chase IHG Rewards Premier",
    reward_structure={
        'Travel - Lodging': 3,  # 3x points on IHG hotel stays
        'Dining - Restaurants': 2,  # 2x points on dining
        'Travel - Grocery': 2,  # 2x points on grocery
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

chase_marriott_bonvoy_boundless = CreditCard(
    name="Chase Marriott Bonvoy Boundless",
    reward_structure={
        'Travel - Lodging': 3,  # 3x points on Marriott stays
        'default': 1  # 1x points on everything else
    },
    point_value=0.0085  # Points valued at 0.85 cents each
)

# Additional American Express Cards
amex_blue_business_plus = CreditCard(
    name="American Express Blue Business Plus",
    reward_structure={
        'default': 2,  # 2x points on first $50,000 in purchases each year
    },
    point_value=0.01  # Points valued at 1 cent each
)

amex_business_gold = CreditCard(
    name="American Express Business Gold",
    reward_structure={
        'Shipping': 4,  # 4x points on shipping
        'Advertising Purchases': 4,  # 4x points on advertising
        'Gas Stations': 3,  # 3x points on gas
        'Dining - Restaurants': 3,  # 3x points on dining
        'Airfare': 3,  # 3x points on airfare
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

amex_business_platinum = CreditCard(
    name="American Express Business Platinum",
    reward_structure={
        'Travel - Airlines': 5,  # 5x points on flights
        'Prepaid Hotels': 5,  # 5x points on prepaid hotels
        'default': 1  # 1x points on everything else
    },
    point_value=0.02  # Points valued at 2 cents each
)

amex_hilton_honors = CreditCard(
    name="American Express Hilton Honors",
    reward_structure={
        'Travel - Lodging': 3,  # 3x points on Hilton stays
        'default': 1  # 1x points on everything else
    },
    point_value=0.005  # Points valued at 0.5 cents each
)

amex_hilton_honors_surpass = CreditCard(
    name="American Express Hilton Honors Surpass",
    reward_structure={
        'Travel - Lodging': 6,  # 6x points on Hilton stays
        'Dining - Restaurants': 3,  # 3x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.005  # Points valued at 0.5 cents each
)

# Discover Additional Cards
discover_it_student_cash_back = CreditCard(
    name="Discover it Student Cash Back",
    reward_structure={
        'default': 1,  # 1% cash back on all purchases
        'Rotating Categories': 5  # 5% cash back on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

discover_it_secured = CreditCard(
    name="Discover it Secured",
    reward_structure={
        'default': 1,  # 1% cash back on all purchases
        'Rotating Categories': 5  # 5% cash back on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

# Capital One Business Cards
capital_one_spark_cash_plus = CreditCard(
    name="Capital One Spark Cash Plus",
    reward_structure={
        'default': 2,  # 2% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

capital_one_spark_miles = CreditCard(
    name="Capital One Spark Miles",
    reward_structure={
        'default': 2,  # 2x miles on all purchases
    },
    point_value=0.01  # Miles valued at 1 cent each
)

# Additional Credit Card Instances - Part 4

# Remaining Citi Cards
citi_aadvantage_platinum_select = CreditCard(
    name="Citi AAdvantage Platinum Select",
    reward_structure={
        'Travel - Airlines': 2,  # 2x miles on American Airlines purchases
        'Dining - Restaurants': 2,  # 2x miles on dining
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

citi_aadvantage_executive = CreditCard(
    name="Citi AAdvantage Executive",
    reward_structure={
        'Travel - Airlines': 2,  # 2x miles on American Airlines purchases
        'default': 1  # 1x miles on everything else
    },
    point_value=0.015  # Miles valued at 1.5 cents each
)

citi_aadvantage_mileup = CreditCard(
    name="Citi AAdvantage MileUp",
    reward_structure={
        'Grocery - Supermarkets and Grocery Stores': 2,  # 2x miles on groceries
        'Travel - Airlines': 2,  # 2x miles on American Airlines purchases
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

# Additional Bank of America Cards
bank_of_america_alaska_airlines = CreditCard(
    name="Bank of America Alaska Airlines",
    reward_structure={
        'Travel - Airlines': 3,  # 3x miles on Alaska Airlines purchases
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

bank_of_america_spirit_airlines = CreditCard(
    name="Bank of America Spirit Airlines",
    reward_structure={
        'Travel - Airlines': 3,  # 3x miles on Spirit Airlines purchases
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

bank_of_america_cash_rewards_students = CreditCard(
    name="Bank of America Cash Rewards for Students",
    reward_structure={
        'default': 1,  # 1% cash back on all purchases
        'Grocery - Supermarkets and Grocery Stores': 3,  # 3% cash back on groceries
        'Dining - Restaurants': 3  # 3% cash back on dining
    },
    point_value=0.01  # Cash back value
)

# Additional U.S. Bank Cards
us_bank_altitude_connect = CreditCard(
    name="U.S. Bank Altitude Connect",
    reward_structure={
        'Travel - Transportation': 4,  # 4x points on travel
        'Dining - Restaurants': 2,  # 2x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

us_bank_flexperks_gold = CreditCard(
    name="U.S. Bank FlexPerks Gold",
    reward_structure={
        'Travel - Transportation': 2,  # 2x points on travel
        'Dining - Restaurants': 2,  # 2x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

# Barclays Additional Cards
barclays_aadvantage_aviator_red = CreditCard(
    name="Barclays AAdvantage Aviator Red",
    reward_structure={
        'Travel - Airlines': 2,  # 2x miles on American Airlines purchases
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

barclays_wyndham_rewards_earner = CreditCard(
    name="Barclays Wyndham Rewards Earner",
    reward_structure={
        'Travel - Lodging': 3,  # 3x points on Wyndham hotel stays
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

# Other Bank and Specialized Cards
synchrony_amazon_prime_store_card = CreditCard(
    name="Synchrony Amazon Prime Store Card",
    reward_structure={
        'Retail - Miscellaneous': 5,  # 5% back on Amazon.com purchases for Prime members
        'default': 1  # 1% on other purchases
    },
    point_value=0.01  # Cash back value
)

pnc_cash_rewards = CreditCard(
    name="PNC Cash Rewards",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

td_bank_cash_credit_card = CreditCard(
    name="TD Bank Cash Credit Card",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

pentagon_federal_platinum_rewards = CreditCard(
    name="Pentagon Federal Credit Union Platinum Rewards",
    reward_structure={
        'default': 1.5,  # 1.5 points on all purchases
        'Travel - Transportation': 2  # 2x points on travel
    },
    point_value=0.01  # Points valued at 1 cent each
)

# Additional Credit Card Instances - Part 5

# Chase Remaining Airline and Hotel Cards
chase_southwest_rapid_rewards_plus = CreditCard(
    name="Chase Southwest Rapid Rewards Plus",
    reward_structure={
        'Travel - Airlines': 2,  # 2x points on Southwest purchases
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

chase_united_explorer = CreditCard(
    name="Chase United Explorer",
    reward_structure={
        'Travel - Airlines': 2,  # 2x points on United purchases
        'Dining - Restaurants': 2,  # 2x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

chase_united_quest = CreditCard(
    name="Chase United Quest",
    reward_structure={
        'Travel - Airlines': 3,  # 3x points on United purchases
        'Dining - Restaurants': 2,  # 2x points on dining
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

# American Express Remaining Travel and Airline Cards
amex_delta_skymiles_blue = CreditCard(
    name="American Express Delta SkyMiles Blue",
    reward_structure={
        'Travel - Airlines': 2,  # 2x miles on Delta purchases
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

amex_delta_skymiles_gold = CreditCard(
    name="American Express Delta SkyMiles Gold",
    reward_structure={
        'Travel - Airlines': 2,  # 2x miles on Delta purchases
        'Restaurants': 2,  # 2x miles on dining
        'default': 1  # 1x miles on everything else
    },
    point_value=0.01  # Miles valued at 1 cent each
)

# Remaining Bank of America and Regional Cards
bank_of_america_royal_caribbean = CreditCard(
    name="Bank of America Royal Caribbean",
    reward_structure={
        'Travel - Transportation': 2,  # 2x points on cruise purchases
        'default': 1  # 1x points on everything else
    },
    point_value=0.01  # Points valued at 1 cent each
)

bank_of_america_world_wildlife_fund = CreditCard(
    name="Bank of America World Wildlife Fund",
    reward_structure={
        'default': 1.5  # 1.5% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)

# Additional Specialized and Retail Cards
comenity_wayfair_credit_card = CreditCard(
    name="Comenity Wayfair Credit Card",
    reward_structure={
        'Retail - Miscellaneous': 5,  # 5% back on Wayfair purchases
        'default': 1  # 1% back on other purchases
    },
    point_value=0.01  # Cash back value
)

usaa_rewards_american_express = CreditCard(
    name="USAA Rewards American Express",
    reward_structure={
        'default': 1.25  # 1.25x points on all purchases
    },
    point_value=0.01  # Points valued at 1 cent each
)

pentagon_federal_gold_visa = CreditCard(
    name="Pentagon Federal Credit Union Gold Visa",
    reward_structure={
        'default': 1.5,  # 1.5 points on all purchases
        'Dining - Restaurants': 2  # 2x points on dining
    },
    point_value=0.01  # Points valued at 1 cent each
)

pentagon_federal_power_cash_rewards = CreditCard(
    name="Pentagon Federal Credit Union Power Cash Rewards",
    reward_structure={
        'default': 2  # 2% cash back on all purchases
    },
    point_value=0.01  # Cash back value
)


chase_sapphire_preferred = CreditCard(
    name="Chase Sapphire Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel - Transportation': 0.02,  # 2% on travel and dining
        'Dining - Restaurants': 0.02
    },
    point_value=0.0125  # Ultimate Rewards points worth 1.25 cents each when redeemed for travel
)

chase_sapphire_reserve = CreditCard(
    name="Chase Sapphire Reserve",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel - Transportation': 0.03,  # 3% on travel and dining
        'Dining - Restaurants': 0.03
    },
    point_value=0.015  # Ultimate Rewards points worth 1.5 cents each when redeemed for travel
)

chase_freedom_unlimited = CreditCard(
    name="Chase Freedom Unlimited",
    reward_structure={
        'default': 0.015,  # 1.5% on all purchases
        'Drugstores': 0.03,  # 3% on drugstores and dining
        'Dining - Restaurants': 0.03
    },
    point_value=0.01  # Cash back value
)

chase_freedom_flex = CreditCard(
    name="Chase Freedom Flex",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

# American Express Cards
amex_gold = CreditCard(
    name="American Express Gold Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Restaurants': 0.04,  # 4% on restaurants
        'U.S. Supermarkets': 0.04  # 4% at U.S. supermarkets
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_platinum = CreditCard(
    name="American Express Platinum Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Flights': 0.05,  # 5% on flights
        'Hotels': 0.05  # 5% on hotels
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_blue_cash_preferred = CreditCard(
    name="American Express Blue Cash Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'U.S. Supermarkets': 0.06  # 6% at U.S. supermarkets
    },
    point_value=0.01  # Cash back value
)

# Discover Cards
discover_it_cashback = CreditCard(
    name="Discover it Cash Back",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

# Capital One Cards
capital_one_venture = CreditCard(
    name="Capital One Venture",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'All Purchases': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Miles worth 1 cent each
)

capital_one_quicksilver = CreditCard(
    name="Capital One Quicksilver",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

# Citi Cards
citi_double_cash = CreditCard(
    name="Citi Double Cash",
    reward_structure={
        'default': 0.02  # 2% on all purchases (1% when you buy, 1% when you pay)
    },
    point_value=0.01  # Cash back value
)

# Bank of America Cards
bofa_cash_rewards = CreditCard(
    name="Bank of America Cash Rewards",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Choice Category': 0.03  # 3% on a choice category
    },
    point_value=0.01  # Cash back value
)

chase_sapphire_preferred = CreditCard(
    name="Chase Sapphire Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel - Transportation': 0.02,  # 2% on travel and dining
        'Dining - Restaurants': 0.02
    },
    point_value=0.0125  # Ultimate Rewards points worth 1.25 cents each when redeemed for travel
)

chase_sapphire_reserve = CreditCard(
    name="Chase Sapphire Reserve",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel - Transportation': 0.03,  # 3% on travel and dining
        'Dining - Restaurants': 0.03
    },
    point_value=0.015  # Ultimate Rewards points worth 1.5 cents each when redeemed for travel
)

chase_freedom_unlimited = CreditCard(
    name="Chase Freedom Unlimited",
    reward_structure={
        'default': 0.015,  # 1.5% on all purchases
        'Drugstores': 0.03,  # 3% on drugstores and dining
        'Dining - Restaurants': 0.03
    },
    point_value=0.01  # Cash back value
)

chase_freedom_flex = CreditCard(
    name="Chase Freedom Flex",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

chase_ink_business_preferred = CreditCard(
    name="Chase Ink Business Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel': 0.03,  # 3% on travel, shipping, advertising, internet
        'Shipping': 0.03,
        'Advertising': 0.03,
        'Internet': 0.03
    },
    point_value=0.0125  # Ultimate Rewards points worth 1.25 cents each when redeemed for travel
)

chase_ink_business_cash = CreditCard(
    name="Chase Ink Business Cash",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Office Supply Stores': 0.05,  # 5% on office supply stores and internet
        'Internet': 0.05
    },
    point_value=0.01  # Cash back value
)

chase_ink_business_unlimited = CreditCard(
    name="Chase Ink Business Unlimited",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

chase_freedom_student = CreditCard(
    name="Chase Freedom Student",
    reward_structure={
        'default': 0.01  # 1% on all purchases
    },
    point_value=0.01  # Cash back value
)

chase_world_of_hyatt = CreditCard(
    name="Chase World of Hyatt",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hyatt Purchases': 0.04  # 4% on Hyatt purchases
    },
    point_value=0.01  # Hyatt points value
)

chase_ihg_rewards_premier = CreditCard(
    name="Chase IHG Rewards Premier",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'IHG Purchases': 0.10  # 10% on IHG purchases
    },
    point_value=0.01  # IHG points value
)

chase_ihg_rewards_traveler = CreditCard(
    name="Chase IHG Rewards Traveler",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'IHG Purchases': 0.05  # 5% on IHG purchases
    },
    point_value=0.01  # IHG points value
)

chase_marriott_bonvoy_boundless = CreditCard(
    name="Chase Marriott Bonvoy Boundless",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Marriott Purchases': 0.06  # 6% on Marriott purchases
    },
    point_value=0.01  # Marriott points value
)

chase_marriott_bonvoy_bold = CreditCard(
    name="Chase Marriott Bonvoy Bold",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Marriott Purchases': 0.03  # 3% on Marriott purchases
    },
    point_value=0.01  # Marriott points value
)

chase_southwest_rapid_rewards_plus = CreditCard(
    name="Chase Southwest Rapid Rewards Plus",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Southwest Purchases': 0.02  # 2% on Southwest purchases
    },
    point_value=0.01  # Southwest points value
)

chase_southwest_rapid_rewards_premier = CreditCard(
    name="Chase Southwest Rapid Rewards Premier",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Southwest Purchases': 0.03  # 3% on Southwest purchases
    },
    point_value=0.01  # Southwest points value
)

chase_southwest_rapid_rewards_priority = CreditCard(
    name="Chase Southwest Rapid Rewards Priority",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Southwest Purchases': 0.03  # 3% on Southwest purchases
    },
    point_value=0.01  # Southwest points value
)

chase_united_explorer = CreditCard(
    name="Chase United Explorer",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.02,  # 2% on United purchases
        'Restaurants': 0.02,
        'Hotels': 0.02
    },
    point_value=0.01  # United miles value
)

chase_united_quest = CreditCard(
    name="Chase United Quest",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.03  # 3% on United purchases
    },
    point_value=0.01  # United miles value
)

chase_united_club_infinite = CreditCard(
    name="Chase United Club Infinite",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.04  # 4% on United purchases
    },
    point_value=0.01  # United miles value
)

chase_united_gateway = CreditCard(
    name="Chase United Gateway",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.02  # 2% on United purchases
    },
    point_value=0.01  # United miles value
)

chase_british_airways_visa = CreditCard(
    name="Chase British Airways Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'British Airways Purchases': 0.03  # 3% on British Airways purchases
    },
    point_value=0.01  # Avios points value
)

chase_aer_lingus_visa_signature = CreditCard(
    name="Chase Aer Lingus Visa Signature",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Aer Lingus Purchases': 0.03  # 3% on Aer Lingus purchases
    },
    point_value=0.01  # Avios points value
)

chase_iberia_visa_signature = CreditCard(
    name="Chase Iberia Visa Signature",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Iberia Purchases': 0.03  # 3% on Iberia purchases
    },
    point_value=0.01  # Avios points value
)

chase_disney_visa = CreditCard(
    name="Chase Disney Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Disney Purchases': 0.02  # 2% on Disney purchases
    },
    point_value=0.01  # Disney rewards dollars value
)

chase_disney_premier_visa = CreditCard(
    name="Chase Disney Premier Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Disney Purchases': 0.02  # 2% on Disney purchases
    },
    point_value=0.01  # Disney rewards dollars value
)

chase_amazon_prime_rewards_visa = CreditCard(
    name="Chase Amazon Prime Rewards Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Amazon.com': 0.05,  # 5% on Amazon.com and Whole Foods
        'Whole Foods': 0.05
    },
    point_value=0.01  # Cash back value
)

chase_starbucks_rewards_visa = CreditCard(
    name="Chase Starbucks Rewards Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Starbucks Purchases': 0.03  # 3% on Starbucks purchases
    },
    point_value=0.01  # Starbucks stars value
)

chase_aarp_credit_card = CreditCard(
    name="Chase AARP Credit Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.03,  # 3% on gas and restaurants
        'Dining - Restaurants': 0.03
    },
    point_value=0.01  # Cash back value
)

class CreditCard:
    def __init__(self, name, reward_structure, point_value):
        self.name = name
        self.reward_structure = reward_structure
        self.point_value = point_value

# Chase Cards
chase_sapphire_preferred = CreditCard(
    name="Chase Sapphire Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel - Transportation': 0.02,  # 2% on travel and dining
        'Dining - Restaurants': 0.02
    },
    point_value=0.0125  # Ultimate Rewards points worth 1.25 cents each when redeemed for travel
)

chase_sapphire_reserve = CreditCard(
    name="Chase Sapphire Reserve",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel - Transportation': 0.03,  # 3% on travel and dining
        'Dining - Restaurants': 0.03
    },
    point_value=0.015  # Ultimate Rewards points worth 1.5 cents each when redeemed for travel
)

chase_freedom_unlimited = CreditCard(
    name="Chase Freedom Unlimited",
    reward_structure={
        'default': 0.015,  # 1.5% on all purchases
        'Drugstores': 0.03,  # 3% on drugstores and dining
        'Dining - Restaurants': 0.03
    },
    point_value=0.01  # Cash back value
)

chase_freedom_flex = CreditCard(
    name="Chase Freedom Flex",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

chase_ink_business_preferred = CreditCard(
    name="Chase Ink Business Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel': 0.03,  # 3% on travel, shipping, advertising, internet
        'Shipping': 0.03,
        'Advertising': 0.03,
        'Internet': 0.03
    },
    point_value=0.0125  # Ultimate Rewards points worth 1.25 cents each when redeemed for travel
)

chase_ink_business_cash = CreditCard(
    name="Chase Ink Business Cash",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Office Supply Stores': 0.05,  # 5% on office supply stores and internet
        'Internet': 0.05
    },
    point_value=0.01  # Cash back value
)

chase_ink_business_unlimited = CreditCard(
    name="Chase Ink Business Unlimited",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

chase_freedom_student = CreditCard(
    name="Chase Freedom Student",
    reward_structure={
        'default': 0.01  # 1% on all purchases
    },
    point_value=0.01  # Cash back value
)

chase_world_of_hyatt = CreditCard(
    name="Chase World of Hyatt",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hyatt Purchases': 0.04  # 4% on Hyatt purchases
    },
    point_value=0.01  # Hyatt points value
)

chase_ihg_rewards_premier = CreditCard(
    name="Chase IHG Rewards Premier",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'IHG Purchases': 0.10  # 10% on IHG purchases
    },
    point_value=0.01  # IHG points value
)

chase_ihg_rewards_traveler = CreditCard(
    name="Chase IHG Rewards Traveler",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'IHG Purchases': 0.05  # 5% on IHG purchases
    },
    point_value=0.01  # IHG points value
)

chase_marriott_bonvoy_boundless = CreditCard(
    name="Chase Marriott Bonvoy Boundless",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Marriott Purchases': 0.06  # 6% on Marriott purchases
    },
    point_value=0.01  # Marriott points value
)

chase_marriott_bonvoy_bold = CreditCard(
    name="Chase Marriott Bonvoy Bold",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Marriott Purchases': 0.03  # 3% on Marriott purchases
    },
    point_value=0.01  # Marriott points value
)

chase_southwest_rapid_rewards_plus = CreditCard(
    name="Chase Southwest Rapid Rewards Plus",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Southwest Purchases': 0.02  # 2% on Southwest purchases
    },
    point_value=0.01  # Southwest points value
)

chase_southwest_rapid_rewards_premier = CreditCard(
    name="Chase Southwest Rapid Rewards Premier",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Southwest Purchases': 0.03  # 3% on Southwest purchases
    },
    point_value=0.01  # Southwest points value
)

chase_southwest_rapid_rewards_priority = CreditCard(
    name="Chase Southwest Rapid Rewards Priority",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Southwest Purchases': 0.03  # 3% on Southwest purchases
    },
    point_value=0.01  # Southwest points value
)

chase_united_explorer = CreditCard(
    name="Chase United Explorer",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.02,  # 2% on United purchases
        'Restaurants': 0.02,
        'Hotels': 0.02
    },
    point_value=0.01  # United miles value
)

chase_united_quest = CreditCard(
    name="Chase United Quest",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.03  # 3% on United purchases
    },
    point_value=0.01  # United miles value
)

chase_united_club_infinite = CreditCard(
    name="Chase United Club Infinite",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.04  # 4% on United purchases
    },
    point_value=0.01  # United miles value
)

chase_united_gateway = CreditCard(
    name="Chase United Gateway",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'United Purchases': 0.02  # 2% on United purchases
    },
    point_value=0.01  # United miles value
)

chase_british_airways_visa = CreditCard(
    name="Chase British Airways Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'British Airways Purchases': 0.03  # 3% on British Airways purchases
    },
    point_value=0.01  # Avios points value
)

chase_aer_lingus_visa_signature = CreditCard(
    name="Chase Aer Lingus Visa Signature",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Aer Lingus Purchases': 0.03  # 3% on Aer Lingus purchases
    },
    point_value=0.01  # Avios points value
)

chase_iberia_visa_signature = CreditCard(
    name="Chase Iberia Visa Signature",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Iberia Purchases': 0.03  # 3% on Iberia purchases
    },
    point_value=0.01  # Avios points value
)

chase_disney_visa = CreditCard(
    name="Chase Disney Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Disney Purchases': 0.02  # 2% on Disney purchases
    },
    point_value=0.01  # Disney rewards dollars value
)

chase_disney_premier_visa = CreditCard(
    name="Chase Disney Premier Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Disney Purchases': 0.02  # 2% on Disney purchases
    },
    point_value=0.01  # Disney rewards dollars value
)

chase_amazon_prime_rewards_visa = CreditCard(
    name="Chase Amazon Prime Rewards Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Amazon.com': 0.05,  # 5% on Amazon.com and Whole Foods
        'Whole Foods': 0.05
    },
    point_value=0.01  # Cash back value
)

chase_starbucks_rewards_visa = CreditCard(
    name="Chase Starbucks Rewards Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Starbucks Purchases': 0.03  # 3% on Starbucks purchases
    },
    point_value=0.01  # Starbucks stars value
)

chase_aarp_credit_card = CreditCard(
    name="Chase AARP Credit Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.03,  # 3% on gas and restaurants
        'Dining - Restaurants': 0.03
    },
    point_value=0.01  # Cash back value
)

# Continuing Credit Card Instances

# American Express Cards
amex_gold = CreditCard(
    name="American Express Gold Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Restaurants': 0.04,  # 4% on restaurants
        'U.S. Supermarkets': 0.04  # 4% at U.S. supermarkets
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_platinum = CreditCard(
    name="American Express Platinum Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Flights': 0.05,  # 5% on flights
        'Hotels': 0.05  # 5% on hotels
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_green = CreditCard(
    name="American Express Green Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel': 0.03,  # 3% on travel
        'Dining': 0.03  # 3% on dining
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_blue_cash_preferred = CreditCard(
    name="American Express Blue Cash Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'U.S. Supermarkets': 0.06  # 6% at U.S. supermarkets
    },
    point_value=0.01  # Cash back value
)

amex_blue_cash_everyday = CreditCard(
    name="American Express Blue Cash Everyday",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'U.S. Supermarkets': 0.03  # 3% at U.S. supermarkets
    },
    point_value=0.01  # Cash back value
)

amex_everyday = CreditCard(
    name="American Express Everyday",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'U.S. Supermarkets': 0.02  # 2% at U.S. supermarkets
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_everyday_preferred = CreditCard(
    name="American Express Everyday Preferred",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'U.S. Supermarkets': 0.03  # 3% at U.S. supermarkets
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_cash_magnet = CreditCard(
    name="American Express Cash Magnet",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

amex_business_gold = CreditCard(
    name="American Express Business Gold",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Top 2 Business Categories': 0.04  # 4% on top 2 business spending categories
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_business_platinum = CreditCard(
    name="American Express Business Platinum",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Purchases over $5000': 0.015  # 1.5% on purchases over $5000
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_blue_business_plus = CreditCard(
    name="American Express Blue Business Plus",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'First $50000 Spent Annually': 0.02  # 2% on first $50000 spent annually
    },
    point_value=0.01  # Membership Rewards points worth 1 cent each
)

amex_business_cash = CreditCard(
    name="American Express Business Cash",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Office Supplies': 0.02,  # 2% on office supplies and internet
        'Internet': 0.02
    },
    point_value=0.01  # Cash back value
)

# Hilton Honors Cards
amex_hilton_honors = CreditCard(
    name="American Express Hilton Honors",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hilton Purchases': 0.07  # 7% on Hilton purchases
    },
    point_value=0.01  # Hilton points value
)

amex_hilton_honors_surpass = CreditCard(
    name="American Express Hilton Honors Surpass",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hilton Purchases': 0.12  # 12% on Hilton purchases
    },
    point_value=0.01  # Hilton points value
)

amex_hilton_honors_aspire = CreditCard(
    name="American Express Hilton Honors Aspire",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hilton Purchases': 0.14  # 14% on Hilton purchases
    },
    point_value=0.01  # Hilton points value
)

amex_hilton_honors_business = CreditCard(
    name="American Express Hilton Honors Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hilton Purchases': 0.12  # 12% on Hilton purchases
    },
    point_value=0.01  # Hilton points value
)

# Marriott Bonvoy Cards
amex_marriott_bonvoy_brilliant = CreditCard(
    name="American Express Marriott Bonvoy Brilliant",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Marriott Purchases': 0.06  # 6% on Marriott purchases
    },
    point_value=0.01  # Marriott points value
)

amex_marriott_bonvoy_business = CreditCard(
    name="American Express Marriott Bonvoy Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Marriott Purchases': 0.06  # 6% on Marriott purchases
    },
    point_value=0.01  # Marriott points value
)

# Delta SkyMiles Cards
amex_delta_skymiles_blue = CreditCard(
    name="American Express Delta SkyMiles Blue",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.02  # 2% on Delta purchases
    },
    point_value=0.01  # Delta miles value
)

amex_delta_skymiles_gold = CreditCard(
    name="American Express Delta SkyMiles Gold",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.02,  # 2% on Delta purchases
        'Restaurants': 0.02,
        'Supermarkets': 0.02
    },
    point_value=0.01  # Delta miles value
)

amex_delta_skymiles_platinum = CreditCard(
    name="American Express Delta SkyMiles Platinum",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.03  # 3% on Delta purchases
    },
    point_value=0.01  # Delta miles value
)

amex_delta_skymiles_reserve = CreditCard(
    name="American Express Delta SkyMiles Reserve",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.03  # 3% on Delta purchases
    },
    point_value=0.01  # Delta miles value
)

# Business Delta SkyMiles Cards
amex_delta_skymiles_gold_business = CreditCard(
    name="American Express Delta SkyMiles Gold Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.02  # 2% on Delta purchases
    },
    point_value=0.01  # Delta miles value
)

amex_delta_skymiles_platinum_business = CreditCard(
    name="American Express Delta SkyMiles Platinum Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.03  # 3% on Delta purchases
    },
    point_value=0.01  # Delta miles value
)

amex_delta_skymiles_reserve_business = CreditCard(
    name="American Express Delta SkyMiles Reserve Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Delta Purchases': 0.03  # 3% on Delta purchases
    },
    point_value=0.01  # Delta miles value
)

amex_amazon_business_prime = CreditCard(
    name="American Express Amazon Business Prime",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Amazon Business Purchases': 0.05  # 5% on Amazon Business purchases
    },
    point_value=0.01  # Cash back value
)

# Discover Cards
discover_it_cashback = CreditCard(
    name="Discover it Cash Back",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

discover_it_miles = CreditCard(
    name="Discover it Miles",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Miles value
)

discover_it_chrome = CreditCard(
    name="Discover it Chrome",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas Stations': 0.02,  # 2% on gas stations and restaurants
        'Restaurants': 0.02
    },
    point_value=0.01  # Cash back value
)

discover_it_student_cashback = CreditCard(
    name="Discover it Student Cash Back",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

discover_it_student_chrome = CreditCard(
    name="Discover it Student Chrome",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas Stations': 0.02,  # 2% on gas stations and restaurants
        'Restaurants': 0.02
    },
    point_value=0.01  # Cash back value
)

discover_it_secured = CreditCard(
    name="Discover it Secured",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas Stations': 0.02,  # 2% on gas stations and restaurants
        'Restaurants': 0.02
    },
    point_value=0.01  # Cash back value
)

discover_it_business = CreditCard(
    name="Discover it Business",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

discover_it_nhl = CreditCard(
    name="Discover it NHL",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Quarterly Rotating Categories': 0.05  # 5% on quarterly rotating categories
    },
    point_value=0.01  # Cash back value
)

# Capital One Cards
capital_one_venture = CreditCard(
    name="Capital One Venture",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'All Purchases': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Miles value
)

capital_one_venture_x = CreditCard(
    name="Capital One Venture X",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Hotels': 0.10,  # 10% on hotels and rental cars
        'Rental Cars': 0.10
    },
    point_value=0.01  # Miles value
)

capital_one_ventureone = CreditCard(
    name="Capital One VentureOne",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'All Purchases': 0.0125  # 1.25% on all purchases
    },
    point_value=0.01  # Miles value
)

capital_one_quicksilver = CreditCard(
    name="Capital One Quicksilver",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

capital_one_savor = CreditCard(
    name="Capital One Savor",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Dining and Entertainment': 0.04  # 4% on dining and entertainment
    },
    point_value=0.01  # Cash back value
)

capital_one_savorone = CreditCard(
    name="Capital One SavorOne",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Dining': 0.03,  # 3% on dining, entertainment, and groceries
        'Entertainment': 0.03,
        'Groceries': 0.03
    },
    point_value=0.01  # Cash back value
)

# Continuing Capital One Cards
capital_one_spark_cash_select = CreditCard(
    name="Capital One Spark Cash Select",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

capital_one_spark_miles = CreditCard(
    name="Capital One Spark Miles",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'All Purchases': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Miles value
)

capital_one_spark_miles_select = CreditCard(
    name="Capital One Spark Miles Select",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'All Purchases': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Miles value
)

capital_one_savorone_student = CreditCard(
    name="Capital One SavorOne Student",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Dining': 0.03,  # 3% on dining, entertainment, and groceries
        'Entertainment': 0.03,
        'Groceries': 0.03
    },
    point_value=0.01  # Cash back value
)

capital_one_quicksilver_student = CreditCard(
    name="Capital One Quicksilver Student",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

# Citi Cards
citi_double_cash = CreditCard(
    name="Citi Double Cash",
    reward_structure={
        'default': 0.02  # 2% on all purchases (1% when you buy, 1% when you pay)
    },
    point_value=0.01  # Cash back value
)

citi_premier = CreditCard(
    name="Citi Premier",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Restaurants': 0.03,  # 3% on restaurants, supermarkets, gas, air travel, hotels
        'Supermarkets': 0.03,
        'Gas': 0.03,
        'Air Travel': 0.03,
        'Hotels': 0.03
    },
    point_value=0.01  # ThankYou points value
)

citi_prestige = CreditCard(
    name="Citi Prestige",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Restaurants': 0.05,  # 5% on restaurants and air travel
        'Air Travel': 0.05
    },
    point_value=0.01  # ThankYou points value
)

citi_custom_cash = CreditCard(
    name="Citi Custom Cash",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Top Spending Category': 0.05  # 5% on top spending category
    },
    point_value=0.01  # Cash back value
)

citi_rewards_plus = CreditCard(
    name="Citi Rewards+",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Supermarkets': 0.02,  # 2% at supermarkets and gas stations
        'Gas': 0.02
    },
    point_value=0.01  # ThankYou points value
)

citi_aadvantage_platinum_select = CreditCard(
    name="Citi AAdvantage Platinum Select",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'American Airlines Purchases': 0.02  # 2% on American Airlines purchases
    },
    point_value=0.01  # American Airlines miles value
)

citi_aadvantage_executive = CreditCard(
    name="Citi AAdvantage Executive",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'American Airlines Purchases': 0.02  # 2% on American Airlines purchases
    },
    point_value=0.01  # American Airlines miles value
)

citi_aadvantage_mileup = CreditCard(
    name="Citi AAdvantage MileUp",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'American Airlines Purchases': 0.02,  # 2% on American Airlines purchases
        'Groceries': 0.02  # 2% on groceries
    },
    point_value=0.01  # American Airlines miles value
)

citi_aadvantage_business = CreditCard(
    name="Citi AAdvantage Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'American Airlines Purchases': 0.02  # 2% on American Airlines purchases
    },
    point_value=0.01  # American Airlines miles value
)

# Wells Fargo Cards
wells_fargo_active_cash = CreditCard(
    name="Wells Fargo Active Cash",
    reward_structure={
        'default': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Cash back value
)

wells_fargo_autograph = CreditCard(
    name="Wells Fargo Autograph",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Restaurants': 0.03,  # 3% on restaurants, travel, gas, transit, streaming
        'Travel': 0.03,
        'Gas': 0.03,
        'Transit': 0.03,
        'Streaming': 0.03
    },
    point_value=0.01  # Points value
)

wells_fargo_business_platinum = CreditCard(
    name="Wells Fargo Business Platinum",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

wells_fargo_cash_wise = CreditCard(
    name="Wells Fargo Cash Wise",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

wells_fargo_business_elite = CreditCard(
    name="Wells Fargo Business Elite",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

# U.S. Bank Cards
us_bank_altitude_reserve = CreditCard(
    name="U.S. Bank Altitude Reserve",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel': 0.03,  # 3% on travel and mobile wallet purchases
        'Mobile Wallet Purchases': 0.03
    },
    point_value=0.01  # Points value
)

us_bank_altitude_connect = CreditCard(
    name="U.S. Bank Altitude Connect",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Travel': 0.04,  # 4% on travel and gas stations
        'Gas Stations': 0.04
    },
    point_value=0.01  # Points value
)

us_bank_altitude_go = CreditCard(
    name="U.S. Bank Altitude Go",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Restaurants': 0.04  # 4% on restaurants
    },
    point_value=0.01  # Points value
)

us_bank_cash_plus = CreditCard(
    name="U.S. Bank Cash+",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Two Categories of Choice': 0.05  # 5% on two chosen categories
    },
    point_value=0.01  # Cash back value
)

us_bank_triple_cash_rewards_business = CreditCard(
    name="U.S. Bank Triple Cash Rewards Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.03,  # 3% on gas, office supplies, restaurants, cell phone
        'Office Supplies': 0.03,
        'Restaurants': 0.03,
        'Cell Phone': 0.03
    },
    point_value=0.01  # Cash back value
)

us_bank_flexperks_gold = CreditCard(
    name="U.S. Bank FlexPerks Gold",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Airline Purchases': 0.02  # 2% on airline purchases
    },
    point_value=0.01  # FlexPoints value
)

us_bank_korean_air_skypass = CreditCard(
    name="U.S. Bank Korean Air SKYPASS",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Korean Air Purchases': 0.02  # 2% on Korean Air purchases
    },
    point_value=0.01  # SKYPASS miles value
)

us_bank_rei_co_op_mastercard = CreditCard(
    name="U.S. Bank REI Co-op Mastercard",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'REI Purchases': 0.05  # 5% on REI purchases
    },
    point_value=0.01  # REI gift card value
)

# Barclays Cards
barclays_arrival_plus = CreditCard(
    name="Barclays Arrival Plus",
    reward_structure={
        'default': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Miles value
)

barclays_jetblue_plus = CreditCard(
    name="Barclays JetBlue Plus",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'JetBlue Purchases': 0.06  # 6% on JetBlue purchases
    },
    point_value=0.01  # JetBlue points value
)

barclays_jetblue_card = CreditCard(
    name="Barclays JetBlue Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'JetBlue Purchases': 0.03  # 3% on JetBlue purchases
    },
    point_value=0.01  # JetBlue points value
)

barclays_jetblue_business = CreditCard(
    name="Barclays JetBlue Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'JetBlue Purchases': 0.06  # 6% on JetBlue purchases
    },
    point_value=0.01  # JetBlue points value
)

# Barclays Additional Cards
barclays_aadvantage_aviator_red = CreditCard(
    name="Barclays AAdvantage Aviator Red",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'American Airlines Purchases': 0.02  # 2% on American Airlines purchases
    },
    point_value=0.01  # American Airlines miles value
)

barclays_aadvantage_aviator_business = CreditCard(
    name="Barclays AAdvantage Aviator Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'American Airlines Purchases': 0.02  # 2% on American Airlines purchases
    },
    point_value=0.01  # American Airlines miles value
)

barclays_wyndham_rewards_earner = CreditCard(
    name="Barclays Wyndham Rewards Earner",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Wyndham Purchases': 0.05  # 5% on Wyndham purchases
    },
    point_value=0.01  # Wyndham points value
)

barclays_wyndham_rewards_earner_plus = CreditCard(
    name="Barclays Wyndham Rewards Earner Plus",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Wyndham Purchases': 0.06  # 6% on Wyndham purchases
    },
    point_value=0.01  # Wyndham points value
)

barclays_wyndham_rewards_earner_business = CreditCard(
    name="Barclays Wyndham Rewards Earner Business",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Wyndham Purchases': 0.08  # 8% on Wyndham purchases
    },
    point_value=0.01  # Wyndham points value
)

barclays_carnival_world_mastercard = CreditCard(
    name="Barclays Carnival World Mastercard",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Carnival Purchases': 0.02  # 2% on Carnival purchases
    },
    point_value=0.01  # FunPoints value
)

barclays_princess_cruises_rewards = CreditCard(
    name="Barclays Princess Cruises Rewards",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Princess Cruises Purchases': 0.02  # 2% on Princess Cruises purchases
    },
    point_value=0.01  # Princess Points value
)

barclays_holland_america_line_rewards = CreditCard(
    name="Barclays Holland America Line Rewards",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Holland America Purchases': 0.02  # 2% on Holland America purchases
    },
    point_value=0.01  # Mariner Points value
)

barclays_barnes_and_noble_mastercard = CreditCard(
    name="Barclays Barnes & Noble Mastercard",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Barnes & Noble Purchases': 0.05  # 5% on Barnes & Noble purchases
    },
    point_value=0.01  # Barnes & Noble certificate value
)

# Specialty and Store Cards
synchrony_amazon_prime_store_card = CreditCard(
    name="Synchrony Amazon Prime Store Card",
    reward_structure={
        'default': 0.00,  # 0% on other purchases
        'Amazon Purchases': 0.05  # 5% on Amazon purchases
    },
    point_value=0.01  # Amazon gift card value
)

comenity_wayfair_credit_card = CreditCard(
    name="Comenity Wayfair Credit Card",
    reward_structure={
        'default': 0.00,  # 0% on other purchases
        'Wayfair Purchases': 0.05  # 5% on Wayfair purchases
    },
    point_value=0.01  # Wayfair credit value
)

# Additional Bank Cards
pnc_cash_rewards = CreditCard(
    name="PNC Cash Rewards",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.04  # 4% on gas
    },
    point_value=0.01  # Cash back value
)

pnc_points = CreditCard(
    name="PNC Points",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Dining': 0.04  # 4% on dining
    },
    point_value=0.01  # PNC points value
)

pnc_business_cash = CreditCard(
    name="PNC Business Cash",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.02,  # 2% on gas, office supplies, dining
        'Office Supplies': 0.02,
        'Dining': 0.02
    },
    point_value=0.01  # Cash back value
)

# TD Bank and Other Bank Cards
td_bank_cash_credit_card = CreditCard(
    name="TD Bank Cash Credit Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Dining': 0.02,  # 2% on dining and groceries
        'Groceries': 0.02
    },
    point_value=0.01  # Cash back value
)

td_bank_double_up_credit_card = CreditCard(
    name="TD Bank Double Up Credit Card",
    reward_structure={
        'default': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Cash back value
)

hsbc_cash_rewards_mastercard = CreditCard(
    name="HSBC Cash Rewards Mastercard",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

bmo_harris_bank_cash_back_mastercard = CreditCard(
    name="BMO Harris Bank Cash Back Mastercard",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Groceries': 0.03,  # 3% on groceries, gas, dining
        'Gas': 0.03,
        'Dining': 0.03
    },
    point_value=0.01  # Cash back value
)

citizens_bank_cash_back_plus = CreditCard(
    name="Citizens Bank Cash Back Plus",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

fifth_third_bank_cash_back_card = CreditCard(
    name="Fifth Third Bank Cash/Back Card",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

mt_bank_visa_signature = CreditCard(
    name="M&T Bank Visa Signature Credit Card",
    reward_structure={
        'default': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

huntington_voice_credit_card = CreditCard(
    name="Huntington Voice Credit Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Choice Category': 0.03  # 3% on a choice category
    },
    point_value=0.01  # Cash back value
)


# Continuing SunTrust Cash Rewards Credit Card
suntrust_cash_rewards_credit_card = CreditCard(
    name="SunTrust Cash Rewards Credit Card",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.02,  # 2% on gas and groceries
        'Groceries': 0.02
    },
    point_value=0.01  # Cash back value
)

# USAA Rewards Cards
usaa_rewards_visa = CreditCard(
    name="USAA Rewards Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.02,  # 2% on gas and dining
        'Dining': 0.02
    },
    point_value=0.01  # USAA Rewards points value
)

usaa_rewards_american_express = CreditCard(
    name="USAA Rewards American Express",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.02,  # 2% on gas and dining
        'Dining': 0.02
    },
    point_value=0.01  # USAA Rewards points value
)

# Navy Federal Credit Union Cards
navy_federal_cashrewards = CreditCard(
    name="Navy Federal Credit Union cashRewards",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'All Purchases': 0.015  # 1.5% on all purchases
    },
    point_value=0.01  # Cash back value
)

# Pentagon Federal Credit Union Cards
penfed_platinum_rewards = CreditCard(
    name="Pentagon Federal Credit Union Platinum Rewards",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Gas': 0.05  # 5% on gas
    },
    point_value=0.01  # Cash back value
)

penfed_gold_visa = CreditCard(
    name="Pentagon Federal Credit Union Gold Visa",
    reward_structure={
        'default': 0.01,  # 1% on all purchases
        'Groceries': 0.03  # 3% on groceries
    },
    point_value=0.01  # Cash back value
)

penfed_power_cash_rewards = CreditCard(
    name="Pentagon Federal Credit Union Power Cash Rewards",
    reward_structure={
        'default': 0.015,  # 1.5% on all purchases
        'All Purchases': 0.02  # 2% on all purchases
    },
    point_value=0.01  # Cash back value
)