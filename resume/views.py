from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite

from .models import staticVars, Person, Education, ProjectOrJob, ProfessionalSkills, Academics, AreaOfInterest
from .forms import PersonForm, EducationForm, ProjectOrJobForm, ProfessionalSkillsForm, AcademicsForm, AreaOfInterestForm
import logging as log
from django.forms import formset_factory
'''
FORMS = [('resumes', ResumeForm),
         ('work_experience', WorkExperienceFormSet),
         ('certifications', CertificationFormSet),
         ('education', EducationFormSet),
         ('skills', SkillFormSet),
         ('languages', LanguageFormSet), ]


TEMPLATES = {'resumes': 'resumes/resumes.html',
             'work_experience': 'resumes/work_experience.html',
             'certifications': 'resumes/certifications.html',
             'education': 'resumes/education.html',
             'skills': 'resumes/skills.html',
             'languages': 'resumes/languages.html', }'''
workExp = []
personForm = []
educations = []
skills = []
FORM_TYPES = ['person', 'workorjob', 'education', 'skills']
iterator = iter(FORM_TYPES)
step = next(iterator)
def resumeFill(request):
    personform = PersonForm()
    educationform = EducationForm()
    forms = [personform,educationform]
    global step
    if request.method == 'POST':
        #form_number = staticVars.form_number
        print("we are in resumeFill ")
        personform = PersonForm(request.POST)
        educationform = EducationForm(request.POST)
        projectOrJobform = ProjectOrJobForm(request.POST)
        professionalSkillsform = ProfessionalSkillsForm(request.POST)
        academicsform = AcademicsForm(request.POST)
        areaOfInterestform = AreaOfInterestForm(request.POST)

        if personform.is_valid():
            personform.save()
            name1 = personform.cleaned_data['first_name']
            print(name1)
            personForm.append(personform.cleaned_data)

        if step == 'person' and not personform.is_valid():
            return render(request, 'resume/resume_fill.html',{'form': PersonForm(),'name':'person','error': 'error'})

        if educationform.is_valid():
            #educationform.save()
            education = educationform.cleaned_data
            if education not in educations:
                educations.append(education)

        if step == 'education' and not educationform.is_valid():
            print("education form not valid")

        if projectOrJobform.is_valid():
            projectOrJobform.save()
            work = projectOrJobform.cleaned_data
            print("job form valid")
            if not work in workExp:
                workExp.append(projectOrJobform.cleaned_data)

        if professionalSkillsform.is_valid():
            professionalSkillsform.save()
            skill = professionalSkillsform.cleaned_data
            if skill not in skills:
                skills.append(skill)

        if academicsform.is_valid():
            academicsform.save()

        print("value ",request.POST['submit'])

        '''if request.POST['submit']=="add another":
            print("calling from add another")
            return render(request, 'resume/resume_fill.html',{'form': ProjectOrJobForm(),'name':'job'})'''

        if  request.POST['submit']=="submit":
            print("calling from submit ",len(workExp))
            return render(request, 'resume/index.html',{'form':personForm[0],
            'workExp':workExp,
            'skills':skills,
            'education':educations})

        if request.POST['submit']=="next":
            step = next(iterator)
        
        print("step is ",step)
        if step == FORM_TYPES[0]:
            return render(request, 'resume/resume_fill.html',{'form': PersonForm(),'name':'person'})
        elif step==FORM_TYPES[1]:
            return render(request, 'resume/resume_fill.html',{'form': ProjectOrJobForm(),'name':'job'})
        elif step==FORM_TYPES[2]:
            return render(request, 'resume/resume_fill.html',{'form': EducationForm(),'name':'education'})
        elif step==FORM_TYPES[3]:
            return render(request, 'resume/resume_fill.html',{'form': ProfessionalSkillsForm(),'name':'skills'})

       # return render(request, 'resume/resume_fill.html',{'form': ProjectOrJobForm(),'name':'job'})
       
    else :
        print("bahar se call tha")
        return render(request, 'resume/resume_fill.html',{'form': PersonForm(),'name':'person'})

    '''return render(request, 'resume/resume_fill.html', {

        'personform': PersonForm(),
        'educationform': EducationForm(),
        'projectOrJobform': ProjectOrJobForm(),
        'professionalSkillsform': ProfessionalSkillsForm(),
        'academicsform': AcademicsForm(),
        'areaOfInterestform': AreaOfInterestForm(),
    })'''
    '''context ={}
    performset = formset_factory(PersonForm)
    formset = performset()
    context['formset']=formset
    return render(request,'resume/resume_fill.html',context)'''

def ProjectOrJob(request):

    if request.method == 'POST':
        print("im in project or job")
        #form_number = staticVars.form_number
        log.debug('to call person form')
        personform = PersonForm(request.POST)
        educationform = EducationForm(request.POST)
        projectOrJobform = ProjectOrJobForm(request.POST)
        professionalSkillsform = ProfessionalSkillsForm(request.POST)
        academicsform = AcademicsForm(request.POST)
        areaOfInterestform = AreaOfInterestForm(request.POST)

        if personform.is_valid():
            personform.save()
            name1 = personform.cleaned_data['first_name']
            print(name1)

        if educationform.is_valid():
            educationform.save()

        if projectOrJobform.is_valid():
            projectOrJobform.save()
            workExp.append(projectOrJobform.cleaned_data)

        if professionalSkillsform.is_valid():
            professionalSkillsform.save()

        if academicsform.is_valid():
            academicsform.save()

        if areaOfInterestform.is_valid():
            areaOfInterestform.save()
        
        if request.POST.get("add another"):
            return render(request, 'resume/resume_fill.html',{'form': (ProjectOrJobForm)})
        else :
            render(request, 'resume/resumeView.html',{'personform': personform.cleaned_data,
            'workExp': workExp})

    return render(request, 'resume/resume_fill.html',{'form': (ProjectOrJobForm)})
    


def resumeView(request):
    site_name = RequestSite(request).domain
    person = Person.objects.all()[:1]
    log.debug('here')
    education = Education.objects.all()
    projectOrJob = ProjectOrJob.objects.all()[:5]
    professionalSkills = ProfessionalSkills.objects.all()[:5]
    academics = Academics.objects.all()[:5]
    areaOfInterest = AreaOfInterest.objects.all()

    return render('resume/index.html', {
        'site_name': site_name,
        'person': person,
        'education': education,
        'projectOrJob': projectOrJob,
        'professionalSkills': professionalSkills,
        'academics': academics,
        'areaOfInterest': areaOfInterest,
    }
    )  # , context_instance=RequestContext(request))
