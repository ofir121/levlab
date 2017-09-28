from django.db import models

# Create your models here.


class AluHyper (models.Model):
    id = models.IntegerField(primary_key=True)
    SampleCode = models.IntegerField(default=0)
    SampleType = models.TextField(max_length=100, default="NA")
    AVG_Norm = models.DecimalField(max_digits=100, decimal_places=2, default="0")
    contIndex = models.DecimalField(max_digits=100, decimal_places=2, default="0")

    def __str__(self):
        return str(self.SampleCode) + " - " + self.SampleType

    class Meta:
        verbose_name_plural = "AluHyper"



