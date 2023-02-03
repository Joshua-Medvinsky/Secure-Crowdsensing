# Secure Crowdsensing
This project involved the development of a cross-platform application in Kivy to securely collect and store noise level information. The focus of this project was to ensure the confidentiality and integrity of user data at rest, utilizing a blockchain and Merkle tree implementation for secure storage.

## Key Features
* A user-friendly cross-platform app for reporting noise levels and locations.
* An algorithm for processing collected noise levels in Python.
* A secure blockchain and Merkle tree implementation to store user data, ensuring confidentiality and integrity of data at rest.
* A cost-effective solution for large scale data storage, as only the root hash of the Merkle tree is stored on the blockchain.

## Usage
To launch the noise data collection app, see the collection.py file in the repository. The repository also includes images of the application when launched.

A user can submit noise information by using the app as follows:

1. Input the location and level of noise they observed.
2. The location data is stored in the leaf of the Merkle tree.
3. The root hash of the Merkle tree is stored on the contract in the blockchain.
4. The contract can be used to verify the integrity of the data set with a Merkle proof and root hash.
## Conclusion
This project provides a secure and cost-effective solution for collecting and storing noise level information, while maintaining the confidentiality and integrity of user data. The implementation of the blockchain and Merkle tree ensures that the information can be easily verified and is protected from any potential vulnerabilities.

###### Below is an example of how a user would submit noise information on the application.

![image](https://user-images.githubusercontent.com/76570188/192072960-6333b3fa-022e-4fa7-8173-575fd80a038f.png)
![image](https://user-images.githubusercontent.com/76570188/192072964-3d271cf8-1002-49f1-9ebd-e013cdd1f5e3.png)
![image](https://user-images.githubusercontent.com/76570188/192072967-eba3b7b1-4dc6-4e0d-ab46-47a20d8e2f35.png)
![image](https://user-images.githubusercontent.com/76570188/192072968-586c0191-39ed-46b2-8af6-be52ce37688b.png)
