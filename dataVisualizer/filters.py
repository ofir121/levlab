from .models import AluHyper
from django_filters.views import FilterView
from django_tables2 import SingleTableView

class FilteredSamplesListView(FilterView, SingleTableView):
    table_class = AluHyper
    model = AluHyper
    template_name = 'tableView.html'

    filterset_class = SamplesFilter