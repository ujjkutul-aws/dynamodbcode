from flask import *
import aws_controller
from flask_bootstrap import Bootstrap
from forms import NameForm
import os
Secret_key = os.urandom(32)
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = Secret_key
Bootstrap(app)

@app.route('/')
def home():
    return "AWS DynamoDB Lab Flask website"


@app.route('/get-items', methods=["GET", "POST"])
def items():
    data = aws_controller.get_items()
    form = NameForm()
    if form.validate_on_submit():
        product_id = request.form.get("product_id")
        product_name = request.form.get("product_name")
        product_qty = request.form.get("product_qty")
        store_location = request.form.get("store_location")
        if request.form.get("add") == "add":
            print(product_id,product_name,product_qty,store_location)
            aws_controller.create_product(product_id,product_name,product_qty,store_location)
            return redirect(url_for('items'))
        elif request.form.get("delete") == "delete":
            print(product_id,product_name)
            aws_controller.delete_product(product_id,product_name)
            return redirect(url_for('items'))
        elif request.form.get("update") == "update":
            aws_controller.update_product(product_id,product_name,product_qty,store_location)
            return redirect(url_for('items'))
    return render_template('base.html', data=data, form=form)


if __name__ == '__main__':
    app.run(debug=True)
