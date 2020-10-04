from django import forms

from django.forms import modelformset_factory
from .models import Person, ProfileInterest, Education, ProjectOrJob, ProfessionalSkills, Academics, AreaOfInterest
import logging as log

class MyModelFormSet():
    def __init__(self, *args, **kwargs):
        super(MyModelFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

class PersonForm(forms.ModelForm):

    class Meta:
	
        model = Person
        #fields = ('first_name', 'last_name', 'gender', 'age','email','mobile','address')
        log.debug('in personForm in forms')
        fields = ('first_name', 'last_name','email','mobile','address')
        extra_field_count = forms.CharField(widget=forms.HiddenInput())
        widgets = {

            'first_name': forms.TextInput(attrs={'title': 'First Name'}),
            'last_name': forms.TextInput(attrs={'title': 'Last Name'}),
            #'age': forms.DateInput(),
            'email': forms.EmailInput(),
            'mobile': forms.TextInput(),
            'address':forms.TextInput()
        }
    def save(self):
        person = self.instance
        person.first_name = self.cleaned_data["first_name"]
        person.last_name = self.cleaned_data["last_name"]
        person.email = self.cleaned_data["email"]
        person.mobile = self.cleaned_data["mobile"]
        person.address = self.cleaned_data["address"]




class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('degree','institute', 'stream', 'passing_year', 'result')
        widgets = {
            'degree': forms.Select(attrs={'title': 'Degree'}),
            'stream': forms.TextInput(attrs={'title': 'Stream'}),
            'institute':forms.TextInput(attrs={'title': 'Institute'}),
            'passing_year': forms.TextInput(attrs={'title': 'Passing Date'}),
            'result': forms.TextInput(attrs={'title': 'Result'})
        }

    def save(self):
        educations = self.instance
        educations.degree = self.cleaned_data["degree"]
        educations.stream = self.cleaned_data["stream"]
        educations.institute = self.cleaned_data["institute"]
        educations.passing_year = self.cleaned_data["passing_year"]
        educations.result = self.cleaned_data["result"]


class ProjectOrJobForm(forms.ModelForm):

    class Meta:
        model = ProjectOrJob
        fields = ('work', 'title', 'start_date', 'end_date', 'description')
        widgets = {

            'work': forms.RadioSelect(attrs={'title': 'Work'}),
            'title': forms.TextInput(attrs={'title': 'Title'}),
            'start_date': forms.TextInput(attrs={'title': 'Start Date'}),
            'end_date': forms.TextInput(attrs={'title': 'End Date'}),
            'description': forms.Textarea(attrs={'title': 'Description'})
        }
    def save(self):
        workorjob = self.instance
        workorjob.title = self.cleaned_data["title"]
        workorjob.start_date = self.cleaned_data["start_date"]
        workorjob.end_date = self.cleaned_data["end_date"]
        workorjob.description = self.cleaned_data["description"]


class ProfessionalSkillsForm(forms.ModelForm):

    class Meta:
        model = ProfessionalSkills
        fields = ('skill_detail',)
        widgets = {

            'skill_detail': forms.TextInput(attrs={'title': 'Professional Skills'})
        }
    def save(self):
        skills = self.instance
        skills.skill_detail = self.cleaned_data['skill_detail']
        
ProfessionalSkillsSet = modelformset_factory(ProfessionalSkills,form = ProfessionalSkillsForm, formset= MyModelFormSet, extra =1, max_num = 5)

class AcademicsForm(forms.ModelForm):

    class Meta:
        model = Academics
        fields = ('academic_detail',)
        widgets = {

            'academic_detail': forms.Textarea(attrs={'title': 'Academics'})
        }


class AreaOfInterestForm(forms.ModelForm):

    class Meta:
        model = AreaOfInterest
        fields = ('area_of_interest_detail',)
        widgets = {

            'area_of_interest_detail': forms.Textarea(attrs={'title': 'Area Of Interest'})
        }
