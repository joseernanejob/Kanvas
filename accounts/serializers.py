from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Account:
        if validated_data["is_superuser"]:
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)

    class Meta:
        model = Account
        fields = ["id", "email", "username", "password", "is_superuser"]
        extra_kwargs = {
            "username": {
                "validators": {
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="A user with that username already exists.",
                    )
                }
            },
            "email": {
                "validators": {
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="user with this email already exists.",
                    )
                }
            },
            "password": {"write_only": True},
        }
