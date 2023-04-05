# Fintech_Module18

![blockchain](https://github.com/nielsdehaan1977/Fintech_Module18/blob/main/Images/blockchain_tech.jpg)
---
# Blockchain based ledger system in streamlit
---
## This python code can be utilized as an app by running Streamlit. The app provides a user friendly web interface for a blockchain based ledger system. This ledger allows to conduct financial transactions and to verify the integrity of the data in the ledger. 

---
## pychain.py
---
### This application was built to provide both ### TO BE ADDED

---
The tool can help 

* The tool goes through the following steps:

* Add Block to Blockchain
* Update PyChain Ledger
* Increase Block hashing difficulty option
* Block inspection option
* Validate Chain option

---
## Table of Content

- [Tech](#technologies)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Contributor(s)](#contributor(s))
- [License(s)](#license(s))

---
## Tech

This project leverages python 3.9 with the following packages:
```
`Python 3.9`
```
* [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) - Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

* [streamlit](https://streamlit.io/) - Streamlit is an open-source Python library that makes it easy to create and share, custom web apps for machine learning and data science.

---

## Installation Guide

### Before running the application first install the following dependencies in either Gitbash or Terminal. (If not already installed)

#### Step1: Activate dev environment in Gitbash or Terminal to do so type:
```python
    conda activate dev
```
#### Step2: install the following libraries (if not installed yet) by typing:
```python
    pip install pandas
    pip install streamlit

 ```
#### Step3: Start python file with RUN Streamlit
Streamlit can be started by:
1. Activate your developer environment in Terminal or Git Bash (already done in step 1)
2. Form the location where you cloned the github repository folder, type: ***Streamlit run pychain.py***

![streamlit](https://github.com/nielsdehaan1977/Fintech_Module18/blob/main/Images/streamlit_start.jpg)


## Usage

* Add Block to Blockchain
in the Store a Transaction Record in the PyChain section of the streamlit app you can input the following data: to replicate a blockchain transaction. 
- sender: Person who sends something
- receiver: Person who will receive something
- amount: the amount that is exchanged
Once you press Add Block the data will be added once the hash puzzle is solved. 

(Below screenshot shows the blockchain consisting of several blocks)
![adding_blocks](https://github.com/nielsdehaan1977/Fintech_Module18/blob/main/Images/streamlit4.4.1.jpg)

* Update PyChain Ledger
Once the hash puzzle is solved the block will be added to the existing PyChain ledger. 
The record shows: 
1. Record, in this case sender, receiver and amount information
2. Creator_id
3. Hash of previous block linking the new block to the previous block
4. Timestamp of block being added to the ledged
5. Nonce of the block

* Increase Block hashing difficulty option
This streamlit app provides you with the option to increase the difficulty of solving the hash puzzle, by providing a slider on the sidebar, where you can increase the starting 0's of the hash from 1 (easiest) to 5 (hardest) (with standard value 4). 





* Block inspection option

* Validate Chain option

(Below screenshot shows the blockchain validation)
![adding_blocks](https://github.com/nielsdehaan1977/Fintech_Module18/blob/main/Images/streamlit4.4.2.jpg)


## Contributor(s)

This project was created by Niels de Haan (nlsdhn@gmail.com), Jason Steiner (jason.steiner@richmond.edu), Marc Pocorni (

---

## License(s)

MIT