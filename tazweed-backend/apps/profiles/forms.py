from . import Seller, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email')

class SellerForm(forms.ModelForm):
    class Meta:
        model =Seller
        fields = ('shop')
        
        