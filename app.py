from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Or your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ankittalukder@gmai.com'      # Your email address
app.config['MAIL_PASSWORD'] = 'your_email_password'       # Your email password or app password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('All fields are required!')
            return redirect(url_for('contact'))

        msg = Message(subject='Contact Form Submission',
                      sender=email,
                      recipients=['recipient@example.com'],  # Replace with your own email
                      body=f"Name: {name}\nEmail: {email}\nMessage: {message}")

        try:
            mail.send(msg)
            flash('Thank you for your message!')
        except Exception as e:
            flash(f'An error occurred: {e}')
        return redirect(url_for('contact'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
