# PyChain Ledger
################################################################################
# You’ll make the following updates to the provided Python file for this
# Challenge, which already contains the basic `PyChain` ledger structure that
# you created throughout the module:

# Step 1: Create a Record Data Class
# * Create a new data class named `Record`. This class will serve as the
# blueprint for the financial transaction records that the blocks of the ledger
# will store.

# Step 2: Modify the Existing Block Data Class to Store Record Data
# * Change the existing `Block` data class by replacing the generic `data`
# attribute with a `record` attribute that’s of type `Record`.

# Step 3: Add Relevant User Inputs to the Streamlit Interface
# * Create additional user input areas in the Streamlit application. These
# input areas should collect the relevant information for each financial record
# that you’ll store in the `PyChain` ledger.

# Step 4: Test the PyChain Ledger by Storing Records
# * Test your complete `PyChain` ledger.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################
# Step 1:
# Create a Record Data Class

# Define a new Python data class named `Record`. Give this new class a
# formalized data structure that consists of the `sender`, `receiver`, and
# `amount` attributes. To do so, complete the following steps:
# 1. Define a new class named `Record`.
# 2. Add the `@dataclass` decorator immediately before the `Record` class
# definition.
# 3. Add an attribute named `sender` of type `str`.
# 4. Add an attribute named `receiver` of type `str`.
# 5. Add an attribute named `amount` of type `float`.
# Note that you’ll use this new `Record` class as the data type of your `record` attribute in the next section.


# @TODO
# Create a Record Data Class that consists of the `sender`, `receiver`, and
# `amount` attributes
@dataclass
class Record:
    sender: str
    receiver: str
    amount: float


################################################################################
# Step 2:
# Modify the Existing Block Data Class to Store Record Data

# Rename the `data` attribute in your `Block` class to `record`, and then set
# it to use an instance of the new `Record` class that you created in the
# previous section. To do so, complete the following steps:
# 1. In the `Block` class, rename the `data` attribute to `record`.
# 2. Set the data type of the `record` attribute to `Record`.

# Creating the Block data class
@dataclass
class Block:

    # @TODO
    # Rename the `data` attribute to `record`, and set the data type to `Record`
    record: Record

    # Include creator id, previous hash, current timestamp and nonce
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    # define function to define hashing of block
    def hash_block(self):
        # Create an instance of the sha256 hashing function
        sha = hashlib.sha256()

        # Encode the data using the encode function
        record = str(self.record).encode()
        # hash it
        sha.update(record)

        # encode creator id
        creator_id = str(self.creator_id).encode()
        # hash it
        sha.update(creator_id)

        # encode timestamp
        timestamp = str(self.timestamp).encode()
        # hash it
        sha.update(timestamp)

        # encode previous hash
        prev_hash = str(self.prev_hash).encode()
        # hash it
        sha.update(prev_hash)
        
        # encode nonce
        nonce = str(self.nonce).encode()
        # hash it
        sha.update(nonce)

        # Return the hash to the rest of the Block class
        return sha.hexdigest()

# Create a data class called Pychain
@dataclass
class PyChain:
    # The class PyChain holds a list of blocks
    chain: List[Block]
    
    # Setup difficulty level for hashing
    difficulty: int = 4

    # define proof of work function 
    def proof_of_work(self, block):
        
        # set calculated hash variable as block.hash_block
        calculated_hash = block.hash_block()

        # multiply the difficulty level set times the amount of 0s the hash has to begin with
        num_of_zeros = "0" * self.difficulty

        # do the proof of wokr calculations till you find the solution
        while not calculated_hash.startswith(num_of_zeros):
            
            # update nonce value
            block.nonce += 1
            # return the block with the updated nonce value
            calculated_hash = block.hash_block()

        # print winning hash with the calculated hash value
        print("Wining Hash", calculated_hash)
        # once solution found return block
        return block

    # Once solution found, add block to blockchain
    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    # chekc if blockchain is still valid
    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        # run for loop to check if the hash of the previous block matches the prev_block value in the current block. 
        for block in self.chain[1:]:
            # if they don't match, the loop will immediately return False to alert us that the blockchain is invalid. 
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False
            # calculate the hash of the current block and store it in block_hash.
            block_hash = block.hash_block()

        # print that blockchain is valid if prvious block hash matches the prev_block value in the current block
        print("Blockchain is Valid")
        return True

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit
@st.cache_resource()
# define setup function
def setup():
    # print initialziing chain
    print("Initializing Chain")
    # start with the geneisis (first) block (zero value)
    return PyChain([Block("Genesis", 0)])

# print below strings
st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

# startup pychains blockchain starting with genesis block
pychain = setup()

################################################################################
# Step 3:
# Add Relevant User Inputs to the Streamlit Interface

# Code additional input areas for the user interface of your Streamlit
# application. Create these input areas to capture the sender, receiver, and
# amount for each transaction that you’ll store in the `Block` record.
# To do so, complete the following steps:
# 1. Delete the `input_data` variable from the Streamlit interface.
# 2. Add an input area where you can get a value for `sender` from the user.
# 3. Add an input area where you can get a value for `receiver` from the user.
# 4. Add an input area where you can get a value for `amount` from the user.
# 5. As part of the Add Block button functionality, update `new_block` so that `Block` consists of an attribute named `record`, which is set equal to a `Record` that contains the `sender`, `receiver`, and `amount` values. The updated `Block`should also include the attributes for `creator_id` and `prev_hash`.

# @TODO:
# Delete the `input_data` variable from the Streamlit interface.
#input_data = st.text_input("Block Data")

# @TODO:
# Add an input area where you can get a value for `sender` from the user.
sender_data = st.text_input('sender')

# @TODO:
# Add an input area where you can get a value for `receiver` from the user.
receiver_data = st.text_input('receiver')

# @TODO:
# Add an input area where you can get a value for `amount` from the user.
amout_data = st.number_input('amount')

# if button is pressed continue with below code
if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # @TODO
    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`,
    # and `amount` values
    new_block = Block(
        record = Record(sender_data,receiver_data,amout_data),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    # add blcok to the blcokchain
    pychain.add_block(new_block)
    st.balloons()

################################################################################
# Streamlit Code (continues)

# print below string
st.markdown("## The PyChain Ledger")

# define pychain df as dataframe and print it
pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

# give option to increase difficulty of hashing by changing the slider
difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

# give option to select one of the blocks of the blockchain to see the input values
st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

# show the values of the selected block
st.sidebar.write(selected_block)

# give option to validate chain by pressing button
if st.button("Validate Chain"):
    st.write(pychain.is_valid())

################################################################################
# Step 4:
# Test the PyChain Ledger by Storing Records

# Test your complete `PyChain` ledger and user interface by running your
# Streamlit application and storing some mined blocks in your `PyChain` ledger.
# Then test the blockchain validation process by using your `PyChain` ledger.
# To do so, complete the following steps:

# 1. In the terminal, navigate to the project folder where you've coded the
#  Challenge.

# 2. In the terminal, run the Streamlit application by
# using `streamlit run pychain.py`.

# 3. Enter values for the sender, receiver, and amount, and then click the "Add
# Block" button. Do this several times to store several blocks in the ledger.

# 4. Verify the block contents and hashes in the Streamlit drop-down menu.
# Take a screenshot of the Streamlit application page, which should detail a
# blockchain that consists of multiple blocks. Include the screenshot in the
# `README.md` file for your Challenge repository.

# 5. Test the blockchain validation process by using the web interface.
# Take a screenshot of the Streamlit application page, which should indicate
# the validity of the blockchain. Include the screenshot in the `README.md`
# file for your Challenge repository.
