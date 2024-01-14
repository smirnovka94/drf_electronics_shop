from rest_framework.serializers import ValidationError


class Status_Link_In_LinkValidator:
    """Запрет на ввод поставщика для завода"""
    def __call__(self, attrs):
        status_link = attrs.get('status_link')
        related_link = attrs.get('related_link')
        if status_link == "FA" and related_link is not None:
            raise ValidationError("У завода не может быть поставщика")
