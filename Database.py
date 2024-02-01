import pandas as pd

class Database():

    def __init__(self):
        self.cols = ['Account Number', 'Routing Number', 'Username', 'Password',
                     'Balence', 'Transactions']
        self.rows = []
        self.df = pd.DataFrame()
        for col in self.cols:
            self.df[col] = 0

    def add(self, dict, name=None):
        if name == None:
            name = 'account' + str(len(self.rows)+1)
        self.df.loc[name] = self.update(dict, name)
        return
    
    def createRow(self):
        dict = {}
        for col in self.cols:
            dict[col] = '-1'
        return dict
    
    def update(self, dict, name):
        if name in self.rows:
            defualtDict = self.df.loc[name, :]
        else:
            self.rows.append(name)
            defualtDict = self.createRow()

        for key in dict:
            if key in defualtDict:
                defualtDict[key] = dict[key]

        return defualtDict
        

data = Database()
data.add({'Username': 'apple'})
data.add({'Password': 'trash'}, 'account1')
print(data.df)