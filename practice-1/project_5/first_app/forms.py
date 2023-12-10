from django import forms
from django.core import validators

# widgets --> field to html input

class contactForm(forms.Form):
    name = forms.CharField(label = ' user name: ',disabled=False,initial='rahaman',
                           help_text='Total lenght must be within 70 character',
                           widget=forms.Textarea(attrs={'placeholder':'Enter your name', 'id':'nameInput','class':'class1 class2 class3'})
                    
                           )
    
    # name = forms.CharField(widget=forms.TextInput())
    # form field valiate
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName) < 10 :
    #          raise forms.ValidationError('Enter a name at least 10 character')


    # email = forms.EmailField(label = 'user email',required= True,widget=forms.TextInput(attrs={'placeholder':'Enter your Email'}))
    # form field valiate
    # def clean_email(self):
    #     valEmail = self.cleaned_data['email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError('Enter .com')
        

    # best approach for validate     
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valNam =  self.cleaned_data['name']
    #     valEma =  self.cleaned_data['email']
    #     if len(valNam) < 10 :
    #          raise forms.ValidationError('Enter a name at least 10 character')
    #     if '.com' not in valEma:
    #         raise forms.ValidationError('Enter .com')
        
    # age = forms.IntegerField()
    # age1 = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # dateTime = forms.DateTimeField()
    dateTime1 = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'dateTime-local'}))
    date = forms.DateField()
    data1 = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check = forms.BooleanField()
    choices = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    meal = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal , widget=forms.CheckboxSelectMultiple)
    file = forms.FileField(required=False)
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))

    def length(value):
        if len(value) <5:
            raise forms.ValidationError('enter a value grater than 5 char')
        

    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name'}),validators=[validators.MaxLengthValidator(10,message='limit overflow'),validators.MinLengthValidator(5,message='enter more')])
    text = forms.CharField(widget=forms.TextInput,validators=[length])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}), validators=[validators.EmailValidator(message='enter a valid email')])
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter your age'}), validators=[validators.MinValueValidator(2,message='enter more than 2'),validators.MaxValueValidator(15,message='enter less value')])
    file= forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='enter pdf file')])
    # Regex, url, pattern validator



