# -*- coding: utf-8 -*-

import django_filters
from lmhsweb.models import Main, TYPE_CHOICES, SOURCES_CHOICES, Projet, Auteur
from django.db.models.fields import BLANK_CHOICE_DASH
from collections import Iterable
from itertools import chain
from re import search, sub
from django_filters.widgets import BaseCSVWidget, CSVWidget
from django_filters.fields import BaseCSVField
from django_filters.filters import Filter
from dal import autocomplete
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.db.models.constants import LOOKUP_SEP
from django.utils.encoding import force_text


class customCSVWidget(forms.Widget):
    def _isiterable(self, value):
        return isinstance(value, Iterable) and not isinstance(value, str)

    def value_from_datadict(self, data, files, name):
        value = super(customCSVWidget,self).value_from_datadict(data, files, name)

        if value is not None:
            if value == '':  # empty value should parse as an empty list
                return []
            return value.split(' ')
        return None

    def render(self, name, value, attrs=None):
        if not self._isiterable(value):
            value = [value]

        if len(value) <= 1:
            # delegate to main widget (Select, etc...) if not multiple values
            value = value[0] if value else ''
            return super(customCSVWidget,self).render(name, value, attrs)

        # if we have multiple values, we need to force render as a text input
        # (otherwise, the additional values are lost)
        surrogate = forms.TextInput()
        value = [force_text(surrogate._format_value(v)) for v in value]
        value = ' '.join(list(value))

        return surrogate.render(name, value, attrs)


class customCSVField(forms.Field):
    """
    Base field for validating CSV types. Value validation is performed by
    secondary base classes.
    ex::
        class IntegerCSVField(BaseCSVField, filters.IntegerField):
            pass
    """
    base_widget_class = customCSVWidget

    def __init__(self, *args, **kwargs):
        widget = kwargs.get('widget') or self.widget
        kwargs['widget'] = self._get_widget_class(widget)

        super(customCSVField,self).__init__(*args, **kwargs)

    def _get_widget_class(self, widget):
        # passthrough, allows for override
        if isinstance(widget, BaseCSVWidget) or (
                isinstance(widget, type) and
                issubclass(widget, BaseCSVWidget)):
            return widget

        # complain since we are unable to reconstruct widget instances
        assert isinstance(widget, type), \
            "'%s.widget' must be a widget class, not %s." \
            % (self.__class__.__name__, repr(widget))

        bases = (self.base_widget_class, widget, )
        return type(str('CSV%s' % widget.__name__), bases, {})

    def clean(self, value):
        if value is None:
            return None
        return [super(customCSVField, self).clean(v) for v in value]


class customCSVFilter(Filter):
    """
    Base class for CSV type filters, such as IN and RANGE.
    """
    base_field_class = customCSVField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('help_text', _('Multiple values may be separated by spaces.'))
        super(customCSVFilter,self).__init__(*args, **kwargs)

        class ConcreteCSVField(self.base_field_class, self.field_class):
            pass
        ConcreteCSVField.__name__ = self._field_class_name(
            self.field_class, self.lookup_expr
        )

        self.field_class = ConcreteCSVField

    @classmethod
    def _field_class_name(cls, field_class, lookup_expr):
        """
        Generate a suitable class name for the concrete field class. This is not
        completely reliable, as not all field class names are of the format
        <Type>Field.
        ex::
            BaseCSVFilter._field_class_name(DateTimeField, 'year__in')
            returns 'DateTimeYearInField'
        """
        # DateTimeField => DateTime
        type_name = field_class.__name__
        if type_name.endswith('Field'):
            type_name = type_name[:-5]

        # year__in => YearIn
        parts = lookup_expr.split(LOOKUP_SEP)
        expression_name = ''.join(p.capitalize() for p in parts)

        # DateTimeYearInField
        return str('%s%sField' % (type_name, expression_name))


class MultiValueCharFilter(customCSVFilter, django_filters.CharFilter):
    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs


class MainFilter(django_filters.FilterSet):

    PROJECT_CHOICES = Projet.objects.all().values_list("nom", "nom")
    PROJECT_CHOICES_FILTER = BLANK_CHOICE_DASH + list(PROJECT_CHOICES)
    TYPE_CHOICES_FILTER = BLANK_CHOICE_DASH + list(TYPE_CHOICES)
    SOURCES_CHOICES_FILTER = BLANK_CHOICE_DASH + list(SOURCES_CHOICES)

    auteur__nom = MultiValueCharFilter(name="auteur__nom", label='Auteur', lookup_expr='icontains')
    titre = MultiValueCharFilter(name="titre", label='Titre', lookup_expr='icontains')
    date = django_filters.CharFilter(label="Date", lookup_expr='icontains')
    mot_cle__nom = MultiValueCharFilter(name="mot_cle__nom",label="Mot clé", lookup_expr='icontains')
    pdf_text = django_filters.CharFilter(label="Recherche plein texte", lookup_expr='icontains')
    source_liste = django_filters.ChoiceFilter(name = 'source', label = "Source (choisir)", choices = SOURCES_CHOICES_FILTER, lookup_expr='icontains')
    source_texte = django_filters.CharFilter(name = 'source', label = "Source (écrire)", lookup_expr='icontains')
    projet__nom = django_filters.ChoiceFilter(label="Projet", choices=PROJECT_CHOICES_FILTER, lookup_expr='icontains')
    type = django_filters.ChoiceFilter(label="Type", choices=TYPE_CHOICES_FILTER, lookup_expr='icontains')
    cote_calcul = django_filters.CharFilter(label = "Cote", lookup_expr='iexact')
   # auteur__cote = django_filters.CharFilter(label = "Cote Auteur", lookup_expr='iexact')

    class Meta:
        model = Main
        fields = [
            'auteur__nom',
            'titre',
            'date',
            'mot_cle__nom',
            'pdf_text',
            'source_liste',
            'source_texte',
            'projet__nom',
            'type',
            'cote_calcul',
          #  'auteur__cote'
        ]
