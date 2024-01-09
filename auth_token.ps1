$cred = gcloud auth print-access-token
$project_id = 'lab-gke-408602'
$baid = '013A7B-750280-649417'
$headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = $project_id }

Invoke-WebRequest `
    -Method GET `
    -Headers $headers `
    -Uri "https://iam.googleapis.com/v1/projects/$project_id/serviceAccounts" | Select-Object -Expand Content