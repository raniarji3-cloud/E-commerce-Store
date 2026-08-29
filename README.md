# 🛍️ ShopAZ — Smart E-Commerce & Custom Design Platform

> **An intelligent e-commerce platform that connects customers not only with products, but also with designers for personalized, made-to-order experiences.**

## 🚀 Overview

**ShopAZ** is a full-stack e-commerce platform built with **Django** to address a common problem in online shopping: customers can easily purchase ready-made products, but finding or requesting a product that matches their **specific style, requirements, and budget** is often difficult.

ShopAZ bridges this gap by combining a traditional e-commerce experience with a **custom designer-request workflow**.

Customers can browse products, manage their cart and orders, discover designers based on their specialization, and submit personalized design requests with descriptions, reference images, and budgets.

The platform is designed as a foundation for a more intelligent shopping ecosystem where **e-commerce, personalization, and AI-powered assistance** can work together.

---

## 🎯 Real-World Problem

Traditional e-commerce platforms mainly focus on:

**Product → Customer → Purchase**

But many customers want:

* A customized outfit or product
* A design based on a reference image
* A specific style, material, pattern, or color
* A product within a particular budget
* Direct access to a suitable designer

This often requires searching through multiple platforms, contacting designers separately, and manually explaining requirements.

### 💡 ShopAZ Solution

ShopAZ introduces:

**Customer → Product/Designer → Custom Request → Personalized Solution**

Customers can select a suitable designer and submit all their requirements from one platform.

---

## ✨ Key Features

### 🛒 E-Commerce

* Product browsing and categorization
* Product detail pages
* Shopping cart management
* Quantity controls
* Checkout workflow
* Order management
* Order status tracking

### 👤 Authentication

* User registration
* Secure login/logout
* CSRF-protected forms
* Authenticated user workflows
* Personalized user experience

### 🎨 Designer Marketplace

Customers can discover designers based on:

* Specialization
* Location
* Experience
* Price range
* Designer profile/avatar

Each designer has a dedicated customization workflow.

### ✨ Custom Design Requests

Customers can:

1. Select a designer
2. Provide a design title
3. Describe their requirements
4. Upload an optional reference image
5. Specify their budget
6. Submit the request

Each request is stored and associated with the selected designer and authenticated customer.

### 📋 Request Tracking

Customers can view their submitted requests through **My Design Requests**, including:

* Requested design
* Assigned designer
* Budget
* Submission date
* Current request status

Supported statuses include:

`Pending → Accepted → Rejected → Completed`

### 🛠️ Admin Management

The Django Admin dashboard allows administrators to manage:

* Products
* Categories
* Orders
* Designers
* Design Requests
* Request statuses

---

## 🧠 Intelligent E-Commerce Vision

ShopAZ is designed beyond a conventional shopping website.

The architecture provides a foundation for future intelligent features such as:

* 🤖 AI-based product recommendations
* 🎨 AI-assisted custom design generation
* 🖼️ Reference-image understanding
* 🧑‍🎨 Intelligent designer matching
* 💬 AI shopping assistance
* 🛍️ Agentic commerce workflows
* 📊 Personalized shopping experiences

The long-term goal is to make the platform capable of understanding **what the customer wants**, rather than simply displaying products.

---

## 🏗️ Technology Stack

### Backend

* Python
* Django
* Django ORM
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript
* Responsive UI

### Features & Services

* Django Authentication
* CSRF Protection
* Image Uploads
* Django Admin
* Database-driven designer and request management

---

## 📂 Project Structure

```text
CodeAlpha_E-commerce-Store/
│
├── EcommerceStore/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── products.html
│   ├── login.html
│   ├── signup.html
│   ├── designers.html
│   ├── create_design_request.html
│   └── design_requests.html
│
├── static/
│   ├── css/
│   └── images/
│
├── manage.py
└── README.md
```

---

## 🔄 Custom Design Workflow

```text
Customer
   ↓
Browse Designers
   ↓
Select Designer
   ↓
Customize With This Designer
   ↓
Describe Design Requirements
   ↓
Upload Reference Image
   ↓
Set Budget
   ↓
Send Design Request
   ↓
Designer/Admin Reviews Request
   ↓
Accepted / Rejected
   ↓
Completed
```

---

## 🗄️ Core Data Models

ShopAZ uses a relational database architecture with models for:

* `User`
* `Category`
* `Product`
* `Cart`
* `CartItem`
* `Order`
* `OrderItem`
* `Designer`
* `DesignRequest`

The `DesignRequest` model connects a **customer** with a selected **designer**, while storing the customization requirements, reference image, budget, status, and submission time.

---

## 🔐 Security

The application follows Django's built-in security mechanisms, including:

* CSRF protection
* Authentication
* Password hashing through Django's authentication system
* Server-side form validation
* Authenticated request handling

---

## 📈 Future Improvements

The next evolution of ShopAZ is focused on **AI-powered and agentic commerce**.

### Planned Features

* [ ] AI shopping assistant
* [ ] Personalized product recommendations
* [ ] AI-based designer matching
* [ ] AI-generated design concepts
* [ ] Image-to-design understanding
* [ ] Automated designer-request assistance
* [ ] Smart product search
* [ ] Personalized customer dashboard
* [ ] Payment gateway integration
* [ ] Real-time order notifications
* [ ] Designer dashboard
* [ ] Production/deployment optimization

---

## 🎓 Project Goal

ShopAZ was developed to explore how a conventional e-commerce application can evolve into a **personalized and intelligent commerce platform**.

Rather than limiting customers to predefined products, the platform creates a bridge between:

**E-Commerce + Customization + Designers + AI**

This makes ShopAZ a foundation for building a future-ready **AI-driven commerce experience**.

---

## 👩‍💻 Author

**Rani Arji**

B.Tech — Computer Science & Engineering

---

## ⭐ Why ShopAZ?

> **ShopAZ doesn't just ask “What do you want to buy?” — it moves toward understanding “What do you want to create?”**

If you find this project interesting, consider giving the repository a ⭐.
