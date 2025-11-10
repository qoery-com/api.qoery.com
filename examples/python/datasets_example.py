import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.DatasetsApi(api_client)
    
    # Start job
    job = api.v0_datasets_post(qoery.V0DatasetsPostRequest(search="climate change"))
    print(f"Job ID: {job.job_id}")
    
    # Get status
    status = api.v0_datasets_job_id_get(job.job_id)
    print(f"Status: {status.status}")
    
    # Download CSV
    csv = api.v0_datasets_job_id_csv_get(job.job_id)
    print(f"CSV: {len(csv)} bytes")
