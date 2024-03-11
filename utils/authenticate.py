from google.oauth2 import service_account
import google.auth

def gcp_authenticate():
    # Set the path to your service account key file
    key_file_path = 'GenAI_and_LLMOps/genai-416507-3a3b00be5e42.json'

    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(key_file_path)

    # Obtain the project ID from the credentials
    project_id = credentials.project_id

    return credentials, project_id
