from django import forms
from .models import ProjectItem

class ProjectItemForm(forms.ModelForm):

    class Meta:
        model = ProjectItem
        fields = [ 'description','title','url_github','image','tags']
        widgets={
            'title':forms.TextInput(
                attrs={"class": "form-control mb-3", 'requerid':True,'placeholder':'Nombre de proyecto',}
                ),
            'url_github':forms.TextInput(
                attrs={"class": "form-control  mb-3", 'requerid':True,'placeholder':'www.example.com'}
                ),
            'image':forms.FileInput(
                attrs={"class": "form-control mb-3", 'requerid':True,'placeholder':'www.example.com'}
                ),
            'tags':forms.TextInput(
                attrs={"class": "form-control mb-3", 'requerid':True,'placeholder':'CSS, JS, PYTHON, etc'}
                )
        }
        #exclude= ('description',)
            
""" description:forms.Textarea(
attrs={"class": "form-control mb-3", 'requerid':True,'rows':'2',}
)"""