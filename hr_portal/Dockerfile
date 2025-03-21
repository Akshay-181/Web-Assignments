# Use Python with Apache and CGI
FROM python:3.11-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-wsgi-py3 python3-docx python3-pip && \
    pip install pdfminer.six

# Enable CGI module in Apache
RUN a2enmod cgi
RUN a2enmod wsgi

# Set environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# Copy the project files
COPY ./html /var/www/html/
COPY ./cgi-bin /usr/lib/cgi-bin/

# Set permissions
RUN chmod +x /usr/lib/cgi-bin/*.py

# Configure Apache
COPY apache.conf /etc/apache2/sites-available/000-default.conf

# Start Apache server
CMD ["apachectl", "-D", "FOREGROUND"]
