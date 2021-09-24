'''
這邊以一個較大的範例來應用
設計一個簡單的房地產應用程式來管理可銷售或出租的標的

標的有兩種： 公寓、透天厝，
仲介需要能在這兩個標的上輸入相關細節、列出標的、出售或已出租

仔細審閱需求
透天厝與公寓為不同類別
租與售也要用不同表示方式
'''

# 從Property開始實作
# Property能夠被透天厝和公寓繼承
# 額外加入 **kwargs 用於多重繼承
# 加入 super().__init__ 避免此類別不是多重繼承中最後一個被呼叫的
# prompt_init為靜態方法，可直接呼叫方法使用
class Property:
    def __init__(self, square_feet = '', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    
    def display(self):
        '''Display the proporty detail information'''
        print("PROPERTY DETAILS")
        print("================")
        print(f"square footage: {self.square_feet}")
        print(f"bedrooms: {self.num_bedrooms}")
        print(f"bathrooms: {self.num_baths}")
        print()
    
    @staticmethod
    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),
                    beds = input("Enter the number of bedrooms: "),
                    baths = input("Enter number of baths: ")
                    )

# 用在 Apartment, House 的 prompt_init 靜態方法
def get_valid_input(input_string: str, valid_options: tuple):
    input_string += f"({', '.join(valid_options)})"
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


# Apartment 擴充 Property
class Apartment(Property):
    valid_laundries = ('coin','ensuite','none')
    valid_balconies = ('yes','no','solarium')

    # __init__ 和 display 加上 super() 呼叫相對應父類別方法確保Property正確的初始化
    def __init__(self, balcony = '', laundry = '', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    
    def display(self):
        super().display()
        print('APARTMENT DETAILS')
        print('=================')
        print(f"laundry: {self.laundry}")
        print(f'has balcony: {self.balcony}')
        print()
    
    # @staticmethod
    # def prompt_init():
    #     '''
    #     從父類別取得靜態值，
    #     並加上Apartment有的靜態值
    #     回傳dict

    #     但是此函式過於冗長且在 House 又要再寫一次，試著將以下東西函式化寫在class外
    #     '''
    #     parent_init = Property.prompt_init()

    #     laundry = ''
    #     while laundry.lower not in Apartment.valid_laundries:
    #         laundry = input(f"What laundry facilities does the property have ({', '.join(Apartment.valid_laundries)})")
        
    #     balcony = ''
    #     while balcony.lower not in Apartment.valid_balconies:
    #         balcony = input(f"Does the property have a balcony? ({', '.join(Apartment.valid_balconies)})")
        
    #     parent_init.update(
    #         {
    #             "laundry": laundry,
    #             "balcony": balcony,
    #         }
    #     )
    #     return parent_init

    @staticmethod
    def prompt_init():
        '''
        從父類別取得靜態值，
        並加上Apartment有的靜態值
        回傳dict
        '''
        parent_init = Property.prompt_init()

        # 簡潔許多!
        laundry = get_valid_input('What laundry facilities does the property have ', Apartment.valid_laundries)
        balcony = get_valid_input('Does the property have a balcony? ', Apartment.valid_balconies)
        parent_init.update(
            {
                "laundry": laundry,
                "balcony": balcony,
            }
        )
        return parent_init

class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories = '', garage = '', fenced = '', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories
    
    def display(self):
        super().display()
        print('HOUSE DETAILS')
        print('=============')
        print(f'# of stories: {self.num_stories}')
        print(f'garage: {self.garage}')
        print(f'fenced yard: {self.fenced}')
        print()
    
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input('Is the yard fenced? ', House.valid_fenced)
        garage = get_valid_input('Is there a garage? ', House.valid_garage)
        num_stories = input("How many stories? ")
    
        parent_init.update(
            {
                "fenced": fenced,
                "garage": garage,
                "num_stories": num_stories,
            }
        )
        return parent_init

class Purchase:
    def __init__(self, price = '', taxes = '', **kwargs) -> None:
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
    
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("================")
        print(f"selling price: {self.price}")
        print(f"estimated taxes: {self.taxes}")
        print()
    
    @staticmethod
    def prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )

class Rental:
    def __init__(self, furnished = '', utilities = '', rent = '', **kwargs) -> None:
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("==============")
        print(f"rent: {self.rent}")
        print(f"estimated utilities: {self.utilities}")
        print(f"furnished: {self.furnished}")
        print()

    @staticmethod
    def prompt_init():
        return dict(
            rent = input('What is the monthly rent? '),
            utilities = input('What are the estimated utilities? '),
            furnished = get_valid_input("Is the property furnished?", ('yes', 'no'))
        )

class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(House.prompt_init())
        return init

class Agent:
    def __init__(self) -> None:
        self.property_list = []

    def display_property(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase,
    }

    def add_property(self):
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ", ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type,payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
