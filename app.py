from flask import Flask, request, render_template, jsonify
from mod.getfile import process_jsonfile, get_just_stores
from mod.forms import SearchForm
import re

app = Flask(__name__)

# Call the function which parse
# json store file
mylist = process_jsonfile()

# Get the name of stores
# return list
storenames = get_just_stores()


@app.route("/")
def index():
    """
        Ruturn the landing page for textfield
        with list of stores with valid postcodes

        :return: list
        :return: form
    """
    form = SearchForm()
    return render_template("includes/index.html", form=form, stores=storenames)


@app.route("/selected_stores")
def get_stores():
    """
        Return search string of stores
        with postcode, stores locations,
        Longtitude and latitude

    """
    found_list = []
    if request.method == 'GET':
        value = request.args.get('name_post')
        for index in mylist:
            if re.findall(value.upper(), index['postcode'].upper()) or \
               re.findall(value.upper(), index['name'].upper()):
                found_list.append(index)
        sort_found_list = sorted(found_list, key=lambda k: k['postcode'])
        return render_template("includes/selectedstores.html",
                               stores=sort_found_list)


@app.route("/store/<string:string>/")
def get_store(string):
    """
        Return search string of store
    """
    value = str(string)
    if request.method == 'GET':
        for index in mylist:
            if re.search(value, index['postcode']) or\
               re.search(value, index['name']):
                return (index['name'])


@app.route("/all_stores")
def get_all_stores():
    """
        Return all stores,postcode, stores locations,
        Longtitude and latitude
    """
    return render_template("includes/home.html", stores=mylist)


if __name__ == "__main__":
    app.run()
