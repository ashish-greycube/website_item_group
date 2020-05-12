import frappe
import numpy as np
from erpnext.portal.product_configurator.item_variants_cache import ItemVariantsCacheManager
from erpnext.portal.product_configurator.utils import get_product_settings,get_item_codes_by_attributes,get_items,get_product_settings,get_attribute_filter_data,get_html_for_items

def get_weightage(item_group_name):
	weightage = frappe.db.get_value('Item Group', item_group_name, 'weightage')
	return weightage

def get_field_filter_data():
	product_settings = get_product_settings()
	filter_fields=[]
	if product_settings.enable_field_filters==1:
		filter_fields = [row.fieldname for row in product_settings.filter_fields]
	#enable_website_item_group
	if product_settings.enable_website_item_group==1:
		filter_fields.append('website_item_groups')

	meta = frappe.get_meta('Item')
	fields = [df for df in meta.fields if df.fieldname in filter_fields]
	
	filter_data = []
	for f in fields:
		if f.fieldtype=='Table':
			doctype=f.options
		else:
			doctype = f.get_link_doctype()

		# apply enable/disable filter
		meta = frappe.get_meta(doctype)
		filters = {}
		if meta.has_field('enabled'):
			filters['enabled'] = 1
		if meta.has_field('disabled'):
			filters['disabled'] = 0

		if f.fieldtype =='Table':
			fieldname = [df.fieldname for df in meta.fields if df.fieldtype=='Link'][0]
			values=[]
			for d in frappe.get_all(doctype,fields=[fieldname],filters=filters,group_by=fieldname):
				values.append(d[fieldname])
			# values = [d[fieldname] for d in frappe.get_all(doctype,fields=[fieldname],filters=filters,group_by=fieldname)]
			values.sort(reverse=True, key=get_weightage)
		else:
			values = [d.name for d in frappe.get_all(doctype, filters)]
		filter_data.append([f, values])
	return filter_data



def get_items_by_fields(field_filters):
	meta = frappe.get_meta('Item')
	filters = []
	for fieldname, values in field_filters.items():
		if not values: continue

		_doctype = 'Item'
		_fieldname = fieldname

		df = meta.get_field(fieldname)
		# added fieldtype as Table
		if df.fieldtype in ['Table','Table MultiSelect']:
			child_doctype = df.options
			child_meta = frappe.get_meta(child_doctype)
			fields = child_meta.get("fields", { "fieldtype": "Link", "in_list_view": 1 })
			if fields:
				_doctype = child_doctype
				_fieldname = fields[0].fieldname

		if len(values) == 1:
			filters.append([_doctype, _fieldname, '=', values[0]])
		else:
			filters.append([_doctype, _fieldname, 'in', values])

	return get_items(filters)

# no change just to call above functions
@frappe.whitelist(allow_guest=True)
def get_products_html_for_website(field_filters=None, attribute_filters=None):
	field_filters = frappe.parse_json(field_filters)
	attribute_filters = frappe.parse_json(attribute_filters)

	items = get_products_for_website(field_filters, attribute_filters)
	html = ''.join(get_html_for_items(items))

	if not items:
		html = frappe.render_template('erpnext/www/all-products/not_found.html', {})

	return html

def get_products_for_website(field_filters=None, attribute_filters=None, search=None):

	if attribute_filters:
		item_codes = get_item_codes_by_attributes(attribute_filters)
		items_by_attributes = get_items([['name', 'in', item_codes]])

	if field_filters:
		items_by_fields = get_items_by_fields(field_filters)

	if attribute_filters and not field_filters:
		return items_by_attributes

	if field_filters and not attribute_filters:
		return items_by_fields

	if field_filters and attribute_filters:
		items_intersection = []
		item_codes_in_attribute = [item.name for item in items_by_attributes]

		for item in items_by_fields:
			if item.name in item_codes_in_attribute:
				items_intersection.append(item)

		return items_intersection

	if search:
		return get_items(search=search)

	return get_items()