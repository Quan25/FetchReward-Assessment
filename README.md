# FetchReward-Assessment
Develop an automation program that takes a YAML configuration file as input and deploys a Linux AWS EC2 instance with two volumes and two users.

#### How to run ####
1. Clone this repository
2. Create an virtual environment for this project and get into it
3. Install essential packages
- boto3
  ```
  pip3 install boto3
  ```
4. Login to [AWS Console](https://console.aws.amazon.com/)
5. Go to [AWS IAM](https://console.aws.amazon.com/iam/home)
6. On left side, click on `Users` and then click on `Add User` 
![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/2)
7. Choose a username for the user and check `Programmatic access` ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/3)
8. Add `AmazonEC2FullAccess` for this user as shown below ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/4)
9. Type as shown for this one ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/6)
10. The next page should be the same as this one ![](https://github.com/Quan25/FetchReward-Assessment/blob/main/screenshots/7)
11. 
