from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from collections import defaultdict
from utils.cpf_verify import main as verify_cpf
import re


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    birth_date = models.DateField(
        verbose_name=_('Birth Date')
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='CPF',
    )
    address = models.CharField(
        max_length=100,
        verbose_name=_('Address'),
    )
    address_number = models.CharField(
        max_length=5,
        verbose_name=_('Address Number'),
    )
    address_complement = models.CharField(
        max_length=30,
        blank=True,
        default='',
        verbose_name=_('Address Complement'),
    )
    neighborhood = models.CharField(
        max_length=255,
        verbose_name=_('Neighborhood'),
    )
    cep = models.CharField(
        max_length=8,
        verbose_name='CEP',
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_('City'),
    )
    state = models.CharField(
        max_length=2,
        verbose_name=_('State'),
        choices=[
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        ],
    )

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    def clean(self, *args, **kwargs):
        error_messages = defaultdict(list)
        user_cpf = re.sub(r'[^0-9]', '', self.cpf)

        if len(user_cpf) != 11:
            error_messages['cpf'].append(
                _('CPF must have 11 characters, only numbers')
            )

        else:
            valid_cpf = verify_cpf(user_cpf)
            if not valid_cpf:
                error_messages['cpf'].append(
                    _('CPF Invalid')
                )

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('Users Profile')
