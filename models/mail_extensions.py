from odoo import models, api
from urllib.parse import urlparse
from email.utils import parseaddr, formataddr

class MailMail(models.Model):
    _inherit = 'mail.mail'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Try to get website from context or HTTP request
            website_id = self.env.context.get('website_id')
            if not website_id:
                # Try to get current website from request
                try:
                    website = self.env['website'].get_current_website(fallback=False)
                    if website:
                        website_id = website.id
                except:
                    website_id = False
            if website_id:
                website = self.env['website'].browse(website_id)
                if website.mail_server_id:
                    # Set the website's mail server
                    vals['mail_server_id'] = website.mail_server_id.id

                    # Update from email if needed to match the domain
                    if website.domain and 'email_from' in vals:
                        # Parse current email_from to keep the name part
                        name, email = parseaddr(vals['email_from'])
                        if not name:
                            name = "Odoo"

                        # Clean the domain - remove protocol and path
                        domain = website.domain
                        if domain:
                            # Remove any protocol (http://, https://)
                            if '://' in domain:
                                parsed_domain = urlparse(domain)
                                domain = parsed_domain.netloc

                            # If still empty, use the raw domain
                            if not domain and website.domain:
                                domain = website.domain.replace('https://', '').replace('http://', '')

                            # Remove any trailing path or query params
                            domain = domain.split('/')[0]

                            # Create the new email from address
                            email = f"noreply@{domain}"
                            vals['email_from'] = formataddr((name, email))

        return super().create(vals_list)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def message_post_with_template(self, template_id, **kwargs):
        """Override to add website mail server when posting with template"""
        # Get current website if available
        website_obj = self.env['website']
        if hasattr(website_obj, 'get_current_website'):
            try:
                website = website_obj.get_current_website(fallback=False)
                if website and website.mail_server_id and kwargs.get('email_layout_xmlid'):
                    # Add mail server to the context
                    kwargs['mail_server_id'] = website.mail_server_id.id
            except Exception:
                # Safely handle any errors
                pass

        return super().message_post_with_template(template_id, **kwargs)
