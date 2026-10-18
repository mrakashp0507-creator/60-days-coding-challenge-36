# Day 36 – Futuristic Reservoir Optimizer

## Overview

A Python implementation of the **Container With Most Water** problem using brute-force enumeration and an optimized two-pointer technique.

The goal is to select two walls that maximize the water area between them.

## Problem Statement

Given a list of non-negative wall heights, choose two walls that can hold the maximum amount of water.

The area is calculated using:

`area = min(height[left], height[right]) * (right - left)`

### Example

**Input**
```text
[1, 8, 6, 2, 5, 4, 8, 3, 7]
```

**Output**
```text
49
```

The optimal walls have heights 8 and 7, with a width of 7.

## Approaches

### 1. Brute Force

- Check every pair of walls.
- Calculate the area for each pair.
- Track the maximum area.

Time complexity: **O(n²)**  
Auxiliary space: **O(1)**

### 2. Two-Pointer Optimization

- Initialize one pointer at each end.
- Calculate the current container area.
- Update the maximum area.
- Move the pointer at the shorter wall inward.
- Repeat until the pointers meet.

Time complexity: **O(n)**  
Auxiliary space: **O(1)**

## Why Move the Shorter Wall?

The shorter wall limits the water height. Moving the taller wall inward reduces the width without increasing the height limit. Moving the shorter wall creates an opportunity to find a taller boundary.

This greedy strategy eliminates unnecessary candidate pairs while preserving the optimal answer.

## Features

- Brute-force solution for comparison
- Optimized two-pointer implementation
- Pointer movement visualization
- Runtime measurement
- Result verification
- Input validation

## How to Run

Requirements: Python 3.

Run the script:

```bash
python day36_container_with_most_water.py
```

Enter non-negative integer heights separated by spaces.

## Real-World Connections

The algorithm demonstrates optimization under competing constraints, such as width versus capacity. Its broader lesson is useful in resource-allocation and infrastructure-planning problems, although this specific formula is a mathematical model rather than a complete reservoir-engineering design.

## Learning Outcomes

- Applied the two-pointer technique.
- Compared quadratic and linear algorithms.
- Explained a greedy optimization rule.
- Visualized pointer movement.
- Measured and verified algorithm outputs.

**Day 36 Status:** Completed – Two Pointer Optimization.
