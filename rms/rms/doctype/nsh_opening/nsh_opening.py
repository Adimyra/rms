# Copyright (c) 2025, faiyaz@adimyra.com and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class NSHOpening(Document):
# 	pass

import frappe
import re
from frappe import _
from frappe.model.document import Document

class NSHOpening(Document):
    def validate(self):
        # Validate all rows in the barcodes child table
        for barcode in self.barcodes:
            if not self.is_valid_bag_number(barcode.bag_number):
                frappe.throw(
                    _("Invalid Article Number: {0}. Format: 2 letters, 8 digits, 2 letters. Scan Again!").format(barcode.bag_number)
                )
    
    @staticmethod
    def is_valid_bag_number(bag_number):
        # Regular expression for validation: 2 alphabets, 8 digits, 2 alphabets
        pattern = r"^[A-Z]{2}\d{8}[A-Z]{2}$"
        return re.match(pattern, bag_number)
