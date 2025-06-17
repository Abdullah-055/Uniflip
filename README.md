# 📦 Uniflip — Campus Marketplace for Students

**Uniflip** is a full-stack Django-based web application built to enable university students to **buy**, **sell**, and **explore** products within their campus community.

---

## 🚀 Features

- 🛒 **List Products** with descriptions, prices, and images  
- 🔐 **User Registration & Login** with profile management  
- 📞 **Contact Seller** directly through the product page  
- 📝 **Order Placement** with buyer details  
- 💌 **Contact Us** form that saves messages to the admin panel  
- 👨‍💼 **Admin Panel** for managing users, products, and messages  
- 💬 **Flash Messages** to enhance UX  
- 🎨 **Clean UI** with HTML5 + CSS (custom pages and layout)

---

## ⚙️ Tech Stack

- **Backend**: Django 5.2  
- **Database**: SQLite3 (default)  
- **Frontend**: HTML, CSS, Django Templates  
- **Admin Interface**: Django Admin Panel  

---

## 📁 Project Structure

```
uniflip/
├── marketplace/
│   ├── templates/marketplace/
│   ├── static/marketplace/css/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── signals.py
├── uniflip/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

## 🖥️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/uniflip.git
cd uniflip
```

2. **Create a virtual environment & install dependencies**

```bash
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. **Apply migrations & create a superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. **Run the server**

```bash
python manage.py runserver
```

5. **Access the site**

Open your browser and go to:  
`http://127.0.0.1:8000/`

---

## 🧪 Testing

You can log in as an admin at `/admin` to view:
- Products
- Orders
- Contact messages
- Registered users

---

## ✨ Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙌 Acknowledgements

- Built with [Django](https://www.djangoproject.com/)
- Designed with ❤️ for students

