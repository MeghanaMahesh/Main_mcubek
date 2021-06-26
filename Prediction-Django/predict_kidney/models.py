from django.db import models


class PredResults_kidney(models.Model):

    Patient_ID = models.IntegerField()
    Patient_Age = models.IntegerField()
    Patient_Gender = models.IntegerField()
    Patient_Name = models.CharField(max_length=255)
    '''
    BP = models.IntegerField()
    AL = models.IntegerField()
    PCV = models.IntegerField()
    PCC = models.IntegerField()
    BGR = models.IntegerField()
    BU = models.IntegerField()
    SC = models.IntegerField()
    HEMO = models.IntegerField()
    HTN = models.IntegerField()
    DM = models.IntegerField()
    APPET = models.IntegerField()
    SG = models.FloatField()
    SU = models.FloatField()
    RBC = models.FloatField()
    PC = models.FloatField()
    BA = models.FloatField()
    SOD = models.FloatField()
    POT = models.FloatField()
    WC = models.FloatField()
    RC = models.FloatField()
    CAD = models.FloatField()
    PE = models.FloatField()
    ANE = models.FloatField()
    '''
    Kidney_Disease = models.CharField(max_length=30)

    def __str__(self):
        return self.Kidney_Disease
