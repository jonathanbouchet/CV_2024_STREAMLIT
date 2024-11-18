from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, field_serializer

class FirebaseSettings(BaseSettings):
    """model to define the firebase connection settings

    :param  BaseSettings:
    """
    type : str| None = None
    project_id: SecretStr | None = None
    private_key_id: SecretStr | None = None
    private_key: SecretStr| None = None
    client_email: SecretStr| None = None
    client_id: SecretStr| None = None
    auth_uri: str| None = None
    token_uri: str| None = None
    auth_provider_x509_cert_url: str| None = None
    client_x509_cert_url: SecretStr| None = None
    universe_domain: str| None = None

    model_config = SettingsConfigDict(env_file=".env.firebase")

    @field_serializer('project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'client_x509_cert_url')
    def dump_secret(self, v):
        return v.get_secret_value()