## Website Item Group

Display 'Website Item Group' field filter on all-products page on web

### How it works ?

* Go to 'Products Settings'-->'Enable Website Item Group' enable it. screen shot shown below
* Go to http://localhost/all-products
* You will see 'Website Item Group' for field filters. screen shot shown below
* It would filter out Item Groups mentioned in 'Item' doctype --> website reference --> 'Website Item Group' child table

### Installation Steps

Step 1) One time to get app

`bench get-app https://github.com/ashish-greycube/website_item_group`

Step 2) to install app on any instance/site

`bench --site [sitename] install-app website_item_group`
`bench --site [sitename] migrate`

### Screeenshots

#### Enable Website Item Group
![Enable Website Item Group](https://github.com/ashish-greycube/website_item_group/blob/master/enable_in_product_settings.png)

#### 'Website Item Group' for field filters 
![Website Item Group](https://github.com/ashish-greycube/website_item_group/blob/master/visible_in_all_products_field_filter.png)
#### License

MIT