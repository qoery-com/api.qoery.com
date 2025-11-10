# Qoery.JobProgress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentStep** | **String** | Current step in the processing pipeline. Possible values: - &#x60;initializing&#x60;: Setting up the job and preparing resources - &#x60;searching&#x60;: Finding relevant URLs based on the search query - &#x60;scraping&#x60;: Extracting data from discovered URLs - &#x60;processing&#x60;: Analyzing and structuring extracted data - &#x60;finalizing&#x60;: Preparing the final CSV output  | 
**rowsCollected** | **Number** | Number of data rows collected so far | 
**urlsProcessed** | **Number** | Number of URLs processed so far | 
**urlsTotal** | **Number** | Total number of URLs to process | 
**lastUpdated** | **Date** | Timestamp of last progress update | 


