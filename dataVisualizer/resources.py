from import_export import resources
from .models import AluHyper


class AluResource(resources.ModelResource):
    class Meta:
        model = AluHyper
        fields = ('SampleCode', 'SampleType', 'AVG_Norm','contIndex')
