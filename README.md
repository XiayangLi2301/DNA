[![PythonVersion](https://img.shields.io/badge/python-3.7-blue)](https://img.shields.io/badge/python-3.7-blue)

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Requirements](#requirements)
- [Usage](#usage)
    - [Introduction](#introduction)
    - [Quick-start](#quick-start)
- [Lisence](#license)
## Background

DNA-LC is a coding schema called DNA-LC, which converts binary sequences into DNA base sequences satisfying the constraints of GC content and homopolymer. Furthermore, compared with other methods aimed at one single error correction within a strand, our encoding mode enables the detection and correction of multiple errors and owns a higher error correction capability. Relevant details can be found in our paper under review.

## Install

You can install it from the source.

> git clone https://github.com/XiayangLi2301/DNA.git

## Requirements

numpy==1.20.3

scipy==1.7.1

matplotlib==3.4.3

## Usage

### Introduction

- **DNA_LC**
    - **silico.py**: Generate the simulation sequences required for the experiment. 
    - **tool.py**: Provide some functions used for error-correction in DNA-LC code.
    - **co_single.py**: Contains the algorithm to correct the single error.
    - **encode.py**: The encoding for DNA-LC.
    - **main.py**: Contains the main program: including error correction and calculation of error correction rate.
    - **HEDGES.py**: Contains the main program: including error correction and calculation of error correction rate in HEDGES code.

- **test** : Six drawing files included.
- **perform** : Some experiment results included.
    - **data** : Some experiment datas included.
    - **figure** : Some experiment figures.

### Quick-start:

- You need run main.py in DNA_LC to test the performance of DNA-LC code. During operation, you will receive the following execution prompt once:

    - **the type of error that occurred.**(We provide three types)

    1. all three errors
    2. deletions
    3. inconsecutive deletions

    - **the length of message squence** (positive integer, special conditions)

    - **the number of simulations** (positive integer)

    - **the rate of errors(sub.,ins.,del.)** (If you choose 1 in QUESTION 1, decimal between 0 and 1)

    - **the number of (inconsecutive deletions)**(If you choose 2 or 3 in QUESTION 1, positive integer)

- You need to run Hedges.py to test the performance of HEDGES code. In addition to the above input command, you may also need to enter new parameters according to the following command:
    - **the correct penalty**: A greediness parameter that mitigates the tendency of the heap to expand exponentially. (negative real number)
    - **the runout bytes**: The message zeros padded in each strand of encoding. (positive integer, usually 1 or 2.)

**Note**: 

(1) We only provide an entry for the simulation experiment. If you need to correct errors in a specific scenario, you need to use the functions in main.py and Hedges.py separately.

(2) **The random seeds** for all our random experiments (generating sequences or generating errors) is 0. You can get more details by looking at the functions in **silico.py**.

(3) HEDGES code may contains more hyperparameters, but in our experimental setting, we mainly focus on **the correction penalty**. 

(4) Our main reference for the experimental code of HEDGES Code:
> https://github.com/whpress/hedges

> https://github.com/HaolingZHANG/pyHEDGES

## License

© Xiayang Li, TianJin University
