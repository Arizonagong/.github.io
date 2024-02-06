---
marp: true
paginate: true
class:
  - invert
---
# **VScode and Python**
## Day1: Why VScode and Why Python

Dr. Byoung-gyu Gong
Assistant professor 
Information System
Davide Eccles Business School
University of Utah Asia Campus

---
# Contents
- Introduction
- Overview
--Python
--IDE: VScode
- What can we do with Python

---
Hello world
```python
print("hello world")
1+1=2


```

---
# Introduction

---
# Who am I?

**Byoung-gyu Gong**

- Current: Assistant professor of Information System(U of U Asia Campus)

- Former Data Scientist
At the Sorenson Impact Center

[profile](https://asiacampus.utah.edu/faculty-directory/5992/)
[portfolio: Maps project](https://www.mapsproject.org/)
![bg right 80%](img/profile.png)


---
# Overview

---
## **What is Scripting Language?**
Scripting language is for computation or programming to build application. There are a bunch of different scripting language.

![bg left 80%](img/script.png)

---
![bg left](img/python_logo.png)

# **Why Python**

## **1. Popularity**
Python is the most popular and fastest growing programming language in the world.

1. [IEEE Global Ranking](https://spectrum.ieee.org/top-programming-languages-2022#toggle-gdpr)
2. [Github Global Ranking](https://madnight.github.io/githut/#/pull_requests/2023/2)
3. [TIOBE Index](https://www.tiobe.com/tiobe-index/)

---
![bg right](img/python_coding.png)
## **2. Quality**
Python emphasizes 'readability' thus much more maintainable and scalable. 

---
## **2. Quality**
### 2.1. **OOP**: 
It adopts a philosophy of object-oriented programming(OOP), making the code more intuitive and easy to understand.
![bg 100% left:50%](img/oop.png)

---
## **2. Quality**
### 2.2. **Brevity**: 
- Python achieves functionality and desired output with smallest chunck of code.

![bg 90% right:50%](img/python_short.png)

---
## **2. Quality**
### 2.2. **Brevity**:

- Python code is typically one-third to one-fifth the size of equivalent C++ or Java code. That means there is less to type, less to debug, and less to maintain after the fact.
![bg 100% left:50%](img/c_comp.png)

---
## **3. Versatility**
- Python supports a bunch of predefined and packaged libraries created and maintained by a number of expert users globally. 


![width:1000px contain](img/python_libraries.png)

---

## What is IDE?
IDE means Integrated Development Environment, which provide a number of convenience tool packages to support programming and coding.

Examples: 
- Sublime Text
- VIM
- Xcode
- Eclipse
- NetBeans
- IntelliJ IDEA
![bg 100% right](img/IDE.png)

---
# **Why VScode**

## **1. Accessibility**
- VScode is free and readily available through simple download from the web. 
- There is no limit to use all supporting functionality for the users.
- But, its one of the competitor, Pycharm is not 100% free.

![bg 100% left](img/pycharm.png)

---
## **2. Versatility**
- VScode IDE supports almost all kinds of scripting language and allow integration for the single product development.
- But, still majority of IDE's support single script language for the programming and development.
![bg 100% right](img/vscode_ver.gif)

---
## **3. Convenience**
- Auto completion function is evolving fast, and the MS backed VScode is the forerunner of this field. 
- They recently added new service called 'copilot' powered by their strong ChatGPT. 
- It will be the game changer of programming in the future and without the copilot, it will not be available to do coding.

![bg 100% vertical left](img/copilot.gif)
![bg 100% left](img/copilot_natural.gif)

---

# What can we do with Python?

---
## Data Visualization

[Plotly Dashboards](https://plotly.com/examples/dashboards/)
![bg 100% vertical right](img/plotly.png)

[Vega Altair](https://altair-viz.github.io/)
![bg 100% right](img/vega_altair.png)

---

## Automated Programs
[Resume Builder & Parser](https://github.com/xitanggg/open-resume)
![bg 100% vertical right](img/resume.png)
[Image Recognition](https://github.com/anujdutt9/Handwritten-Digit-Recognition-using-Deep-Learning)
![bg 100% vertical right](img/handwriting.png)

---

## Artificial Intellgence
[Scikit-Learn](https://scikit-learn.org/stable/)
![bg 100% vertical right](img/scikit.png)
[Plotly AI](https://scikit-learn.org/stable/)
![bg 100% vertical right](img/plotly_ai.png)

---

## Best Web Applications Built by Python

1. **Facebook**: 21% of its code is run by Python
2. **Instagram**: It was built and run 100% by famous Python web framework called Django.
3. **Spotify**: It uses python for backend development and data analytics for the recommendation system.
4. **Netflix**: They use Python for their recommendation system.
5. **Reddit**: In 2015, they engirely migrated their code to Python from Lisp.

---

# **VScode and Python**
## Day1: Why VScode and Why Python
## Day1: VScode and Python set-up

Dr. Byoung-gyu Gong
Assistant professor 
Information System
Davide Eccles Business School
University of Utah Asia Campus

---

# Environment Structure

---

# **Global Environment**

Global Environment means your entire python program installed in your single computer. Once you work in the global environment and install libraries, then it will be downloaded all across the local environment. 
- **Warning**: It can make your computation seriously slow.

![bg 100% vertical right](img/global_env.png)

---
# **Local Environment**

Local Environment indicates subset of your entire Python program. It is usually limited to your folder. Once you install specific libraries for your local environment, then it will be only installed to your local environment.

- **Warning**: If you use the local environment, then it cannot interact with the other local environments as they are isolated from each others.

![bg 100% vertical right](img/local_env1.png)

---

# **Local Environment**
## **1. Virtual Environment**
One of the local environments is **virtual environment** and presented as '.venv'. 
** We will use 'virtual environment' for your class

## **2. Conda Environment**
One of the local environments is **Conda environment** and presented as '.conda'.

---

# Activitiy

## What do you want to make or build with Python?

## What is your future dream project when you get high level Python coding skills?

---

# Review
- Introductino
- Overview
--Python
--IDE: VScode
- What can we do with Python
- Environment Structure
-- Global Environment
-- Local Environment