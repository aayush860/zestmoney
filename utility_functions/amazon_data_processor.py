class amazon_data_processor:
    def __init__(self, string):
        self.string = string
        self.data = []

    def process(self):
        self.data = self.string.split('\n')
        indexx = self.data.index('Apple iPhone 11 (64GB) - Black')
        value = int(self.data[indexx+2].split('₹')[1].replace(',', ''))
        return value

