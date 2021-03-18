# 3430-extra-credit

## Description
The goal of this program is to place the least amount of cell base stations where each house is within four miles of one station to allow cell service. The program generates a new random list of 30 numbers, each to represent a house and it's distance in miles from the easten endpoint. By working with randomly generated distances the algorithm will produce different amounts for the minimum number of bases needed. 

## Method
Given the list of house distances, the first step is to sort it. Once we have the list of houses sorted by distance, we place our first base station four miles 'west' of the first house. We then take the distance of the first home + four miles and store it into our base_station variable, then increment the number of bases by one. After placing our first station, starting with the second element in the list of houses, loop through each house until the absolute value of distance of current house - base_station mile marker is greater than four. After reaching a house that meets this requirement, place a new base station four miles west and increment the number of bases. Base_station now becomes current house distance + four miles. Upon completion of the loop, we will have the minimum number of bases needed to cover all houses. 

## Requirements
No additional requirements are necessary to run the program. 

# User Manual
## Step 1 - Select 'Download ZIP' from the GitHub link above
![image of zip](https://github.com/hansonbriley/3430-extra-credit/blob/main/images/zip.jpg)
## Step 2 - Extract contents to a folder

## Step 3 - Navigate to folder and run with 'python main.py'
![navigate and run](https://github.com/hansonbriley/3430-extra-credit/blob/main/images/nav-run.JPG)
