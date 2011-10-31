from django import forms
from django.utils.translation import ugettext_lazy as _
from cropper.models import Cropped, Original
import Image

class OriginalForm(forms.ModelForm):
    """
    Form class for uplaod images will be cropped
    """
    class Meta:
        model = Original

class CroppedForm(forms.ModelForm):
    """
    Form class for crop images
    """

    def __init__(self, *args, **kwargs):
        """
        The class contructor. Changes ``original`` widget field type to hidden
        """
        super(CroppedForm, self).__init__(*args, **kwargs)
        self.fields['original'].widget = forms.HiddenInput()

    def _dimension_clean(self, field, key, offset='not_exists'):
        """
        Form helper. Validates for cropped area offset left, offset top,
        area width and  height values.
        """
        value  = self.cleaned_data.get(key, 0)
        offset  = self.cleaned_data.get(offset, 0)
        original = self.cleaned_data.get('original')

        if not original:
            return value

        if value + offset > getattr(original, 'image_%s' % field):
            raise forms.ValidationError, _('Value exceeds picture dimension')

        return value

    def clean_x(self):
        """
        Validates for cropped area offset left
        """
        return self._dimension_clean('width', 'x')

    def clean_y(self):
        """
        Validates for cropped area offset top
        """
        return self._dimension_clean('height', 'y')

    def clean_w(self):
        """
        Validates for cropped area width
        """
        return self._dimension_clean('width', 'w', 'x')

    def clean_h(self):
        """
        Validates for cropped area height
        """
        return self._dimension_clean('height', 'h', 'y')

    class Meta:
        model = Cropped
