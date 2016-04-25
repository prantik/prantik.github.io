---
title: Performance Analysis of Scala List Sort
layout: post 
category: blog
tags: scala list sort performance
year: 2016
month: 4
day: 24
published: true
summary: Performance Analysis of Scala List Sort
image: scala.png
---

The default behavior of the [scala list](http://www.scala-lang.org/api/2.11.7/#scala.collection.immutable.List) sortBy operation is sorting in the ascending order.
To get the descending order, the options are simple a) sortBy with default behavior and then reverse the list or b) provide an explicit ordering function. 

The first option has obvious disadvantages over the second option: O(nlogn) operation followed by another O(n) operation and poor readability aspects; providing explicit ordering function provides reader clarity on expected outcome. To test out the performance, I wrote a simple scala code. 

<script src="https://gist.github.com/prantik/5a1316e1b9a00628075095db0950cf86.js"></script>

Here are the performance results over 25 simulation runs.

|  List Length   |  Mean Difference <br> (in ms)  | Std Dev <br> (in ms) |
| -------------: |----------------:| --------:|
|    100,000     |   -2.0          | 2.81     |
|    200,000     |   -4.0          | 8.67     |
|    300,000     |   -4.0          | 14.09    |
|    400,000     |   -13.0         | 12.15    |
|    500,000     |   -3.0          | 10.46    |
|    600,000     |   -16.0         | 37.20    |
|    700,000     |   -19.0         | 12.30    |
|    800,000     |   -15.0         | 17.14    |
|    900,000     |   -26.0         | 20.15    |
|  1,000,000     |   -17.0         | 20.69    |
|  1,100,000     |   102.0         | 27.85    |
|  1,200,000     |    75.0         | 27.94    |
|  1,300,000     |   106.0         | 31.75    |
|  1,400,000     |   106.0         | 24.59    |
|  1,500,000     |   104.0         | 33.15    |
|  1,600,000     |   144.0         | 49.35    |
|  1,700,000     |   104.0         | 32.93    |
|  1,800,000     |   126.0         | 43.07    |
|  1,900,000     |   142.0         | 45.59    |
|  2,000,000     |   134.0         | 69.49    |
|  2,100,000     |   217.0         | 58.57    |
|  2,200,000     |   215.0         | 48.13    |
|  2,300,000     |   270.0         | 64.25    |
|  2,400,000     |   270.0         | 72.78    |
|  2,500,000     |   278.0         | 54.27    |



For lists of sizes greater than million elements, it becomes obvious that the second option with explicitly provided ordering operator is a better choice. For smaller lists, like the typical ones we interact with on a daily basis in production, either option seems to work well.


