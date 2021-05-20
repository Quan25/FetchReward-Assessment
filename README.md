# FetchReward-Assessment
Develop an automation program that takes a YAML configuration file as input and deploys a Linux AWS EC2 instance with two volumes and two users.

#### How to run ####
1. Clone this repository
2. Create an virtual environment for this project and get into it ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/1.png)
4. Install essential packages
- boto3
  ```
  pip3 install boto3
  ```
4. Login to [AWS Console](https://console.aws.amazon.com/)
5. Go to [AWS IAM](https://console.aws.amazon.com/iam/home)
6. On left side, click on `Users` and then click on `Add User` 
![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/2.png)
7. Choose a username for the user and check `Programmatic access` ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/3.png)
8. Add `AmazonEC2FullAccess` for this user as shown below ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/4.png)
9. Type as shown for this one ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/6.png)
10. The next page should be the same as this one ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/7.png)
11. Go to terminal and enter `aws configure`, and copy and paste the credentials from step 10 ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/8.png)
12. check if all the info is entered with
```
aws configure list
```
![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/10.png)
14. On search, type `key` and choose `key pairs` ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/14.png)
15. Then, create a key pair as shown ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/15.png)
16. Go back to your terminal and type 
```
chmod 400 ec2-keypair.pem
```
![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/8.png)
17. Now that we can run the python script to create ec2 instance 
```
python3 createInstance.py
```
#### check if the instances have been created as required ####

![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/11.png)
![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/13.png)
![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/12.png)
