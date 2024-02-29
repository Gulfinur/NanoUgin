from django.contrib import admin

from .models import DeviceType
from .models import DeviceModel
from .models import Device
from .models import All_Parameters

admin.site.register(DeviceType)
admin.site.register(DeviceModel)
admin.site.register(Device)
admin.site.register(All_Parameters)