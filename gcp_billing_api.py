import requests
import json

# Documentation GCO
# https://cloud.google.com/billing/docs/reference/rest

# Install gcloud
#(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
#& $env:Temp\GoogleCloudSDKInstaller.exe

api_access_token = headers = "ya29.a0AfB_byBflp4M-nFc1dWL16MGbVMFYe8kTuf3uN9M73RGpePGM5hc37W3SaeDE1izPYCtrOznWbyTEcWzfxna3geO2ICKVFaPs3NK9crY-bLGzREo9Hpo33yt9oHcELyKIcU3jCy5xtrcCTpX4eBTdFVsKq8lvEEgpQYKWmKEHQaCgYKAVsSARASFQHGX2MiLYgmK__cEuQyj1vuvYt5_g0177"
project_id = "lab-gke-two"
billing_account_id = '0000-700000-649417'
api_base_url = "https://billingbudgets.googleapis.com"
headers = {
    'Authorization': f'Bearer {api_access_token}',
    'x-goog-user-project': project_id
}

url = f"https://iam.googleapis.com/v1/projects/{project_id}/serviceAccounts"
#url = f"{api_base_url}/v1/billingAccounts/{billing_account_id}/budgets'"
url = f"https://billingbudgets.googleapis.com/v1/billingAccounts/{billing_account_id}/budgets"
response = requests.get(url, headers=headers)
data = response.json()
print(json.dumps(response.json(), indent=2))
#print(data)