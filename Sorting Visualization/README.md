## Sorting Visualization 

![](<https://img.shields.io/badge/python3-passing-brightgreen.svg>)
![](<https://img.shields.io/badge/Video%20record-support-brightgreen.svg>)
![](<https://img.shields.io/badge/Sound-support-brightgreen.svg>)
![](<https://img.shields.io/badge/Sparse%20data-support-brightgreen.svg>)
![](<https://img.shields.io/badge/Resampling%20data-support-brightgreen.svg>)

There are various types of sorting algorithms and it is very difficult to understand their working without visualization.
Hence we decided to visualize these sorting algos in python with the help of matplotlib.animations

Pro tip :- Time complexity can also be seen through these visualizations

## Introduction

This repository is a demo of visualizing 8 types of Sorting Algorithms. It aims to make Sorting Algorithms easier for programmers to understand. Also, you can see the difference of Time Complexity between different sorting algorithms.

| Sorting Algorithm | AverageTime Complexity | Bad Time Complexity | Stability |
| ----------------- | ---------------------- | ------------------- | --------- |
| Bubble Sort       | O(N^2)                 | O(N^2)              | YES       |
| Insertion Sort    | O(N^2)                 | O(N^2)              | YES       |
| Shell Sort        | O(N^5/4)               | O(N^2)              | NO        |
| Selection Sort    | O(N^2)                 | O(n^2)              | NO        |
| Heapify Sort      | O(NlogN)               | O(NlogN)            | NO        |
| Merge Sort        | O(NlogN)               | O(NlogN)            | YES       |
| Quick Sort        | O(NlogN)               | O(N^2)              | NO        |
| Count Sort        | O(N)                   | O(N)                | YES       |



## Dependencies

- python3.x
- matplotlib
- pygame

## Quick Start

0. Check all dependencies installed

      This command can help you install all the dependent packages

      `pip install -r requirements.txt`
      
2. Start sorting.py

   `python3 sorting.py`

   - `Enter the number of elements:`: choise a number
   - `Choose algorithm:`: Sorting Type. Choose one
	 1.Bubble 
	 2.Insertion 
	 3.Quick 
	 4.Selection 
	 5.Merge Sort 
	 6.Heapify 
	 7.Shell 
	 8.Count sort
	 
3. Start sorting.py

   `python3 QuickSort.py`

   - `Press “Enter” key:`: to Perform Visualization.
   - `Press “R” key:`: to generate new array.
      
#### All sortings are done on randomly generated arrays of size 30.

### Bubble Sort
Total operations = 435 

![bubble](https://f.top4top.io/p_1743devrw1.gif)

### Selection Sort
Total operations = 460

![selection](https://g.top4top.io/p_1743jlpcp2.gif)

### Insertion Sort
Total operations = 230

![Insertion](https://h.top4top.io/p_1743xxqrn3.gif)

### Quick Sort
Total operations = 131

![quick](https://i.top4top.io/p_1743rf4xy4.gif)

another sorting algorithm visualization using pygame 

![quick](https://i.top4top.io/p_1743ghv4d1.png)
### Merge Sort
Total operations = 177

![merge](https://j.top4top.io/p_1743bj4815.gif)
