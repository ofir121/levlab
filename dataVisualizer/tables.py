import django_tables2 as tables
from .models import AluHyper


class SamplesTable(tables.Table):
    class Meta:
        model = AluHyper
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table'}

