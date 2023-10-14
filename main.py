# Brandon Smith 001395827

import csv
import datetime
import HashTable
from Package import Package

# Create Hashtable for storage
packageHashTable = HashTable.Hashtable(10)

# Read in CSV package file
# runs O(N) time and O(N) space complexity

with open(r"C:\Users\sox_b\PycharmProjects\packageDeliveryApp\WGUPS Package File.csv", 'r') as csvFile:
    packageFile = csv.reader(csvFile)

    next(packageFile)
    for row in packageFile:
        packageID = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zipCode = row[4]
        deliveryDeadline = row[5]
        massKilo = row[6]
        specialNotes = row[7]

        package = Package(packageID, address, city, state, zipCode, deliveryDeadline, massKilo, specialNotes)
        packageHashTable.insert(key=packageID, value=package)

# Read in CSV distance file
# runs O(N*N) time and O(N) space complexity
with open(r"C:\Users\sox_b\PycharmProjects\packageDeliveryApp\WGUPS Distance Table .csv", 'r') as csvDistanceFile:
    distanceFile = csv.reader(csvDistanceFile)
    next(distanceFile)
    readInList = []
    for row in distanceFile:
        readInList.append(row)

    addressList = readInList[0:27]
    for i in addressList:
        i.remove('''''')
    distanceList = readInList[28::]

# Loading trucks with packages with packageID reference

truck1 = [14, 16, 20, 15, 19, 13, 21, 12, 37, 34, 27, 35, 29, 7, 39, 30]
truck2 = [3, 18, 36, 38, 1, 25, 26, 28, 32, 31, 6, 5, 40, 4, 10, 17]
truck3 = [8, 9, 2, 11, 22, 23, 24, 33]

# Initializing timekeeper for different trucks with different start times
global truck1Time
truck1Time = datetime.datetime(2021, 1, 19, 8, 0, 0)
global truck2Time
truck2Time = datetime.datetime(2021, 1, 19, 9, 5, 0)
global truck3Time
truck3Time = datetime.datetime(2021, 1, 19, 10, 20, 0)

# Initializing mileage keeper for different trucks and total mileage of all trucks
global truck1Mileage
truck1Mileage = 0
global truck2Mileage
truck2Mileage = 0
global truck3Mileage
truck3Mileage = 0
global totalMileage
totalMileage = 0


# Delivery algorithm
# runs O(N*N) time and O(N) space complexity
def packageDelivery(self):
    # Setting the enrouteStartTime
    if self == truck1:
        for i in self:
            package = packageHashTable.find(i)
            global truck1Time
            package.enrouteStartTime = truck1Time.time()

    elif self == truck2:
        for i in self:
            package = packageHashTable.find(i)
            global truck2Time
            package.enrouteStartTime = truck2Time.time()

    else:
        for i in self:
            package = packageHashTable.find(i)
            global truck3Time
            package.enrouteStartTime = truck3Time.time()

    undeliveredPackages = self.copy()
    shortestPath = float('inf')

    while (len(undeliveredPackages) != 0):
        if len(undeliveredPackages) == len(self):

            for iD in undeliveredPackages:
                package = packageHashTable.find(iD)
                addressIndex = addressList.index([package.address])
                currentAddressIndex = 0
                if float(distanceList[currentAddressIndex][addressIndex]) < shortestPath:
                    shortestPath = float(distanceList[currentAddressIndex][addressIndex])
                    nextDeliveryAdddress = package.address
                    nextPackageID = package.packageID

        else:
            for iD in undeliveredPackages:
                package = packageHashTable.find(iD)
                addressIndex = addressList.index([package.address])
                if float(distanceList[currentAddressIndex][addressIndex]) < shortestPath:
                    shortestPath = float(distanceList[currentAddressIndex][addressIndex])
                    nextDeliveryAdddress = package.address
                    nextPackageID = package.packageID
        undeliveredPackages.remove(nextPackageID)
        currentAddressIndex = addressList.index([nextDeliveryAdddress])
        package = packageHashTable.find(nextPackageID)
        package.deliveryStatus = 'delivered'
        travelTime = int((shortestPath / 18) * 60)
        travelMileage = 18 * (travelTime / 60)
        global totalMileage
        totalMileage += travelMileage
        shortestPath = float('inf')

        if self == truck1:
            truck1Time = truck1Time + datetime.timedelta(minutes=travelTime)
            package.deliveryTime = truck1Time.time()
            global truck1Mileage
            truck1Mileage += travelMileage

        elif self == truck2:
            truck2Time = truck2Time + datetime.timedelta(minutes=travelTime)
            package.deliveryTime = truck2Time.time()
            global truck2Mileage
            truck2Mileage += travelMileage
        else:
            truck3Time = truck3Time + datetime.timedelta(minutes=travelTime)
            package.deliveryTime = truck3Time.time()
            global truck3Mileage
            truck3Mileage += travelMileage


packageDelivery(truck1)
packageDelivery(truck2)
packageDelivery(truck3)

# Console user interface section
truckOrPackageSelection = None
while truckOrPackageSelection != 3:
    print('Which type of information would you like to display?')
    print('Enter 1 for Truck Info.')
    print('Enter 2 for Package info.')
    print('Enter 3 to close application.')

    truckOrPackageSelection = int(input())

    if truckOrPackageSelection == 1:
        print('{} has a total mileage of {} miles.'.format('Truck1', truck1Mileage))
        print('{} has a total mileage of {} miles.'.format('Truck2', truck2Mileage))
        print('{} has a total mileage of {} miles.'.format('Truck3', truck3Mileage))
        print('{} have a total mileage of {} miles.'.format('All trucks', int(totalMileage)))
        print()

    elif truckOrPackageSelection == 2:
        print('What time would you like to know the status of packages? (HH:MM)')
        searchTime = datetime.datetime.strptime(input(), '%H:%M').time()
        for i in (range(1, (packageHashTable.size + 1))):
            testPackage = (packageHashTable.find(i))
            if testPackage.enrouteStartTime < searchTime < testPackage.deliveryTime:
                testPackage.deliveryStatus = 'en route'
            elif searchTime > testPackage.deliveryTime:
                testPackage.deliveryStatus = 'delivered'
            else:
                testPackage.deliveryStatus = 'at the hub'

        for i in (range(1, 41)):
            testPackage = (packageHashTable.find(i))
            if testPackage.deliveryStatus == 'delivered':
                print(
                    "{} {} {: <20} {} {} {} {} {} {} ".format(testPackage.packageID, testPackage.address,
                                                              testPackage.city,
                                                              testPackage.state, testPackage.zipCode,
                                                              testPackage.deliveryDeadline, testPackage.mass,
                                                              testPackage.deliveryStatus, testPackage.deliveryTime))
                print()

            else:
                print(
                    "{} {} {: <20} {} {} {} {} {} ".format(testPackage.packageID, testPackage.address, testPackage.city,
                                                           testPackage.state, testPackage.zipCode,
                                                           testPackage.deliveryDeadline, testPackage.mass,
                                                           testPackage.deliveryStatus))
                print()

    else:
        print('Goodbye.')
        exit()
