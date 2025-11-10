# JobProgress

Progress information for a dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_step** | **str** | Current step in the processing pipeline. Possible values: - &#x60;initializing&#x60;: Setting up the job and preparing resources - &#x60;searching&#x60;: Finding relevant URLs based on the search query - &#x60;scraping&#x60;: Extracting data from discovered URLs - &#x60;processing&#x60;: Analyzing and structuring extracted data - &#x60;finalizing&#x60;: Preparing the final CSV output  | 
**rows_collected** | **int** | Number of data rows collected so far | 
**urls_processed** | **int** | Number of URLs processed so far | 
**urls_total** | **int** | Total number of URLs to process | 
**last_updated** | **datetime** | Timestamp of last progress update | 

## Example

```python
from qoery.models.job_progress import JobProgress

# TODO update the JSON string below
json = "{}"
# create an instance of JobProgress from a JSON string
job_progress_instance = JobProgress.from_json(json)
# print the JSON string representation of the object
print(JobProgress.to_json())

# convert the object into a dict
job_progress_dict = job_progress_instance.to_dict()
# create an instance of JobProgress from a dict
job_progress_from_dict = JobProgress.from_dict(job_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


