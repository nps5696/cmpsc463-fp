# Introsort Algorithm, CMPSC-463 Final Project
![pylint](https://img.shields.io/badge/pylint-9.04-yellow?logo=python&logoColor=whitehttps://img.shields.io/badge/pylint-9.04-yellow?logo=python&logoColor=whitehttps://img.shields.io/badge/pylint-9.04-yellow?logo=python&logoColor=whitehttps://img.shields.io/badge/pylint-9.04-yellow?logo=python&logoColor=white)
## Implementing hybrid sorting algorithms
### 
 For this project I am going to implement Introsort algorithm. The algorithm relies on Quicksort and Heapsort. 

#### These are the key points for the project:

- Implement Introsort
- Add Unit Tests
- Run Performance Analysis

## Quicksort and Introspective Sort Prformance Comparison

Quicksort has big disadvancage for the cases where it is picking left most or right most element, redurcing its complexity to O(n^2). Intospective sorting algorithm utilizes heapsort for the cases such this. Let's look at the sorting time performance graph:

![introsort vs quicksort run time](https://github.com/nps5696/cmpsc463-fp/blob/develop/img/intospective_vs_quicksort.png)
