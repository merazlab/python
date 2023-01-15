# Python features class


class MyFeatures:
    
    def __init__(self, features=None) -> None:
        self.features={}
        
    def set_features(self, name, feature):
        self.features[name] = feature
        
    def show_features(self, name):
        print(self.features[name])
        
    def __len__(self):
        print(len(self.features.keys()))
        
f1 = MyFeatures()
f1.set_features('age', [2, 4, 6])
f1.set_features('saliry', [1, 2, 3])

f1.show_features('age')
f1.show_features('saliry')

f1.len()