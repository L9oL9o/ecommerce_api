from django.db.models import Model, DateTimeField, CharField


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class Gender(Model):
#     gender = CharField(max_length=55)
#
#     class Meta:
#         abstract = True

class Gender(Model):
    gender = CharField(max_length=55)

    class Meta:
        abstract = True