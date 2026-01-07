php.ini en Windows:
C:/xampp/php/php.ini
(Espero que no sea vuestro caso)

En Ubuntu está en:
/etc/php/8.3/apache2


sudo nano /etc/php/8.3/apache2/php.ini

display_errors

display_errors = Off

sudo service apache2 restar
