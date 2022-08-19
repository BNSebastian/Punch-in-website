from django import forms
from django.forms import ModelForm
from .models import jobs

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'
    
class pontajForm(ModelForm):
    reasons = [
        ("Traveling", "Traveling"),
        ("Office work", "Office work"),
        ("Repairing wind turbine", "Repairing wind turbine")
    ]        
    reason = forms.ChoiceField(choices=reasons) 
    description = forms.CharField(required=False)
    start_date = forms.DateInput()
    
    def __init__(self, *args, **kwargs):
        super(pontajForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control' 
               
    class Meta:
        model = jobs
        # fields = "_all_"
        fields = (
            'reason',
            'date', 
            'start_date', 
            'end_date', 
            'description',
        )  
        widgets = {
            'date': DateInput(),
            'start_date': TimeInput(),
            'end_date': TimeInput(),
        }

# class pontajForm(ModelForm):
#     class Meta:
#         model = jobs
#         # fields = "_all_"
#         fields = (
#             'reason', 
#             'start_date', 
#             'end_date', 
#             'description',
#         )
#         reasons = [
#         ("Office work", "Office work"),
#         ("Traveling", "Traveling"),
#         ("Repairing a wind turbine", "Repairing a wind turbine")            
#         ]
#         widgets = {
#             'reason': forms.SelectMultiple(choices = reasons),
            
#             # 'user': forms.HiddenInput(),
#         }

        
    # reasons = [
    #     ("1", "Office work"),
    #     ("2", "Traveling"),
    #     ("3", "Repairing wind turbine")
    # ]        
    # reason = forms.ChoiceField(choices=reasons)
    # start = forms.DateField() 
    # end = forms.DateField() 
    # description = forms.CharField(max_length=255,)
    
    # user_id = forms.IntegerField(
    #     # widget=forms.HiddenInput(),
        
    #     )
    # # email = forms.EmailField()

