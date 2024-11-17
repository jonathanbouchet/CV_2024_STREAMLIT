from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, field_serializer
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import streamlit as st

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

@st.cache_resource
def set_db() -> None:
    """set firebase credentials
    Retrieve the credentials needed to set up a firebase connection from Settings

    """
     # set Firestore Database credentials
    if not st.session_state["db_initialized"]:
        print("in set_db")
        config_firebase = FirebaseSettings()
        print(f"firebase config: {config_firebase}")
        config_firebase_deserialized = config_firebase.model_dump()
        # print(f"firebase config deserialized: {config_firebase_deserialized}")

        credential_values = {
            "type": config_firebase_deserialized.get("type"),
            "project_id": config_firebase_deserialized.get("project_id"),
            "private_key_id": config_firebase_deserialized.get("private_key_id"),
            "private_key": config_firebase_deserialized.get("private_key"),
            "client_email": config_firebase_deserialized.get("client_email"),
            "client_id": config_firebase_deserialized.get("client_id"),
            "auth_uri": config_firebase_deserialized.get("auth_uri"),
            "token_uri": config_firebase_deserialized.get("token_uri"),
            "auth_provider_x509_cert_url": config_firebase_deserialized.get("auth_provider_x509_cert_url"),
            "client_x509_cert_url": config_firebase_deserialized.get("client_x509_cert_url"),
            "universe_domain": config_firebase_deserialized.get("universe_domain"),
        }
        cred = credentials.Certificate(credential_values)
        firebase_admin.initialize_app(cred)
        st.session_state["db_initialized"] = True

    # firebase_admin.initialize_app(cred,  {"storageBucket": credential_values["storageBucket"]})


def write_to_db(payload: dict, collection_name: str) -> str:
    """write user comment to database

    :param dict payload: _description_
    :param str collection_name: _description_
    :return str: _description_
    """
    if st.session_state["db_initialized"]:
        # print(f"in write_to_db, payload: {payload}, db col: {collection_name}")
        try:
            db = firestore.client()
            doc_ref = db.collection(f"{collection_name}").document()  # create a new document.ID
            doc_ref.set(payload)  # add obj to collection
            db.close()
            return "comment submitted"
        except Exception as e:
            print(e)
            return e
    else:
        print("database not initialized")