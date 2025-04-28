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


########################################################################################################################################################################################

mcc_specific = {
    # Airlines (specific airline codes in 3000-3299 range)
    3000: "Travel - Airlines - United Airlines",
    3001: "Travel - Airlines - American Airlines",
    3002: "Travel - Airlines - Pan American",
    3003: "Travel - Airlines - Eurofly",
    3004: "Travel - Airlines - Dragonfair",
    3005: "Travel - Airlines - British Airways",
    3006: "Travel - Airlines - Japan Airlines",
    3007: "Travel - Airlines - Air France",
    3008: "Travel - Airlines - Lufthansa",
    3009: "Travel - Airlines - Air Canada",
    3010: "Travel - Airlines - KLM Royal Dutch Airlines",
    3011: "Travel - Airlines - Aeroflot",
    3012: "Travel - Airlines - Qantas",
    3013: "Travel - Airlines - Alitalia",
    3014: "Travel - Airlines - Saudi Arabian Airlines",
    3015: "Travel - Airlines - Swiss International",
    3016: "Travel - Airlines - SAS",
    3017: "Travel - Airlines - South African Airways",
    3018: "Travel - Airlines - Varig",
    3020: "Travel - Airlines - Air India",
    3025: "Travel - Airlines - Air Berlin",
    3026: "Travel - Airlines - Emirates Airlines",
    3035: "Travel - Airlines - Etihad Airways",
    3058: "Travel - Airlines - Delta",
    3066: "Travel - Airlines - Southwest Airlines",
    3131: "Travel - Airlines - Frontier Airlines",
    3143: "Travel - Airlines - Spirit Airlines",
    3144: "Travel - Airlines - Virgin Atlantic Airways",
    3245: "Travel - Airlines - Singapore Airlines",
    3246: "Travel - Airlines - Qatar Airways",
    3247: "Travel - Airlines - Turkish Airlines",
    3248: "Travel - Airlines - WestJet Airlines",
    3299: "Travel - Airlines - Other",
    
    # Car Rental (specific rental agencies in 3300-3499 range)
    3300: "Travel - Car Rental - Budget Rent-A-Car",
    3351: "Travel - Car Rental - Hertz",
    3352: "Travel - Car Rental - Dollar Rent-A-Car",
    3353: "Travel - Car Rental - National Car Rental",
    3354: "Travel - Car Rental - Avis Rent-A-Car",
    3355: "Travel - Car Rental - Enterprise Rent-A-Car",
    3357: "Travel - Car Rental - Alamo Rent-A-Car",
    3395: "Travel - Car Rental - Thrifty Car Rental",
    3405: "Travel - Car Rental - Enterprise Rent-A-Car",
    3434: "Travel - Car Rental - Payless Car Rental",
    3441: "Travel - Car Rental - Sixt Car Rental",
    3499: "Travel - Car Rental - Other",
    
    # Hotels & Lodging (specific hotels in 3500-3999 range)
    3501: "Travel - Lodging - Holiday Inn",
    3502: "Travel - Lodging - Best Western",
    3503: "Travel - Lodging - Sheraton",
    3504: "Travel - Lodging - Hilton",
    3505: "Travel - Lodging - Hyatt Hotels",
    3506: "Travel - Lodging - Intercontinental Hotels",
    3507: "Travel - Lodging - Westin",
    3508: "Travel - Lodging - Marriott",
    3509: "Travel - Lodging - Four Seasons",
    3510: "Travel - Lodging - Days Inn",
    3512: "Travel - Lodging - La Quinta Inns",
    3515: "Travel - Lodging - Courtyard by Marriott",
    3521: "Travel - Lodging - DoubleTree Hotel",
    3535: "Travel - Lodging - Hilton International",
    3536: "Travel - Lodging - Radisson Hotels",
    3542: "Travel - Lodging - Ritz-Carlton",
    3543: "Travel - Lodging - Hampton Inns",
    3546: "Travel - Lodging - Homewood Suites",
    3550: "Travel - Lodging - Embassy Suites",
    3559: "Travel - Lodging - W Hotels",
    3560: "Travel - Lodging - Waldorf Astoria",
    3561: "Travel - Lodging - Comfort Inn",
    3562: "Travel - Lodging - Quality Inn",
    3563: "Travel - Lodging - Sleep Inn & Suites",
    3564: "Travel - Lodging - Clarion Hotels",
    3565: "Travel - Lodging - Cambria Suites",
    3566: "Travel - Lodging - Ascend Collection Hotels",
    3572: "Travel - Lodging - Fairfield Inn",
    3573: "Travel - Lodging - TownePlace Suites",
    3574: "Travel - Lodging - SpringHill Suites",
    3575: "Travel - Lodging - Residence Inn",
    3579: "Travel - Lodging - Extended Stay America",
    3581: "Travel - Lodging - Candlewood Suites",
    3582: "Travel - Lodging - Staybridge Suites",
    3583: "Travel - Lodging - Holiday Inn Express",
    3584: "Travel - Lodging - Crowne Plaza Hotels",
    3585: "Travel - Lodging - Hotel Indigo",
    3586: "Travel - Lodging - Wyndham Hotels",
    3587: "Travel - Lodging - Super 8 Motels",
    3588: "Travel - Lodging - Howard Johnson",
    3589: "Travel - Lodging - Travelodge",
    3590: "Travel - Lodging - Fairmont Hotels",
    3591: "Travel - Lodging - Knights Inn",
    3592: "Travel - Lodging - Ramada Inns",
    3600: "Travel - Lodging - Motel 6",
    3615: "Travel - Lodging - Studio 6",
    3620: "Travel - Lodging - Ace Hotel",
    3625: "Travel - Lodging - Aloft Hotels",
    3629: "Travel - Lodging - Kimpton Hotels",
    3635: "Travel - Lodging - Grand Hyatt",
    3640: "Travel - Lodging - Park Hyatt",
    3641: "Travel - Lodging - Hyatt Place",
    3645: "Travel - Lodging - Hyatt Regency",
    3649: "Travel - Lodging - Andaz Hotels",
    3650: "Travel - Lodging - Hyatt House",
    3660: "Travel - Lodging - Omni Hotels",
    3665: "Travel - Lodging - The Peninsula Hotels",
    3670: "Travel - Lodging - Red Roof Inns",
    3675: "Travel - Lodging - Microtel Inns & Suites",
    3680: "Travel - Lodging - Renaissance Hotels",
    3681: "Travel - Lodging - JW Marriott",
    3685: "Travel - Lodging - Autograph Collection Hotels",
    3690: "Travel - Lodging - Millennium Hotels",
    3695: "Travel - Lodging - Element Hotels",
    3700: "Travel - Lodging - Starwood Hotels",
    3705: "Travel - Lodging - Le Meridien",
    3715: "Travel - Lodging - St. Regis",
    3734: "Travel - Lodging - Hard Rock Hotels",
    3738: "Travel - Lodging - MGM Resorts Properties",
    3739: "Travel - Lodging - Bellagio",
    3740: "Travel - Lodging - Aria",
    3741: "Travel - Lodging - Vdara",
    3742: "Travel - Lodging - Mandalay Bay",
    3743: "Travel - Lodging - THEhotel",
    3744: "Travel - Lodging - Delano",
    3745: "Travel - Lodging - Luxor",
    3746: "Travel - Lodging - Excalibur",
    3747: "Travel - Lodging - New York New York",
    3748: "Travel - Lodging - Monte Carlo",
    3749: "Travel - Lodging - MGM Grand",
    3770: "Travel - Lodging - Caesars Properties",
    3780: "Travel - Lodging - Harrah's",
    3781: "Travel - Lodging - Flamingo",
    3782: "Travel - Lodging - Bally's",
    3783: "Travel - Lodging - Paris Las Vegas",
    3784: "Travel - Lodging - Rio",
    3785: "Travel - Lodging - Planet Hollywood",
    3786: "Travel - Lodging - Caesars Palace",
    3790: "Travel - Lodging - The Cromwell",
    3795: "Travel - Lodging - The LINQ",
    3800: "Travel - Lodging - Wynn Las Vegas",
    3801: "Travel - Lodging - Encore",
    3802: "Travel - Lodging - Venetian Resort",
    3803: "Travel - Lodging - Palazzo Resort",
    3805: "Travel - Lodging - The Cosmopolitan",
    3815: "Travel - Lodging - Nobu Hotels",
    3825: "Travel - Lodging - Four Points by Sheraton",
    3850: "Travel - Lodging - Mandarin Oriental",
    3855: "Travel - Lodging - Disney Resorts",
    3865: "Travel - Lodging - Mlife Resorts",
    3866: "Travel - Lodging - AC Hotels by Marriott",
    3870: "Travel - Lodging - Moxy Hotels",
    3880: "Travel - Lodging - EDITION Hotels",
    3885: "Travel - Lodging - Design Hotels",
    3890: "Travel - Lodging - Tribute Portfolio Hotels",
    3900: "Travel - Lodging - Waldorf Astoria Hotels & Resorts",
    3912: "Travel - Lodging - Curio Collection Hotels",
    3920: "Travel - Lodging - Canopy by Hilton",
    3935: "Travel - Lodging - Tapestry Collection by Hilton",
    3940: "Travel - Lodging - Tru by Hilton",
    3941: "Travel - Lodging - Home2 Suites by Hilton",
    3950: "Travel - Lodging - Hilton Garden Inn",
    3955: "Travel - Lodging - Conrad Hotels",
    3999: "Travel - Lodging - Other",
    
    # Transportation Services (4000-4799)
    4011: "Travel - Transportation - Railroads",
    4111: "Travel - Transportation - Local/Suburban Commuter",
    4112: "Travel - Transportation - Passenger Railways",
    4119: "Travel - Transportation - Ambulance Services",
    4121: "Travel - Transportation - Taxicabs and Limousines",
    4131: "Travel - Transportation - Bus Lines",
    4214: "Travel - Transportation - Motor Freight Carriers",
    4215: "Travel - Transportation - Courier Services",
    4225: "Travel - Transportation - Public Warehousing",
    4411: "Travel - Transportation - Cruise Lines",
    4457: "Travel - Transportation - Boat Rentals and Leases",
    4468: "Travel - Transportation - Marinas, Marine Service",
    4511: "Travel - Transportation - Airlines, Air Carriers",
    4582: "Travel - Transportation - Airports, Airport Terminals",
    4722: "Travel - Transportation - Travel Agencies and Tour Operators",
    4723: "Travel - Transportation - Package Tour Operators",
    4784: "Travel - Transportation - Toll and Bridge Fees",
    4789: "Travel - Transportation - Transportation Services",
    
    # Utility Services (4800-4999)
    4812: "Utilities - Telecommunication Equipment",
    4813: "Utilities - Telecom Key-Function Transaction",
    4814: "Utilities - Telecommunication Services",
    4815: "Utilities - Monthly Telecom Services",
    4816: "Utilities - Computer Network/Information Services",
    4821: "Utilities - Telegraph Services",
    4829: "Utilities - Money Orders",
    4899: "Utilities - Cable and Other Pay TV Services",
    4900: "Utilities - Electric, Gas, Sanitary, Water",
    
    # Retail Outlet Services (5000-5599)
    5013: "Retail - Motor Vehicle Supplies and Parts",
    5021: "Retail - Office and Commercial Furniture",
    5039: "Retail - Construction Materials",
    5044: "Retail - Office, Photographic Equipment",
    5045: "Retail - Computers and Computer Equipment",
    5046: "Retail - Commercial Equipment",
    5047: "Retail - Medical, Dental Equipment",
    5051: "Retail - Metal Service Centers and Offices",
    5065: "Retail - Electrical Parts and Equipment",
    5072: "Retail - Hardware Equipment and Supplies",
    5074: "Retail - Plumbing and Heating Equipment",
    5085: "Retail - Industrial Supplies",
    5094: "Retail - Precious Stones and Metals",
    5099: "Retail - Durable Goods",
    5111: "Retail - Stationery, Office Supplies",
    5122: "Retail - Drugs, Proprietaries, Sundries",
    5131: "Retail - Piece Goods, Notions, and Other Dry Goods",
    5137: "Retail - Men's, Women's, and Children's Uniforms",
    5139: "Retail - Commercial Footwear",
    5169: "Retail - Chemicals and Allied Products",
    5172: "Retail - Petroleum and Petroleum Products",
    5192: "Retail - Books, Periodicals, and Newspapers",
    5193: "Retail - Florists Supplies, Nursery Stock",
    5198: "Retail - Paints, Varnishes, and Supplies",
    5199: "Retail - Non-Durable Goods",
    5200: "Retail - Home Supply Warehouse Stores",
    5211: "Retail - Lumber and Building Materials",
    5231: "Retail - Glass, Paint, and Wallpaper Stores",
    5251: "Retail - Hardware Stores",
    5261: "Retail - Lawn and Garden Supply Stores",
    5271: "Retail - Mobile Home Dealers",
    5300: "Retail - Wholesale Clubs",
    5309: "Retail - Duty-Free Stores",
    5310: "Retail - Discount Stores",
    5311: "Retail - Department Stores",
    5331: "Retail - Variety Stores",
    5399: "Retail - Miscellaneous General Merchandise",
    5411: "Grocery - Supermarkets and Grocery Stores",
    5422: "Grocery - Meat Providers",
    5441: "Grocery - Candy Stores",
    5451: "Grocery - Dairy Products",
    5462: "Grocery - Bakeries",
    5499: "Grocery - Specialty Food Stores",
    5511: "Retail - Car and Truck Dealers (New and Used)",
    5521: "Retail - Car and Truck Dealers (Used Only)",
    5531: "Retail - Auto and Home Supply Stores",
    5532: "Retail - Automotive Tire Stores",
    5533: "Retail - Automotive Parts and Accessories Stores",
    5541: "Gas - Service Stations",
    5542: "Gas - Automated Fuel Dispensers",
    5551: "Retail - Boat Dealers",
    5561: "Retail - Camper, Recreational and Utility Trailer Dealers",
    5571: "Retail - Motorcycle Shops and Dealers",
    5592: "Retail - Motor Homes Dealers",
    5598: "Retail - Snowmobile Dealers",
    5599: "Retail - Miscellaneous Automotive Dealers",
    
    # Clothing Stores (5600-5699)
    5611: "Retail - Men's and Boys' Clothing and Accessory Stores",
    5621: "Retail - Women's Ready-to-Wear Stores",
    5631: "Retail - Women's Accessory and Specialty Shops",
    5641: "Retail - Children's and Infants' Wear Stores",
    5651: "Retail - Family Clothing Stores",
    5655: "Retail - Sports and Riding Apparel Stores",
    5661: "Retail - Shoe Stores",
    5681: "Retail - Furriers and Fur Shops",
    5691: "Retail - Men's and Women's Clothing Stores",
    5697: "Retail - Tailors, Seamstresses, Mending",
    5698: "Retail - Wig and Toupee Stores",
    5699: "Retail - Miscellaneous Apparel and Accessory Shops",
    
    # Miscellaneous Stores (5700-7299)
    5712: "Retail - Furniture, Home Furnishings",
    5713: "Retail - Floor Covering Stores",
    5714: "Retail - Drapery, Window Covering",
    5718: "Retail - Fireplace, and Accessories Stores",
    5719: "Retail - Miscellaneous Home Furnishing Stores",
    5722: "Retail - Household Appliance Stores",
    5732: "Retail - Electronics Stores",
    5733: "Retail - Music Stores (Musical Instruments, Pianos)",
    5734: "Retail - Computer Software Stores",
    5735: "Retail - Record Stores",
    5811: "Dining - Caterers",
    5812: "Dining - Restaurants",
    5813: "Dining - Bars, Lounges, Discos, Nightclubs, Taverns",
    5814: "Dining - Fast Food Restaurants",
    5815: "Digital Goods - Digital Goods: Media, Books, Movies, Music",
    5816: "Digital Goods - Digital Goods: Games",
    5817: "Digital Goods - Digital Goods: Applications (Excludes Games)",
    5818: "Digital Goods - Digital Goods: Large Digital Goods Merchant",
    5832: "Retail - Antique Shops",
    5912: "Drugstores - Drug Stores and Pharmacies",
    5921: "Retail - Package Stores, Beer, Wine, and Liquor",
    5931: "Retail - Used Merchandise and Secondhand Stores",
    5932: "Retail - Antique Shops - Sales, Repairs",
    5933: "Retail - Pawn Shops",
    5935: "Retail - Wrecking and Salvage Yards",
    5937: "Retail - Antique Reproductions",
    5940: "Retail - Bicycle Shops - Sales and Service",
    5941: "Retail - Sporting Goods Stores",
    5942: "Retail - Book Stores",
    5943: "Retail - Stationery Stores, Office Supplies",
    5944: "Retail - Jewelry Stores, Watches, Clocks",
    5945: "Retail - Hobby, Toy, and Game Shops",
    5946: "Retail - Camera and Photographic Supply Stores",
    5947: "Retail - Gift, Card, Novelty, and Souvenir Shops",
    5948: "Retail - Luggage and Leather Goods Stores",
    5949: "Retail - Fabric, Needlework, Piece Goods, and Sewing Stores",
    5950: "Retail - Glassware, Crystal Stores",
    5960: "Retail - Direct Marketing - Insurance Services",
    5962: "Retail - Direct Marketing - Travel",
    5963: "Retail - Door-to-Door Sales",
    5964: "Retail - Direct Marketing - Catalog Merchant",
    5965: "Retail - Direct Marketing - Combination Catalog and Retail Merchant",
    5966: "Retail - Direct Marketing - Outbound Telemktg Merchant",
    5967: "Retail - Direct Marketing - Inbound Telemktg Merchant",
    5968: "Retail - Direct Marketing - Continuity/Subscription Merchant",
    5969: "Retail - Direct Marketing - Other Direct Marketers",
    5970: "Retail - Artists' Supply and Craft Shops",
    5971: "Retail - Art Dealers and Galleries",
    5972: "Retail - Stamp and Coin Stores",
    5973: "Retail - Religious Goods Stores",
    5975: "Retail - Hearing Aids - Sales, Service",
    5976: "Retail - Orthopedic Goods - Prosthetic Devices",
    5977: "Retail - Cosmetic Stores",
    5978: "Retail - Typewriter Stores - Sales, Service",
    5983: "Retail - Fuel Dealers - Fuel Oil, Wood, Coal",
    5992: "Retail - Florists",
    5993: "Retail - Cigar Stores and Stands",
    5994: "Retail - News Dealers and Newsstands",
    5995: "Retail - Pet Shops, Pet Foods, and Supplies",
    5996: "Retail - Swimming Pools - Sales, Supplies",
    5997: "Retail - Electric Razor Stores - Sales and Service",
    5998: "Retail - Tent and Awning Shops",
    5999: "Retail - Miscellaneous Specialty Retail",
    6010: "Financial - Manual Cash Disbursements",
    6011: "Financial - Automated Cash Disbursements",
    6012: "Financial - Financial Institutions",
    6050: "Financial - Quasi Cash—Member Financial Institution",
    6051: "Financial - Quasi Cash—Merchant",
    6211: "Financial - Securities—Brokers/Dealers",
    6300: "Financial - Insurance Sales/Underwriting",
    6381: "Financial - Insurance Premiums",
    6399: "Financial - Insurance - Default",
    6513: "Financial - Real Estate Agents and Managers - Rentals",
    6529: "Financial - Remote Stored Value Load",
    6530: "Financial - Remote Stored Value Load",
    6531: "Financial - Payment Service Provider",
    6532: "Financial - Payment Transaction--Member",
    6533: "Financial - Payment Transaction--Merchant",
    6534: "Financial - Money Transfer--Member",
    6535: "Financial - Value Purchase--Member",
    6536: "Financial - Money Transfer--Merchant",
    6537: "Financial - Money Transfer for a Purchase—Merchant",
    6538: "Financial - MoneySend Intracountry",
    6539: "Financial - MoneySend Funding",
    6540: "Financial - Stored Value Card Purchase/Load",
    7011: "Travel - Lodging - Hotels, Motels, Resorts",
    7032: "Recreation - Sporting and Recreational Camps",
    7033: "Recreation - Trailer Parks, Campgrounds",
    7210: "Services - Laundry, Cleaning, and Garment Services",
    7211: "Services - Laundry - Family and Commercial",
    7216: "Services - Dry Cleaners",
    7217: "Services - Carpet and Upholstery Cleaning",
    7221: "Services - Photographic Studios",
    7230: "Services - Beauty and Barber Shops",
    7251: "Services - Shoe Repair Shops",
    7261: "Services - Funeral Service and Crematories",
    7273: "Services - Dating and Escort Services",
    7276: "Services - Tax Preparation Services",
    7277: "Services - Counseling Services - Debt, Marriage",
    7278: "Services - Buying and Shopping Services, Clubs",
    7296: "Services - Clothing Rental",
    7297: "Services - Massage Parlors",
    7298: "Services - Health and Beauty Spas",
    7299: "Services - Miscellaneous Personal Services",
    
    # Business Services (7300-7999)
    7311: "Business - Advertising Services",
    7321: "Business - Consumer Credit Reporting Agencies",
    7333: "Business - Commercial Photography, Art, and Graphics",
    7338: "Business - Quick Copy, Reproduction, and Blueprinting",
    7339: "Business - Stenographic and Secretarial Support",
    7342: "Business - Exterminating and Disinfecting Services",
    7349: "Business - Cleaning, Maintenance, and Janitorial Services",
    7361: "Business - Employment Agencies, Temporary Help Services",
    7372: "Business - Computer Programming and Data Processing",
    7375: "Business - Information Retrieval Services",
    7379: "Business - Computer Maintenance and Repair Services",
    7392: "Business - Management, Consulting, and Public Relations",
    7393: "Business - Detective Agencies, Protective Services",
    7394: "Business - Equipment, Tool, Furniture, and Appliance Rental",
    7395: "Business - Photofinishing Laboratories, Photo Developing",
    7399: "Business - Business Services, Not Elsewhere Classified",
    7512: "Business - Automobile Rental Agency",
    7513: "Business - Truck and Utility Trailer Rentals",
    7519: "Business - Motor Home and Recreational Vehicle Rentals",
    7523: "Business - Parking Lots and Garages",
    7531: "Business - Automotive Body Repair Shops",
    7534: "Business - Tire Retreading and Repair Shops",
    7535: "Business - Automotive Paint Shops",
    7538: "Business - Automotive Service Shops",
    7542: "Business - Car Washes",
    7549: "Business - Towing Services",
    7622: "Business - Electronics Repair Shops",
    7623: "Business - A/C and Refrigeration Repair",
    7629: "Business - Electrical and Small Appliance Repair",
    7631: "Business - Watch, Clock, and Jewelry Repair",
    7641: "Business - Furniture Reupholstery, Repair",
    7692: "Business - Welding Services",
    7699: "Business - Miscellaneous Repair Shops",
    7800: "Entertainment - Government-Owned Lotteries",
    7801: "Entertainment - Government-Licensed Casinos",
    7802: "Entertainment - Government-Licensed Horse/Dog Racing",
    7829: "Entertainment - Motion Picture and Video Tape Production",
    7832: "Entertainment - Motion Picture Theaters",
    7841: "Entertainment - Video Tape Rental Stores",
    7911: "Entertainment - Dance Halls, Studios, and Schools",
    7922: "Entertainment - Theatrical Producers and Ticket Agencies",
    7929: "Entertainment - Bands, Orchestras, and Entertainers",
    7932: "Entertainment - Billiard and Pool Establishments",
    7933: "Entertainment - Bowling Alleys",
    7941: "Entertainment - Commercial Sports, Athletic Fields",
    7991: "Entertainment - Tourist Attractions and Exhibits",
    7992: "Entertainment - Public Golf Courses",
    7993: "Entertainment - Video Amusement Game Supplies",
    7994: "Entertainment - Video Game Arcades/Establishments",
    7995: "Entertainment - Betting/Casino Gambling",
    7996: "Entertainment - Amusement Parks, Carnivals, Circuses",
    7997: "Entertainment - Membership Clubs (Sports, Recreation)",
    7998: "Entertainment - Aquariums, Seaquariums, Dolphinariums",
    7999: "Entertainment - Recreation Services (Not Elsewhere Classified)",
    
    # Professional Services (8000-8999)
    8011: "Professional - Doctors and Physicians",
    8021: "Professional - Dentists and Orthodontists",
    8031: "Professional - Osteopathic Physicians",
    8041: "Professional - Chiropractors",
    8042: "Professional - Optometrists and Ophthalmologists",
    8043: "Professional - Optical Goods and Eyeglasses",
    8049: "Professional - Podiatrists and Chiropodists",
    8050: "Professional - Nursing and Personal Care Facilities",
    8062: "Professional - Hospitals",
    8071: "Professional - Medical and Dental Laboratories",
    8099: "Professional - Medical Services and Health Practitioners",
    8111: "Professional - Legal Services and Attorneys",
    8211: "Professional - Elementary and Secondary Schools",
    8220: "Professional - Colleges, Universities",
    8241: "Professional - Correspondence Schools",
    8244: "Professional - Business and Secretarial Schools",
    8249: "Professional - Trade and Vocational Schools",
    8299: "Professional - Educational Services",
    8351: "Professional - Child Care Services",
    8398: "Professional - Charitable and Social Service Organizations",
    8641: "Professional - Civic, Social, and Fraternal Associations",
    8651: "Professional - Political Organizations",
    8661: "Professional - Religious Organizations",
    8675: "Professional - Automobile Associations",
    8699: "Professional - Membership Organizations",
    8734: "Professional - Testing Laboratories",
    8911: "Professional - Architectural, Engineering, and Surveying Services",
    8931: "Professional - Accounting, Auditing, and Bookkeeping Services",
    8999: "Professional - Professional Services",
    
    # Government Services (9000-9999)
    9211: "Government - Court Costs, Including Alimony and Child Support",
    9222: "Government - Fines",
    9223: "Government - Bail and Bond Payments",
    9311: "Government - Tax Payments",
    9399: "Government - Government Services",
    9402: "Government - Postal Services - Government Only",
    9405: "Government - Intra-Government Purchases - Government Only",
    9700: "Government - Automated Referral Service",
    9701: "Government - Visa Credential Service",
    9702: "Government - GCAS Emergency Services",
    9950: "Government - Intra-Company Purchases",
}

