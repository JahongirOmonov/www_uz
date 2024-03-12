from django.db import models


class Operation_systems(models.TextChoices):
    WINDOWS = 'Windows'
    IOS = 'iOS'
    ANDROID = 'Android'
    AIX = 'Aix'
    OTHERS = 'Qolganlari'

class Browsers(models.TextChoices):
    MOBILE_SAFARI = 'Mobil safari'
    CHROME_MOBILE = 'Chrome Mobile'
    CHROME = 'Chrome'
    BONE_LINKCHECKER = '2Bone Linkchecker'
    OTHERS = 'Qolganlari'

