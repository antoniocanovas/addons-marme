# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Reports Marmecars",
    "summary": "Reports from PO with account wiht account_analytic_id in line.",
    "version": "14.0.1.0.0",
    "category": "Reports",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ['purchase'],
    "data": [
        "views/report_purchaseorder_account_analytic_id.xml",
    ],
    "installable": True,
}
