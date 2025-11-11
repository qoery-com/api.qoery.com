import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.DatasetsApi(api_client)
    
    # Start job
    job = api.start_dataset_job(search="climate change")
    print(f"Job ID: {job.job_id}")
    
    # Get status
    status = api.get_dataset_job_status(job.job_id)
    print(f"Status: {status.status}")
    
    # Download CSV
    csv = api.download_dataset_csv(job.job_id)
    print(f"CSV: {len(csv)} bytes")
