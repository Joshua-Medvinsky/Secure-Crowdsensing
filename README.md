# Secure-Crowdsensing

This capstone project involved using crowdsensing is to obtain information on the noise levels of the campus and utilizing the blockchain to keep user data safe. An application was created to allow the user to report the location and level of noise that they observed. The next obstacle was to find a practical way to store this data within the blockchain.


There are several risks with storing information on the blockchain, if there are vulnerabilities within the contract it is easy to exploit. The source code on the blockchain is publicly accessible and viewable by anyone. It is also very expensive to store large amounts of user data within the blockchain. It is far more practical to store the information offline in a Merkle Tree but protect its integrity by storing the hash in the blockchain.
 
 
 To overcome I implemented a Merkle tree to store user data. The location data is stored in the leaf of the tree, and only the root hash is stored in the contract.  The contract can be used to verify that any leaf data (if presented with Merkle proof) can be verified by the contract that it is part of the authorized Merkle tree (i.,e and was not forged). The above approach enables anyone to verify the integrity of the data set (via merkle proof and root hash on contract), while mitigating any storage cost, and exposure of the dataset.

See the collection.py file to launch the noise data collection app, in the repository are images of the application when launched
