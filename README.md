<div align="center">

# 🧠 ShopMind AI Product Recommendation Engine

### AI-Powered Personalized Product Recommendation System using Django, Generative AI Concepts, and Rule-Based Reasoning

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-Web%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/Generative%20AI-Recommendation%20Logic-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/E--Commerce-Product%20Discovery-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Portfolio%20Project-success?style=for-the-badge"/>

---

### Turning User Behavior Into Smarter Product Recommendations

</div>

---

## 📌 Overview

**ShopMind AI Product Recommendation Engine** is a Django-based e-commerce recommendation system that uses product data, user interaction tracking, and AI-inspired reasoning logic to generate personalized product suggestions.

The project demonstrates how an e-commerce platform can move beyond static product listings and provide users with more relevant recommendations based on browsing behavior, product engagement, and recommendation rules.

This project is built as a **portfolio-friendly Generative AI and Knowledge Representation project**, combining backend development, recommendation logic, user behavior tracking, and e-commerce workflow design.

---

## 🎯 Problem It Solves

Traditional e-commerce platforms often show the same products to every user, regardless of their interest or behavior.

This creates problems such as:

- Poor product discovery
- Low personalization
- Irrelevant product suggestions
- Weak user engagement
- Manual product filtering by users

ShopMind improves this by using user interaction data and recommendation logic to suggest products that are more relevant to each user.

---

## ✨ Key Features

### 👤 User Management

- User registration
- Login and authentication flow
- Session-based user interaction tracking
- Personalized user experience foundation

### 🛍️ Product Management

- Product catalog structure
- Product images and details
- Dynamic product listings
- Product category and metadata handling
- CSV-based product data support

### 🤖 Recommendation Engine

- Personalized product recommendation logic
- User click and interaction tracking
- Product behavior analysis
- Rule-based recommendation flow
- AI-inspired product ranking
- Recommendation generation based on user activity

### 📊 Interaction Analytics

- Tracks user product clicks
- Stores interaction data
- Supports behavior-based recommendation improvement
- Helps understand user interest patterns

### 🎨 E-Commerce Interface

- Product browsing pages
- Product detail pages
- Cart-related interface structure
- Responsive HTML, CSS, and JavaScript frontend
- Product discovery user flow

---

## 🧠 Recommendation Logic

The recommendation engine uses a combination of:

- Product dataset information
- User click behavior
- Product interaction history
- Rule-based reasoning
- Knowledge representation concepts
- Generative AI-inspired recommendation flow

The goal is to recommend products that match user interest instead of displaying random or static product suggestions.

This project also includes knowledge representation concepts such as **First Order Logic** to demonstrate reasoning-based AI design.

---

## 🏗️ System Architecture

```text
                 ┌───────────────┐
                 │     User      │
                 └───────┬───────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ E-Commerce Frontend │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Django Backend    │
              └──────────┬──────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────────┐
│ Product Data │  │ User Clicks  │  │ User Session Data│
└──────┬───────┘  └──────┬───────┘  └────────┬─────────┘
       │                 │                   │
       └─────────────────┼───────────────────┘
                         ▼
              ┌─────────────────────┐
              │ Recommendation Logic │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Recommended Products│
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │  Personalized UI    │
              └─────────────────────┘
```

---

## 🔄 Workflow

1. User registers or logs into the platform.
2. User browses products through the e-commerce interface.
3. Product interactions and clicks are captured.
4. Interaction data is stored for recommendation processing.
5. Recommendation logic analyzes product data and user behavior.
6. Relevant products are selected and ranked.
7. Personalized recommendations are shown to the user.
8. The shopping experience becomes more targeted and intelligent.

---

## 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite for local development |
| AI / Logic | Generative AI concepts, Rule-Based Reasoning, First Order Logic |
| Data Handling | CSV product datasets |
| Recommendation Approach | User behavior tracking + product recommendation logic |
| Project Type | E-commerce AI recommendation system |

---

## 📂 Project Structure

```text
GenAI/
│
├── GenAI/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── genai.py
│   └── first_order_logic.py
│
├── products/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── migrations/
│
├── User/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── templates/
│   ├── ecommerce.html
│   ├── product_page.html
│   ├── products_page.html
│   ├── cart.html
│   ├── login.html
│   └── sign_up.html
│
├── static/
│   ├── CSS_files/
│   ├── JS_files/
│   └── Images/
│
├── media/
│   └── product_images/
│
├── All_Products_Data.csv
├── clicked_products.csv
├── manage.py
└── middleware.py
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Maria-Bano/ShopMind-ai-product-recommendation-engine.git
```

### 2. Navigate to the Project

```bash
cd ShopMind-ai-product-recommendation-engine
cd GenAI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Required Packages

```bash
pip install django neo4j
```

If additional packages are required in your local environment, install them according to the imports used in the project files.

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

### 8. Open the Project

```text
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Screenshots will be added after UI cleanup and demo capture.

Planned screenshots:

- Home page
- Product listing page
- Product detail page
- Recommendation results
- User interaction flow

---

## 💡 Example Use Case

A user visits an e-commerce website and browses products such as electronics, appliances, fashion items, or accessories.

Instead of showing the same products to every user, ShopMind tracks the user’s product interactions and applies recommendation logic to suggest products that are more relevant to the user’s interests.

This creates a more personalized shopping experience and demonstrates how AI-based recommendation systems can improve product discovery.

---

## ✅ What This Project Demonstrates

- Django backend development
- E-commerce workflow design
- Product data handling
- User interaction tracking
- Recommendation system logic
- Rule-based reasoning concepts
- Knowledge representation fundamentals
- AI-assisted product discovery
- Full-stack project structuring
- Portfolio-ready AI project presentation

---

## 🔮 Future Improvements

- Add Django REST Framework API endpoints
- Replace SQLite with PostgreSQL
- Add content-based filtering
- Add collaborative filtering
- Add vector similarity search for products
- Integrate an LLM for product explanation generation
- Add real-time recommendation updates
- Build an admin analytics dashboard
- Add Docker support
- Deploy the project on a cloud platform
- Add automated tests
- Add a proper `requirements.txt` file

---

## 🔐 Security & Repository Notes

- Local database files are excluded from version control.
- Environment files should not be committed.
- Product data used in this project is for development and demonstration purposes.
- This repository is structured for portfolio demonstration and educational learning.

---

## 📌 Repository Topics

Recommended GitHub topics for this repository:

```text
python
django
generative-ai
recommendation-system
ecommerce
ai-product-recommendation
knowledge-representation
rule-based-ai
product-recommendation
portfolio-project
```

---

## 📜 License

This project is developed for educational, research, and portfolio demonstration purposes.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star.

**Built by Maria Bano**  
AI Automation & Generative AI Developer

[GitHub](https://github.com/Maria-Bano)

</div>
