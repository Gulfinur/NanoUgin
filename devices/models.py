from django.db import models


class All_Parameters(models.Model):
    name_parameter = models.CharField(max_length=200, default='SOME STRING')
    def __str__(self):
        return self.name_parameter


class DeviceType(models.Model):
    # id_type = models.IntegerField(default=0)
    name_type = models.CharField(max_length=200, default='SOME STRING')
    parameters = models.ManyToManyField(All_Parameters)
    def create(self):
        self.save()
    def __str__(self):
        return self.name_type


class DeviceModel(models.Model):
    id_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    name_model = models.CharField(max_length=200, default='SOME STRING')

    def __str__(self):
        return self.name_model


class Device(models.Model):
    Type_device = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    #queryset = DeviceType.objects.all(name_type=Type_device)

    def __str__(self):
        return self.Type_device

# class Parameter(models.Model):
# id_device = models.ForeignKey(Device, on_delete=models.CASCADE)
# id_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
# id_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
