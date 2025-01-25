# Copyright (c) 2025, faiyaz@adimyra.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BagBarcodes(Document):
	pass

        # Regular expression for validation: 2 alphabets, 8 digits, 2 alphabets
# import re
# from frappe import _
# from frappe.model.document import Document

# class BagBarcodes(Document):
#     def validate(self):
#         # Regular expression for validation: 2 alphabets, 8 digits, 2 alphabets
#         pattern = r"^[A-Z]{2}\d{8}[A-Z]{2}$"
        
#         if not re.match(pattern, self.bag_number):
#             frappe.throw(
#                 _("Invalid Bag Number format: {0}. It should be 12 characters long, starting with 2 alphabets, followed by 8 digits, and ending with 2 alphabets.").format(self.bag_number)
#             )
