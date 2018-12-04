# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# Copyright 2018 Fanha Giang
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "QQBee Backend Theme",
    "summary": "QQbee backend theme",
    "version": "11.0.0.0.1",
    "category": "Themes/Backend",
	"description": """
		Backend theme for QQbee.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Openworx, Fanha Giang",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web_responsive',
    ],
    "data": [
        'views/assets.xml',
        'views/res_company_view.xml',
    ],
}

