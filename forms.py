from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    product_id = StringField('Product Id')
    product_name = StringField('Product Name')
    product_qty = StringField('Product Qty')
    store_location = StringField('Store Location')
    submit = SubmitField('Submit')