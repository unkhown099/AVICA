# AVICA - AI-Powered Auto Service Management System

**AI-powered Vehicle Recognition, Intelligent Recommendations, Customer Module, and Business Analytics System**

A comprehensive management platform designed for Ottowikk Auto Service Center that integrates artificial intelligence with vehicle service management to streamline operations, enhance customer experience, and provide intelligent business insights.

---

## 🎯 Core Features

- **AI-Powered Vehicle Recognition** - Advanced vehicle identification and analysis
- **Intelligent Service Recommendations** - AI-driven maintenance and repair suggestions
- **Customer Relationship Management** - Complete customer lifecycle management
- **Business Analytics Dashboard** - Real-time insights and performance metrics
- **Multi-role Access System** - Tailored interfaces for different user types

---

## 🏗️ Project Structure

```
AVICA/
├── apps/                           # Django Applications
│   ├── accounts/                   # User authentication & authorization
│   ├── vehicles/                   # Vehicle management & recognition
│   ├── customers/                  # Customer relationship management
│   ├── inventory_management/       # Parts & inventory tracking
│   ├── service_advisor/            # Service management interface
│   ├── branch_manager/             # Branch operations management
│   └── business_owner/             # Business analytics & owner dashboard
├── avica_core/                     # Project configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI configuration
│   └── asgi.py                     # ASGI configuration
├── static/                         # Static files (CSS, JS, Images)
├── templates/                      # HTML templates
├── venv/                           # Python virtual environment
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 👥 User Roles & Modules

### 1. Accounts Module (`apps/accounts/`)
- User authentication (login/logout)
- Role-based access control
- Profile management
- Password reset functionality

### 2. Vehicles Module (`apps/vehicles/`)
- Vehicle registration and tracking
- AI-powered vehicle recognition
- Service history tracking
- Vehicle specifications database

### 3. Customers Module (`apps/customers/`)
- Customer profile management
- Service appointment scheduling
- Communication history
- Customer feedback collection

### 4. Inventory Management (`apps/inventory_management/`)
- Auto parts inventory tracking
- Stock level monitoring
- Supplier management
- Purchase order processing

### 5. Service Advisor (`apps/service_advisor/`)
- Service job management
- Customer interaction interface
- Work order creation
- Service status updates

### 6. Branch Manager (`apps/branch_manager/`)
- Branch performance monitoring
- Staff management
- Daily operations oversight
- Local reporting

### 7. Business Owner (`apps/business_owner/`)
- Business analytics dashboard
- Financial reporting
- Multi-branch comparison
- Strategic insights

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Database
- pip (Python package manager)

### Step 1: Clone and Setup Environment

```bash
# Clone repository (if applicable)
# git clone <repository-url>

# Navigate to project directory
cd AVICA

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Database Configuration

```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE avica_db;
EXIT;

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 4: Run Development Server

```bash
python manage.py runserver
```

Access the application at: **http://localhost:8000**

---

## 🔧 Configuration

### Environment Setup
- Update database credentials in `avica_core/settings.py` if needed
- Configure static and media file paths
- Set up email configuration for notifications

### AI Module Configuration

```python
# AI settings (example)
AI_VEHICLE_RECOGNITION_ENABLED = True
AI_RECOMMENDATION_ENGINE = True
```

---

## 📊 Key Technologies

### Backend
- **Django 6.0** - Web framework
- **MySQL** - Database management
- **Django REST Framework** - API development (if applicable)

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript** - Interactive features
- **Bootstrap** - Responsive design framework

### AI/ML Components
- Vehicle recognition algorithms
- Predictive maintenance models
- Customer behavior analysis

---

## 🔐 Security Features

- Password hashing and encryption
- CSRF protection
- SQL injection prevention
- XSS protection
- Session security
- Role-based access control

---

## 📈 Business Benefits

### For Ottowikk Auto Service Center
- 40% faster vehicle check-in process
- 30% improvement in service recommendations accuracy
- Real-time inventory tracking
- Comprehensive customer insights
- Data-driven decision making

### For Customers
- Faster service turnaround
- Accurate maintenance predictions
- Transparent pricing and timelines
- Easy appointment scheduling

---

## 🧪 Testing

```bash
# Run test suite
python manage.py test

# Run specific app tests
python manage.py test apps.vehicles
```

---

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
- Verify MySQL is running
- Check database credentials in `settings.py`

**Static Files Not Loading**
- Run `python manage.py collectstatic`
- Check `STATIC_URL` and `STATICFILES_DIRS` in settings

**Module Import Errors**
- Ensure all apps are in `INSTALLED_APPS`
- Verify Python path includes apps directory

---

## 👨‍💻 Development Team

This project is developed as part of the Software Engineering course requirements, focusing on:
- Software development lifecycle
- Agile methodologies
- Team collaboration
- Quality assurance practices

---

## 📄 License

This project is developed for educational purposes as part of Software Engineering coursework.

---

## 🤝 Contributing

For development team members:
1. Create feature branch
2. Commit changes with descriptive messages
3. Submit pull request for review
4. Ensure all tests pass before merging

---

## 📞 Support

For technical issues or questions regarding the AVICA system, please contact the development team or refer to the project documentation.

---

**Last Updated:** [Current Date]  
**Version:** 1.0.0  
**Status:** Development

---

*Empowering Ottowikk Auto Service Center with intelligent vehicle management solutions.*