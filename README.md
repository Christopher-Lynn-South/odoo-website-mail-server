# Website Mail Server for Odoo 18

## Description
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

## Technical Implementation
The module extends Odoo's mail functionality to dynamically select the appropriate mail server based on the website context. It handles proper formatting of email addresses and includes security configurations to ensure appropriate access rights.

## Installation
Install like any Odoo module. After installation, configure mail servers for each website through the Website configuration interface.

## Compatibility
This module is designed exclusively for Odoo 18.

## Authors
- Christopher Lynn South
- Claude (Anthropic)

## License
LGPL-3
