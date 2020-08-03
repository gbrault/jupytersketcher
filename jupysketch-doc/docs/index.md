# Welcome to Jupyter Sketcher Documentation

[![](images/github_small.png)](https://github.com/gbrault/jupytersketcher)

## Problem solved

When you need to solve a mechanical problem, sooner or later you are going to sketch a figure to capture problem's parameters and variables.

The better documented, the easier the problem is to resolve for the designer, and the easier it is for others to understand how it is actually solved.

What if you could capture this in the program solving the problem and use it as a repository for all definitions and physical variables?

This is what jupytersketcher (name of pysketcher module) is proposing to solve.

Of course, this makes even more sense when using Jupyter notebooks, because as a sketch not only the image of the solved problem can be displayed, but the dictionary of all variables processed in the notebook for solving physics is used to draw the image and at the same time to solve the equations of motion.

jupytersketcher is another small step to help building reusable science.

## Getting Started

You can use the binder link in jupytersketcher Github to see some experiments with pysketcher. 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gbrault/jupytersketcher.git/master?filepath=notebooks%2FDryFriction.ipynb)

## pysketcher features

* Drawing sketches on a matplotlib widget for Jupyter Notebook server or Lab
* Defining a yaml based "grammar" to define sketches and simplify reuse
* Animating sketches within Jupyter notebooks

## Main benefit

With Pysketcher for Jupyter mechanical notebooks, you get a single copy of the description of the problem which is as well a space to simulate the system behaviour
