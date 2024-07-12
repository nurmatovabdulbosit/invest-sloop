from import_export.signals import pre_import

@receiver(pre_import, sender=HorijiyResource)
def pre_import_signal(sender, instance, **kwargs):
    request = kwargs['request']
    instance.before_import_row_kwargs = {'user': request.user}
