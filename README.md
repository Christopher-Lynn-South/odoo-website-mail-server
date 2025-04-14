Website Mail Server for Odoo 18
Description
The Website Mail Server module allows each website in a multi-website Odoo setup to use its own outgoing mail server and domain for sending emails. This ensures that emails sent from forms, orders, and notifications match the domain of the website where the user is interacting, providing a consistent brand experience.
Features

Associate specific outgoing mail servers with each website
Automatically use the correct mail server based on the active website
Format "From" addresses to match the website's domain
Handle domains properly by removing protocols and paths
Maintain proper security without using sudo()

Use Cases

Multi-brand businesses running different websites on a single Odoo instance
Service providers hosting multiple client websites
Organizations with geographically or functionally separate divisions

Technical Implementation
The module extends Odoo's mail functionality to dynamically select the appropriate mail server based on the website context. It handles proper formatting of email addresses and includes security configurations to ensure appropriate access rights.
Installation Guide
For Self-Hosted Odoo 18 Instances

Download the Module:

Clone from GitHub: git clone https://github.com/Christopher-Lynn-South/odoo-website-mail-server.git
Or download the ZIP file from the GitHub repository and extract it


Place the Module in Your Addons Directory:

Copy the website_mail_server folder to your Odoo addons path
Common addon paths include:

/opt/odoo/custom/addons/
/usr/lib/python3/dist-packages/odoo/addons/
/var/lib/odoo/addons/


You can find your addons path in the Odoo configuration file (/etc/odoo/odoo.conf)


Set Proper Permissions:
bashsudo chown -R odoo:odoo /path/to/website_mail_server
sudo chmod -R 755 /path/to/website_mail_server

Update the Addons List:

Go to Apps menu
Remove the "Apps" filter if active
Click "Update Apps List" in the top menu
Confirm by clicking "Update"


Install the Module:

Search for "Website Mail Server" in the Apps menu
Click "Install" button


Restart Odoo Service (recommended):
bashsudo systemctl restart odoo


Configuration
After installation:

Set Up Mail Servers:

Go to Settings → Technical → Email → Outgoing Mail Servers
Create a separate mail server for each domain with proper SMTP credentials
Ensure the "FROM Filter" field matches your domain pattern (e.g., *@yourdomain.com)


Associate Mail Servers with Websites:

Go to Website → Configuration → Websites
For each website, navigate to the "Email Settings" section
Select the appropriate mail server for the website


Test Your Configuration:

Visit each website frontend
Submit a form that sends an email (contact form, newsletter signup, etc.)
Verify the email is sent with the correct domain in the "From" address



Troubleshooting
If the module doesn't appear after installation:

Check Odoo server logs: tail -f /var/log/odoo/odoo-server.log
Verify module location matches your addons path
Ensure proper file permissions
Clear your browser cache and restart Odoo

If emails are not using the correct domain:

Verify the website has a mail server assigned
Check that the domain is properly formatted in the website configuration
Inspect email headers to confirm sending details

For additional support, please open an issue on the GitHub repository.
Compatibility
This module is designed exclusively for Odoo 18.
Authors

Christopher Lynn South
Claude (Anthropic)

License
LGPL-3