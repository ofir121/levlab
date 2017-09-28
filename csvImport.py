import tablib
from import_export import resources
from dataVisualizer.resources import AluResource

alu_resource = resources.modelresource_factory(model=AluResource)()
dataset = tablib.Dataset(['','', 'New book', 'Bla', 'Bla'], headers=['id', 'SampleCode', 'SampleType', 'AVG_Norm', 'contIndex'])
result = alu_resource.import_data(dataset, dry_run=True)
print(result.has_errors())
result = alu_resource.import_data(dataset, dry_run=False)

dataset = AluResource().export()
print (dataset.csv)


