{
    'name': 'Website Mail Server',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Associate specific mail servers with websites',
    'description': """
# Website Mail Server for Odoo 18

The Website Mail Server module allows each website in a multi-website Odoo setup to use its own outgoing mail server and domain for sending emails. This ensures that emails sent from forms, orders, and notifications match the domain of the website where the user is interacting, providing a consistent brand experience.

## Features
- Associate specific outgoing mail servers with each website
- Automatically use the correct mail server based on the active website
- Format "From" addresses to match the website's domain
- Handle domains properly by removing protocols and paths
- Maintain proper security without using sudo()

## Use Cases
- Multi-brand businesses running different websites on a single Odoo instance
- Service providers hosting multiple client websites
- Organizations with geographically or functionally separate divisions
    """,
    'author': 'Christopher Lynn South, Claude (Anthropic)',
    'website': '',
    'depends': ['website', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/init_data.xml',
        'views/website_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # This ensures the module only installs on Odoo 18
    'odoo_version': '18.0',
    'license': 'LGPL-3',
}
