"""
Full-scale Content Builder for Sumeru Technologies Corporate Knowledge Service
Populates app/services/corporate_content.py with comprehensive, researched, verified data.
"""

import os
import json
import pprint

# Base corporate metadata
CORPORATE_METADATA = {
    "company_name": "Sumeru Technologies LLC",
    "founded_year": 1994,
    "tagline": "Technology That Moves Business Forward.",
    "subtagline": "Sumeru Technologies delivers consulting, systems integration and outsourcing solutions that help organizations build, transform and manage critical technology environments.",
    "phone_usa": "+1 331 888 9060",
    "email_primary": "HR@sumerutechnologies.com",
    "email_inquiries": "info@sumerutechnologies.com",
    "locations": {
        "usa": {
            "city": "Warrenville, Illinois",
            "title": "USA Corporate Headquarters",
            "address": "4580 Weaver Parkway, Suite 206, Warrenville, IL 60555",
            "phone": "+1 331 888 9060",
            "email": "HR@sumerutechnologies.com",
            "region": "Americas"
        },
        "europe": {
            "city": "Madrid, Spain",
            "title": "Europe Operations Hub",
            "address": "Calle Del Archiduque, Alberto, 13, 18 Sanchinarro, Madrid, Spain - 28050",
            "phone": "+34 625 81 54 46",
            "email": "europe@sumerutechnologies.com",
            "region": "EMEA"
        },
        "hyderabad": {
            "city": "Hyderabad, India",
            "title": "Global Delivery & Innovation Center",
            "address": "No. 1-98/9/3/20, 4th Floor, VIP Hills, Silicon Valley, Madhapur, Hyderabad, Telangana 500081",
            "phone": "+91 6303316071",
            "email": "india@sumerutechnologies.com",
            "region": "APAC"
        },
        "bangalore": {
            "city": "Bangalore, India",
            "title": "Technology Delivery Center",
            "address": "No. 128, 2nd Floor, Govindappa Road, Basavanagudi, Bengaluru, Karnataka 560004",
            "phone": "+91 80 40939860",
            "email": "bangalore@sumerutechnologies.com",
            "region": "APAC"
        }
    }
}

print("Corporate metadata defined.")
