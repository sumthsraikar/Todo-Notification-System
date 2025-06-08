#  Todo Notification System (AWS + HTML)

Welcome to **Day 1** of my #14DaysOfProjects challenge!  
This project allows you to send notifications via **Email** or **SMS** using **AWS Lambda**, **Amazon SNS**, and **API Gateway**, with a clean frontend built in HTML and JavaScript.

---


Architecture:
![diagram-export-6-8-2025-5_36_59-PM](https://github.com/user-attachments/assets/8023feb9-6ea8-4364-9ee4-77251e47a410)


---

##  Tech Stack

- **Frontend**: HTML, JavaScript
- **Backend**: AWS Lambda (Python)
- **Notifications**: Amazon SNS
- **API Gateway**: HTTP API

---

##  Features

- Send a message via **Email** or **SMS**
- Choose notification type via dropdown
- Serverless architecture using AWS
- Real-time success/error message handling

---

##  Project Structure
 todo-notification-system\
├── index.html # Frontend form
├── lambda_function.py # AWS Lambda function code
└── sns_instructions.md # Setup guide for SNS, Lambda, and API Gateway


---
  
AWS Backend Setup

🔹 Step 1: Create an SNS Topic
Go to the Amazon SNS Console

Choose Topics > Create topic

Select Standard, and name it todo-web-service-notification

Click Create topic

![Screenshot 2025-06-08 154459](https://github.com/user-attachments/assets/e46d565d-d539-473a-9161-727edc6377a4)


🔹 Step 2: Add Subscriptions
Go to your SNS topic and click Create subscription

Create two subscriptions:

Email: Enter your email → confirm via inbox

SMS: Enter your number with country code (e.g., +91XXXXXXXXXX)

![Screenshot 2025-06-08 154459](https://github.com/user-attachments/assets/a7e08537-3a6f-45d0-ada9-f4f1d2ccdd5c)


🔹 Step 3: Create a Lambda Function
Go to AWS Lambda Console

Click Create function → Author from scratch

Name it: NotificationHandler

Runtime: Python 3.x

Click Create function

Add Permissions:
Under the function, go to Configuration > Permissions

Open the execution role

Attach policy: AmazonSNSFullAccess

![Screenshot 2025-06-08 155444](https://github.com/user-attachments/assets/514a9afc-0292-4e05-aac8-940a80140af5)

🔹 Step 4: Create API Gateway
Go to API Gateway Console

Choose Create API > HTTP API

Name: NotificationAPI

Add a Route
Method: POST

Path: /sendNotification

Integration
Select the Lambda function you created

Deploy the API
![Screenshot 2025-06-08 160100](https://github.com/user-attachments/assets/7dbe01f2-f42c-4517-8b93-198e1145d2b3)


Copy the Invoke URL

🌐 Frontend Setup
🔸 Modify the HTML
Open index.html and update the API endpoint:

javascript
Copy
const response = await fetch('https://<your-api-id>.execute-api.<region>.amazonaws.com/sendNotification', {
🔸 Open in Browser
Just double-click index.html or serve with a local server.

OUTPUT:![Screenshot 2025-06-08 164639](https://github.com/user-attachments/assets/11c09ec3-08ec-4bd4-b35b-51f5f1eda9c7)
![WhatsApp Image 2025-06-08 at 5 43 09 PM](https://github.com/user-attachments/assets/deb24fd4-a6e3-4959-bf7a-db9f44d3b733)

![WhatsApp Image 2025-06-08 at 5 43 10 PM](https://github.com/user-attachments/assets/1716bcbb-7a5f-483c-b9f2-9d4987e5786b)

