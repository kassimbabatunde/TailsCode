from wtforms import Form, TextAreaField, StringField, validators


class SearchForm(Form):
    name_post = StringField(
        u'Serach Store', [validators.length(min=3, max=15)])
