A Generative AI product usually has the following layer:
1. API Layer
2. Database Layer(Vector, SQL, NoSQL)
3. RAG Layer
4. Agent Layer(Langchain, Langgraph, Autogen, n8n)
5. MCP
6. Agent to Agent(a2a)
7. Model Finetuning
8. Model Inferencing
9. Gen AI on cloud
10. LLMOPS

System setup:
Python, vscode, cursor, jupyter notebook, postman

What is an API ?
(i) Definition: Application Programming Interface - enables communication between different software systems.
(ii) Importance: APIs are fundamental to modern software, allowing applications to exchange data and functionality.
(iii) Real-world examples: UPI transactions, e-commerce platforms, mapping applications, and the Your Own AI platform.
(iv) API's role in heterogeneous systems: APIs provide a standardized way for systems built with different technologies to interact.
(v) API as a set of rules: APIs define a set of rules for exposing functions and data over the internet, typically using HTTP/HTTPS.
(vi) Request-response mechanism: APIs operate on a request-response model, where a client sends a request to a server, and the server returns a response.

Monolithic V/S Microservice Architecture:

Monolithic: Everything inside an application is binded into one single file. Like Business Logics, APIs, Authentication, Database Access. Example: app.py
Microservices: Everything inside an application is divided into different different independent services. Like each service might have its own logic,
	       own DBs, deployed independently and communicate via APIs. Example: user_service.py, orders.py

Use the "pip show" command to check the version of the libraries you are using in your current project.
For example:
pip show fastapi, pip show uvicorn etc.

Difference between GET and POST:

GET:
	1.) Used to fetch data; Data is sent via URL; Can be accessed directly in a browser.
	2.) Example: https://api.example.com/users?id=10
		Here:
			id=10 is sent in the URL
			You can paste this URL in a browser and hit Enter

POST:
	1.) Used to send data to server (create/update).
	2.) Data is sent in the request body, not URL.
	3.) Cannot be triggered just by typing a URL in browser.
	4.) You cannot hit a POST API call through a URL like the GET API, you need to use POSTMAN or request libraty(python) for POST API call.
	5.) The new entry you are sending through a post call is temporary, and to make the entry permanent, you need to get a persistent storage like a database.