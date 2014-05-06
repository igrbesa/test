from django import forms

class ArticleForm(forms.Form):
	"""docstring for ArticleForm"forms.Form"""
	Name = forms.CharField()
	Surname = forms.CharField()
	Email = forms.EmailField()
	Comment = forms.CharField(required=False)
		