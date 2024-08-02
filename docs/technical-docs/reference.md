---
title: Reference
parent: Technical Docs
nav_order: 3
---



{: .no_toc }
# Reference documentation

{: .attention }
> This page collects internal functions, routes with their functions, and APIs (if any).
> 
> See [Uber](https://developer.uber.com/docs/drivers/references/api) or [PayPal](https://developer.paypal.com/api/rest/) for exemplary high-quality API reference documentation.
>
> You may delete this `attention` box.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Home
### home()
**Route:** `/home` and `/`

**Methods:** GET, POST

**Purpose:** Renders the `index.html` template.

**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Home</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
    <div class="main-banner">
      <img src="static/images/banner.jpg" alt="Fashion Banner">
        <div class="banner-text">
          <h1>Style is Eternal</h1>
          <p>Discover Your Unique Fashion Identity</p>
        </div>
    </div>
    <div class="content">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vehicula ex eu ante vehicula, ac viverra nisi dapibus. Maecenas id magna sit amet nisi consectetur cursus. Nulla facilisi. Duis sollicitudin, tortor nec pellentesque dignissim, odio orci feugiat eros, ac fringilla dolor lorem sed leo. Aliquam erat volutpat.</p>
    </div>
    <!-- Other Home Contents -->
  </body>
  </html>
  ```

## Home (index)
### index()
**Route:** `/index`
**Methods:** GET
**Purpose:** Renders the `index.html` template. This also contains the home page
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Home</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
    <div class="main-banner">
      <img src="static/images/banner.jpg" alt="Fashion Banner">
        <div class="banner-text">
          <h1>Style is Eternal</h1>
          <p>Discover Your Unique Fashion Identity</p>
        </div>
    </div>
    <div class="content">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vehicula ex eu ante vehicula, ac viverra nisi dapibus. Maecenas id magna sit amet nisi consectetur cursus. Nulla facilisi. Duis sollicitudin, tortor nec pellentesque dignissim, odio orci feugiat eros, ac fringilla dolor lorem sed leo. Aliquam erat volutpat.</p>
    </div>
    <!-- Other Home Contents -->
  </body>
  </html>
  ```

## User Registration
### register()
**Route:** `/register`
**Methods:** GET, POST
**Purpose:** Handles user registration.
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Register</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="login-container">
        <h2>Register</h2>
        <form method="POST" action="">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.username.label }}
                {{ form.username(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.email.label }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.password.label }}
                {{ form.password(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.confirm_password.label }}
                {{ form.confirm_password(class="form-control") }}
            </div>
            <div class="form-group">
                <button type="submit">Sign Up</button>
            </div>
        </form>
    </div>
  </body>
  </html>
  ```

## Login
### login()
**Route:** `/login`
**Methods:** GET, POST
**Purpose:** Handles user login.
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Login</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="login-container">
        <h2>Login</h2>

        <form method="POST" action="">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.email.label }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.password.label }}
                {{ form.password(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.remember() }}
                {{ form.remember.label }}
            </div>
            <div class="form-group">
                <button type="submit">Login</button>
            </div>
        </form>
      </div>
  </body>
  </html>
  ```

## Logout
### logout()
**Route:** `/logout`
**Methods:** GET
**Purpose:** Logs out the current user. This will redirect back to the login page.
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Login</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="login-container">
        <h2>Login</h2>

        <form method="POST" action="">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.email.label }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.password.label }}
                {{ form.password(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.remember() }}
                {{ form.remember.label }}
            </div>
            <div class="form-group">
                <button type="submit">Login</button>
            </div>
        </form>
      </div>
  </body>
  </html>
  ```

## User Dashboard
### dashboard()
**Route:** `/dashboard`
**Methods:** GET
**Purpose:** Renders the `dashboard.html` template. Requires user to be logged in.
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Dashboard</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
    <div class="dashboard-header">
     <h2>Welcome, User!</h2>
     <p>This is your dashboard where you can manage your details.</p>
    </div>
    <div class="dashboard-container">
      <form>
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="preferences">Vorlieben:</label><br>
        <textarea id="preferences" name="preferences"></textarea><br>
        <label for="biography">Biographie:</label><br>
        <textarea id="biography" name="biography"></textarea><br>
        <input type="submit" value="Absenden">
      </form>
    </div>
  </body>
  </html>
  ```

## Single Advisor Page
### singleadvisor()
**Route:** `/singleadvisor`
**Methods:** GET
**Purpose:** Renders the `singleadvisor.html` template.
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Advisor</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="main-content">
        <div class="advisor-image">
            <img id="advisor-img" src="" alt="Advisor Image">
        </div>
        <div class="advisor-info">
            <h2 id="advisor-name"></h2>
            <div class="section">
                <div class="section-title about-me">Über mich</div>
                <div id="advisor-description" class="section-content"></div>
                 <div class="section-content">
                <p>Du möchtest mit deine Persönlichkeit mit dem gewissen Style ausdrücken? Dann buche mich als deinen persönlichen Styling Berater! Ich begleite schon seit 5 Jahren die bekanntesten Fashion Influencer aus Instagram und mache auch deinen Style Likebale. Just Call Me!</p>
                </div>
            </div>
            <div class="section">
                <div class="section-title">Details</div>
                <div class="section-content">
                    <p>Kategorie: <span id="advisor-category"></span></p>
                    <p>Standort: <span id="advisor-location"></span></p>
                    <p>Services: <span id="advisor-services"></span></p>
                </div>
            </div>
            <div class="section">
                <div class="section-title">Meine Stylings</div>
                <div class="photos">
                    <img src="{{ url_for('static', filename='images/men1.jpg') }}" alt="Style 1">
                    <img src="{{ url_for('static', filename='images/men2.jpg') }}" alt="Style 2">
                    <img src="{{ url_for('static', filename='images/men3.jpg') }}" alt="Style 3">
                    <img src="{{ url_for('static', filename='images/men4.png') }}" alt="Style 4">
                    <img src="{{ url_for('static', filename='images/men5.jpg') }}" alt="Style 5">
                    <img src="{{ url_for('static', filename='images/men6.jpg') }}" alt="Style 6">
                </div>
            </div>
       <!-- Other Advisor content -->
  </body>
  </html>
  ```

## Payment Page
### payment()
- **Route:** `/payment`
- **Methods:** GET
- **Purpose:** Renders the `payment.html` template. This is the 3 step process that guides the user payment.
- **Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Payment</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="container">
        <div class="payment-steps">
            <div class="step active" id="step1">Order Details</div>
            <div class="step" id="step2">Payment Information</div>
            <div class="step" id="step3">Confirm Payment</div>
        </div>

        <div class="payment-content">
            <div class="step-content" id="step1-content">
                <h2>Order Details</h2>
                <p>Service: Fashion Consultation</p>
                <p>Price: €100</p>
                <button onclick="nextStep(2)">Next</button>
            </div>

            <div class="step-content" id="step2-content" style="display:none;">
                <h2>Payment Information</h2>
                <form id="payment-form">
                    <input type="text" placeholder="Card Number" required>
                    <input type="text" placeholder="Cardholder Name" required>
                    <input type="text" placeholder="Expiry Date (MM/YY)" required>
                    <input type="text" placeholder="CVV" required>
                    <button type="button" onclick="nextStep(3)">Next</button>
                </form>
            </div>

            <div class="step-content" id="step3-content" style="display:none;">
                <h2>Confirm Payment</h2>
                <p>Please review your order and payment details before confirming.</p>
                <button onclick="confirmPayment()">Confirm Payment</button>
            </div>
        </div>
      </div>
    <!-- Other Payment page content -->
  </body>
  </html>
  ```

## About
### aboutus()
**Route:** `/about`
**Methods:** GET
**Purpose:** Renders the `aboutus.html` template. This displays the information about the website.
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>About Us</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="about-container">
        <div class="about-section">
            <div class="image-placeholder">
                 <img src="static/images/step1.png" alt="Schritt 1">
            </div>
            <div class="about-text">
                <div class="section">
                <div class="section-title about-me">Wer ist Mustache?</div>
                 <div class="section-content">
                <p>Die Fashion Webseite von Mustache wurde von 2 Studenten kreiert, die eigentlich nur eine Projektarbeit abgeben. Später haben die beiden festgestellt, dass ihr Produkt eine tatsächliche Nachfrage für diejenigen Menschen erfüllt, die nach guten Fashion Beratern suchen.</p>
                </div>
            </div>
            </div>
        </div>

        <div class="references-section">
            <div class="reference">
               <img src="static/images/C&A.jpg" alt="Referenz 1 Logo">
            </div>
            <div class="reference">
                <img src="static/images/Gucci.jpg" alt="Referenz 2 Logo">
            </div>
            <div class="reference">
                <img src="static/images/H&M.png" alt="Referenz 3 Logo">
            </div>
        </div>
    </div>
  </body>
  </html>
  ```

## Advisors page
### advisors()
**Route:** `/advisors`
**Methods:** GET
**Purpose:** Renders the `advisors.html` template. This displays the list of advisors. 
**Sample Output:**
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Advisors</title>
      <link rel="stylesheet" href="static/css/style.css">
  </head>
  <body>
      <!-- Header -->
      <div class="advisors-content">
        <p>Entdecken Sie unsere erfahrenen Fashion-Berater, die Ihnen helfen, Ihren persönlichen Stil zu finden und zu perfektionieren.</p>
    </div>

    <div class="filters-container">
        <div class="filter">
            <h3>Kategorie</h3>
            <select id="categoryFilter">
                <option value="">Alle Kategorien</option>
            </select>
        </div>
        <div class="filter">
            <h3>Standort</h3>
            <select id="locationFilter">
                <option value="">Alle Standorte</option>
            </select>
        </div>
        <div class="filter">
            <h3>Service</h3>
            <select id="serviceFilter">
                <option value="">Alle Services</option>
            </select>
        </div>
    </div>

    <div id="advisors-container" class="advisors">
        <!-- Advisors will be dynamically added here -->
    </div>

    <div class="footer">
        <p>Impressum</p>
        <p><a href="aboutus.html">Wer ist Mustache</a></p>
        <p>© By Mustache</p>
    </div>

    <div id="contactPopup" style="display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #fff; padding: 20px; border: 1px solid #333;">
        <h2>Nachricht senden</h2>
        <input type="text" id="subject" placeholder="Betreff"></input><br/>
        <input type="text" id="email" placeholder="Email"></input><br/>
        <textarea id="message" rows="4" cols="50" placeholder="Nachricht"></textarea><br/>
        <button onclick="sendMessage()">Senden</button>
    </div>
  
    <!-- Other Advisors Page Content -->
  </body>
  </html>
  ```


## Send Email
### send_email()
**Route:** `/send-email`
**Methods:** POST
**Purpose:** Sends an email using the Mailjet API.
**Sample Output:**
  ```json
  {
      "status": "success",
      "message": "Email sent successfully!"
  }
  ```

## Payment Processing
### process_payment()
**Route:** `/process_payment`
**Methods:** POST
**Purpose:** Processes payment details.
**Sample Output:**
  ```
    Received payment data:
    Order details:
    Service: testService
    Price: 100
    Payment details:
    Card Number: 4444444444444444
    Cardholder Name: John Smith
    Expiry Date: 0226
    CVV: 444
  ```
  ```json
  {
      "message": "Payment processed successfully"
  }
  ```


[Design Desicions](https://pillek.github.io/design-decisions.html){: .btn .btn-purple }
