from abc import ABC,abstractmethod

class Class1(ABC):
    address = None

    def __init__(self,address):
        self.address = address

    @abstractmethod
    def   calculateFreqs(self):
        pass


class ListCount(Class1):

    def calculateFreqs(self):
        freq_list=[0]*26

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        index=ord(char.lower())-ord('a')
                        freq_list[index]+=1

        for i,freq in enumerate(freq_list):
            if freq>0:
                letter=chr(i+ ord('a'))
                print(f"{letter}={freq}")



class DictCount(Class1):
    def calculateFreqs(self):
        freq_dict={}

        with open(self.address,'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char=char.lower()
                        freq_dict[char]=freq_dict.get(char,0)+1

        for letter ,freq in freq_dict.items():
            print(f'"{letter}" {freq}')



list_counter=ListCount("weirdWords.txt")
dict_counter=DictCount("weirdWords.txt")

print("LİstCount is: ")
list_counter.calculateFreqs()

print("\nDictCount is :")
dict_counter.calculateFreqs()












