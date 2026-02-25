import datetime
import math

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items
    
    @property
    def item_price(self):
        return self.__item_price
    
    @property
    def tax_rate(self):
        return self.__tax_rate
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
           self.__name_items.append(name)
           self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for key, value in self.__item_price.items():
            if key in self.__name_items:
                total.append(value)
        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        total_tax = []
        for key, value in self.__tax_rate.items():
            if key in self.__name_items and value == 10:
                ten_percent_tax.append(key)
        for key, value in self.__item_price.items():
            if key in ten_percent_tax:
                total.append(value)
        if len(self.__name_items) > 10:
            for i in total:
                i_with_sale = i * 0.9
                total_tax.append(i_with_sale)
            return sum(total_tax) * 0.1
        else:
            for i in total:
                i_with_nds = i * 0.1
                total_tax.append(i_with_nds)
            return sum(total_tax)
        
    def total_tax(self):
        total = []
        for name in self.__name_items:
            price = self.__item_price[name]
            rate = self.__tax_rate[name]
            nds = price * (rate / 100)
            total.append(nds)
        return sum(total)
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) is str:
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return '+7' + str(telephone_number)
        
collector = OnlineSalesRegisterCollector()

# --- add_item_to_cheque ---
collector.add_item_to_cheque('кола')
collector.add_item_to_cheque('молоко')

print("items:", collector.name_items)      # ['кола', 'молоко']
print("count:", collector.number_items)    # 2


# --- delete_item_from_check ---
collector.delete_item_from_check('кола')
print("after delete:", collector.name_items)   # ['молоко']


# --- check_amount ---
collector.add_item_to_cheque('кефир')
print("amount:", collector.check_amount())


# --- ten_percent_tax_calculation ---
print("10% tax:", collector.ten_percent_tax_calculation())


# --- total_tax ---
print("total tax:", collector.total_tax())


# --- telephone ---
print(OnlineSalesRegisterCollector.get_telephone_number(9991234567))

