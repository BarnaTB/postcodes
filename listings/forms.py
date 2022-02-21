from django import forms


class CsvUploadForm(forms.Form):
    """Form class form admin to upload a csv of listings
    """
    csv_file = forms.FileField(required=True)
