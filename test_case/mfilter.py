import json

class Mfilter:

    def __init__(self,assertEqual):
        self.assertEqual = assertEqual

    def run(self,item,array):
        for a in array:
            param = a.split('|')
            name = param[0]

            if "require" in param:
                if name not in item:
                    self.__validRequire(name)

            if name not in item:
                continue

            if "int" in param:
                self.__validInt(name, item[name])

            if "float" in param:
                self.__validFloat(name, item[name])

            if  "varchar" in param:
                self.__validVarchar(name, item[name])

            if  "array" in param:
                self.__validArray(name, item[name])

            if "Bool" in param:
                self.__validBool(name, item[name])



    def __validRequire(self,name):
        self.assertEqual.assertEqual(name, -1, name + ' require')

    def __validBool(self, name, value):
        if type(value) != type(True) or type(value) !=type(False):
            self.assertEqual.assertEqual(name, -1, name + ' require Bool')


    def __validInt(self,name,value):
        if type(value) != type(1):
            self.assertEqual.assertEqual(name, -1, name+' require int')

    def __validFloat(self,name,value):
        if type(value) != type(1.23) and type(value)!=type(2):
            self.assertEqual.assertEqual(name, -1, name + ' require float')

    def __validArray(self, name, value):
        if type(value) != type([]):
            self.assertEqual.assertEqual(name, -1, name + ' require array')

    def __validVarchar(self,name,value):
        if type(value)==type(u"unicode"):
            value = value.encode('utf-8')

        if type(value) != type("1"):
            self.assertEqual.assertEqual(name, -1, name+' require string')

    def __valid(self,value):
        if type(value)==type(u"unicode"):
            value = value.encode('utf-8')
        return value