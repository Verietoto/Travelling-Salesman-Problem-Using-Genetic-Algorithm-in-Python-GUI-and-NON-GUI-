
"""
Hello World!!! This is a free python code of Traveling Salesman Problem. The main idea is find the shortest closed
polygon route that salesman have to finish.

Contact Me:

Email:      Verietoto@gmail.com
Linkedin:   www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0

"""

"""
importing Some libraries
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
import sys

class RouteChossing:
    def __init__(self, city, coor, popolationNum, parentNum, mutationRate,  typeSelection = "Roulette"):
        """

        :param city: Name of City or Point (Str)
        :param coor: Coordinate [x,y] of each city
        :param popolationNum: How many Individu you want to have (int)
        :param parentNum: How many best individu you pick (int)
        :param mutationRate: Rate of genes mutation
        :param typeSelection: How to choose best individu
        :function createPopulation: Creating a set of route
        :function calculateFtness: Cacluate fitness of every route in population
        :function selectParent: Select N Best Parent based on a methpd
        :function Update: Update population member by replacing the farthest distance to child
        :function showResult: Show the end of prediction results

        """
        self.city = city
        self.coordinate = coor
        self.populationNumber = popolationNum
        self.parentNumber = parentNum
        self.mutationRate = mutationRate
        self.typeSelection = typeSelection

        self.createPopulation()
        self.calculatePopulationFitness()
        self.selectParent()
        self.createChildren()

    def mutation(self, data):
        """
        Mutate 2 random point of genes
        :param data: a set of route, ex: [1,0,3,4,5,1]
        :return: Mutated Data
        """
        mutateChild = data
        randomValue = np.random.rand(1)
        if self.mutationRate > randomValue:
            i = True
            while i == True:
                point1 = np.random.randint(1, len(self.city)-1)
                point2 = np.random.randint(1, len(self.city)-1)
                if point1!=point2:
                    i=False
            a, b = mutateChild[point1], mutateChild[point2]

            mutateChild[point1] = b
            mutateChild[point2] = a
        else:
            mutateChild = data

        return mutateChild

    def crossOver(self, parent1, parent2):
        """

        :param parent1: Route1
        :param parent2: Route2
        :return:
        """
        check = "Not Checked"
        point = 1 + len(parent1) // 3
        parent1Gen = parent1[point:-point]
        parent2Gen = parent2[point:-point]

        child1 = [x for x in parent1[0:-1] if x not in parent2Gen]
        child2 = [x for x in parent2[0:-1] if x not in parent1Gen]

        for i in range(len(parent2Gen)):
            child1.insert(point, parent2Gen[i])
            child2.insert(point, parent1Gen[i])
            point += 1
        child1.append(child1[0])
        child2.append(child2[0])
        return child1, child2

    def getDistance(self, data):
        """
        Calculates Distance in a set of route
        :param data: a set of route list, ex = [1,3,2,1]
        :return: Distance (Float)
        """
        d = 0
        for i in range(len(data) - 1):
            coorNow = self.coordinate[data[i]]
            coorAfter = self.coordinate[data[i + 1]]
            distance = [i - j for i, j in zip(coorNow, coorAfter)]
            d += np.sqrt(distance[0] ** 2 + distance[1] ** 2)
        return d

    def getFitness(self, data):
        """
        Fitness is 1/distance, Basicly the longer distance, the smaller fitness be.
        :param data:
        :return: Fitness
        """
        return 1/self.getDistance(data)

    def createParent(self):
        """
        Creating 1 Individu
        :return: set of Route
        """
        index = np.arange(0,len(self.city))
        parent = list(np.random.choice(index,len(self.city), replace=False))
        parent.append(parent[0])
        return parent

    def createPopulation(self):
        """
        Creating a set of Individu
        :return: self.popoulation is a set of individu list
        """
        self.population = []
        maximumPopulation = 1
        maximumParent = 1

        # Maximum Pent is a permutation of length(city) of length(city)
        for i in range(1, len(self.city) + 1):
            maximumPopulation *= i
        if self.populationNumber > maximumPopulation:
            raise ValueError("The number population is exceeding total permutation of posible route")

        # Maximum parent is permutation of population length and 2
        i = 1
        while i != self.populationNumber:
            parent = self.createParent()
            if parent in self.population:
                continue
            else:
                self.population.append(parent)
                i += 1

    def calculatePopulationFitness(self):
        """
        Calculate Fitness of every individu in population
        :return: self.populationFitness and self.populationDistance
        """
        self.populationDistance = []
        self.populationFitness = []

        for i in self.population:
            self.populationDistance.append(self.getDistance(i))
            self.populationFitness.append(self.getFitness(i))

    def selectParent(self):
        """
        Selecting N best parent bsed on some method
        :return:
        """
        parent = []
        if self.typeSelection == "Roulette":
            indexes = np.argsort(self.populationDistance)
            indexes = np.random.choice(indexes, self.parentNumber,self.populationFitness)


            for i in range(self.parentNumber):
                parent.append(self.population[indexes[i]])
            self.parent = list(permutations(parent, 2))

        elif self.typeSelection == "Ranks":
            indexes = np.argsort(self.populationDistance)[0:self.parentNumber]
            for i in range(self.parentNumber):
                parent.append(self.population[indexes[i]])
            self.parent = list(permutations(parent, 2))

        elif self.typeSelection == "Random":
            indexes = np.random.randint(0, len(self.population), self.parentNumber)
            for i in range(self.parentNumber):
                parent.append(self.population[indexes[i]])
            self.parent = list(permutations(parent, 2))

    def createChildren(self):
        """
        Creating a set of child from best individu
        :return: child (a set of new route from parent) and childrenFitness
        """
        self.childrenFitness = []
        self.children = []
        self.childrenDistance = []

        for i in self.parent:
            child1, child2 = self.crossOver(i[0], i[1])
            self.children.append(self.mutation(child1))
            self.children.append(self.mutation(child2))
        if len(self.children) > self.populationNumber:
            raise ValueError("Number of Childer you made exceed population exist")

        for i in self.children:
            self.childrenDistance.append(self.getDistance(i))
            self.childrenFitness.append(self.getFitness(i))