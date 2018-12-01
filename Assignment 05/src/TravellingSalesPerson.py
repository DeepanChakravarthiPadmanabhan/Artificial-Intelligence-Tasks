import Helper
import matplotlib.pyplot as plt
import random

class TravellingSalePerson:

    # def __init__(self):
    #     self.listOfCities = []
    #     self.CalculateHeuristic = True

    def __init__(self, listOfCities=[]):
        self.listOfCities = listOfCities
        self.CalculateHeuristic = True

    def get_hn(self):
        if(self.CalculateHeuristic):
            i = 0
            distance = 0
            while(i+1 < len(self.listOfCities)):
                distance += self.get_cityDistance(self.GetCity(i), self.GetCity(i+1))
                i += 1
            self.distance = distance
        return self.distance

    def get_cityDistance(self, city1, city2):
        return Helper.GetDistance(city1.latitude, city1.longitude, city2.latitude, city2.longitude)

    def ReCalculateHeuristic(self):
        self.CalculateHeuristic = True

    def AddCity(self, city):
        self.listOfCities.append(city)

    def GetCity(self, index):
        return self.listOfCities[index]

    def GetCityCount(self):
        return len(self.listOfCities)

    def GetNewTSP(self):
        newList = Helper.DeepCopyList(self.listOfCities)
        newTSP = TravellingSalePerson(newList)
        return newTSP

    def Randomize(self):
        random.shuffle(self.listOfCities)

    def GetRightSuccessorAt(self, index):
        newTSP = self.GetNewTSP()
        index1 = index % newTSP.GetCityCount()
        index2 = (index + 1) % newTSP.GetCityCount()
        return TravellingSalePerson.Swap(newTSP, index1, index2)

    def GetLeftSuccessorAt(self, index):
        newTSP = self.GetNewTSP()
        index1 = index % newTSP.GetCityCount()
        index2 = (index - 1) % newTSP.GetCityCount()
        return TravellingSalePerson.Swap(newTSP, index1, index2)

    def GetSuccessorAt(self, tsp, index1, index2):
        return TravellingSalePerson.Swap(tsp, index1, index2)

    def GetAllSuccessors(self, index):
        count = self.GetCityCount()
        listOfScuccessors = []

        for i in range(1, count):
            newTSP = self.GetNewTSP()
            index1 = index % newTSP.GetCityCount()
            index2 = (index + i) % newTSP.GetCityCount()
            listOfScuccessors.append(TravellingSalePerson.Swap(newTSP, index1, index2))

        return listOfScuccessors

    def PlotPath(self):
        plt.plot([city.latitude for city in self.listOfCities], [city.longitude for city in self.listOfCities])
        plt.xlabel('Latitude')
        plt.ylabel('Longitude')
        plt.show()



    @staticmethod
    def Swap(tsp,  index1, index2):
        temp = tsp.GetCity(index1)
        tsp.listOfCities[index1] = tsp.GetCity(index2)
        tsp.listOfCities[index2] = temp
        tsp.CalculateHeuristic = True
        return tsp

