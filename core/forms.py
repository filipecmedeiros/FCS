from django import forms

from django.core.mail import send_mail
from django.conf import settings

class DoubtForm (forms.Form):

	name = forms.CharField(label='Nome')
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea())

	def send_mail(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		message = self.cleaned_data['message']
		message = 'Nome: {0}\nEmail:{1}\n{2}'.format(name, email,message)
		send_mail('FCS Advogados Associados [Dúvida]', message, settings.DEFAULT_FROM_EMAIL,
			[settings.EMAIL_TO]
		)
		return True