# Group MCC codes by ranges for codes not specifically defined
def get_mcc_category(mcc_code):
    """
    Returns the category for a given MCC code
    
    Args:
        mcc_code (int): The MCC code to look up
        
    Returns:
        str: The category corresponding to the MCC code
    """
    # Check if there's a specific category for this code
    if mcc_code in mcc_specific:
        return mcc_specific[mcc_code]
    
    # If not, use the range-based categorization
    
    # Airlines
    if 3000 <= mcc_code <= 3299:
        return "Travel - Airlines"
    
    # Car Rental
    elif 3300 <= mcc_code <= 3499:
        return "Travel - Car Rental"
    
    # Hotels & Lodging
    elif 3500 <= mcc_code <= 3999:
        return "Travel - Lodging"
    
    # Transportation Services
    elif 4000 <= mcc_code <= 4799:
        return "Travel - Transportation"
    
    # Utility Services
    elif 4800 <= mcc_code <= 4999:
        return "Utilities"
    
    # Retail Outlet Services
    elif 5000 <= mcc_code <= 5599:
        return "Retail"
    
    # Clothing Stores
    elif 5600 <= mcc_code <= 5699:
        return "Retail - Clothing"
    
    # Miscellaneous Stores
    elif 5700 <= mcc_code <= 7299:
        return "Retail - Miscellaneous"
    
    # Business Services
    elif 7300 <= mcc_code <= 7999:
        return "Business Services"
    
    # Professional Services
    elif 8000 <= mcc_code <= 8999:
        return "Professional Services"
    
    # Government Services
    elif 9000 <= mcc_code <= 9999:
        return "Government"
    
    # Unknown
    else:
        return "Unknown Category"




#################################################################################################################################################################


















# Example usage:
# Create some credit cards with their reward structures

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