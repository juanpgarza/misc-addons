# Copyright 2021 openNova - Juan Pablo Garza <juanp@opennova.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Base Whatsapp",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Misc",
    "website": "https://github.com/OpenNovaSoft/misc-addons",
    "author": "openNova",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/on_whatsapp_template_view.xml',
        ],
    "installable": True,
}
