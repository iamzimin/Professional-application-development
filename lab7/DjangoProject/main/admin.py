from django.contrib import admin
from .models import CallHistory
from .models import ClientInfo
from .models import ClientGroup
from .models import Bank
from .models import BankType

admin.site.register(CallHistory)
admin.site.register(ClientInfo)
admin.site.register(ClientGroup)
admin.site.register(Bank)
admin.site.register(BankType)
