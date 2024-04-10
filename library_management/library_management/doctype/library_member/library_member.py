# Copyright (c) 2024, Harish Raghav and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    #this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.custom_first_name} {self.custom_last_name or ""}'