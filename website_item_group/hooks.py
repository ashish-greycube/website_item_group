# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "website_item_group"
app_title = "Website Item Group"
app_publisher = "GreyCube Technologies"
app_description = "Display website item group products on web"
app_icon = "octicon octicon-project"
app_color = "orange"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/website_item_group/css/website_item_group.css"
# app_include_js = "/assets/website_item_group/js/website_item_group.js"

# include js, css files in header of web template
# web_include_css = "/assets/website_item_group/css/website_item_group.css"
# web_include_js = "/assets/website_item_group/js/website_item_group.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "website_item_group.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "website_item_group.install.before_install"
# after_install = "website_item_group.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "website_item_group.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"website_item_group.tasks.all"
# 	],
# 	"daily": [
# 		"website_item_group.tasks.daily"
# 	],
# 	"hourly": [
# 		"website_item_group.tasks.hourly"
# 	],
# 	"weekly": [
# 		"website_item_group.tasks.weekly"
# 	]
# 	"monthly": [
# 		"website_item_group.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "website_item_group.install.before_tests"
"extend_website_page_controller_context" : "website_item_group.www.all-products.index"
# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.portal.product_configurator.utils.get_products_html_for_website": "website_item_group.utils.get_products_html_for_website"
# }
# website_route_rules = [
# 	{"from_route": "/all-products", "to_route": "/a.html"},
# ]
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "website_item_group.task.get_dashboard_data"
# }

