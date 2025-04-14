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
        # Default reward rate (usually 1% or 1x)
        reward_rate = self.reward_structure.get('default', 0.01)
        
        # Check if this MCC has a special reward rate
        if mcc in self.reward_structure:
            reward_rate = self.reward_structure[mcc]
        else:
            # Check for category matches (dining, travel, etc.)
            for category, rate in self.reward_structure.items():
                if isinstance(category, str) and category != 'default':
                    if self._is_mcc_in_category(mcc, category):
                        reward_rate = rate
                        break
        
        # Calculate reward value (points or cash back)
        reward_points = amount * reward_rate
        
        # Convert to dollar value
        reward_value = reward_points * self.point_value
        
        return reward_value
    
    def _is_mcc_in_category(self, mcc, category):
        """
        Check if an MCC code belongs to a reward category.
        
        Parameters:
        mcc (int or str): Merchant Category Code
        category (str): Category name (e.g., 'dining', 'travel')
        
        Returns:
        bool: True if the MCC belongs to the category
        """
        # This would contain your mapping of categories to MCC codes
        category_to_mcc = {
            'dining': [5812, 5813, 5814],
            'grocery': [5411, 5422, 5441, 5451, 5462, 5499],
            'travel': list(range(3000, 4000)) + [4511, 4722],
            'gas': [5541, 5542, 5983],
            'entertainment': [7832, 7922, 7929, 7941, 7991, 7994, 7996, 7999],
            'drugstore': [5912],
            # Add more categories as needed
        }
        
        if category in category_to_mcc:
            if isinstance(mcc, str):
                mcc = int(mcc)
            return mcc in category_to_mcc[category]
        return False


# Example usage:
# Create some credit cards with their reward structures
amex_gold = CreditCard(
    name="Amex Gold",
    reward_structure={
        'dining': 4,  # 4x points on dining
        'grocery': 4,  # 4x points on groceries
        'travel': 3,   # 3x points on flights
        'default': 1   # 1x points on everything else
    },
    point_value=0.02  # Amex points valued at 2 cents each
)

chase_sapphire = CreditCard(
    name="Chase Sapphire Preferred",
    reward_structure={
        'dining': 3,
        'streaming': 3,
        'grocery': 3,
        'travel': 2,
        'default': 1
    },
    point_value=0.0125  # Chase points valued at 1.25 cents each
)

citi_double_cash = CreditCard(
    name="Citi Double Cash",
    reward_structure={
        'default': 0.02  # 2% cash back on everything
    }
)







def calculate_best_card(transaction):
    best_reward = 0
    best_card = None
    
    # Iterate through all cards in your database
    for card in card_database:
        # Calculate reward based on transaction amount, MCC, etc.
        reward = card.calculate_reward(transaction['Amount'], transaction['MCC'])
        
        # Compare to current best
        if reward > best_reward:
            best_reward = reward
            best_card = card.name
            
    return best_card, best_reward










# Apply to your entire dataset
df['Best_Card'] = df.apply(calculate_best_card, axis=1)

# Create a database of cards
card_database = [amex_gold, chase_sapphire, citi_double_cash]