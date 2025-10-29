# Qoery.QueriesApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryNlGet**](QueriesApi.md#queryNlGet) | **GET** /query/nl | Natural Language Query



## queryNlGet

> QueryNlGet200Response queryNlGet(query, opts)

Natural Language Query

We search the public web for the most relevant sources to your query, extract structured data, and return curated series.  How it works: - We query the web and fetch the top &#x60;num_results&#x60; relevant pages. - We always extract tabular/JSON-like data when available. - If &#x60;paragraph_extraction&#x60; is true, we scan prose paragraphs to identify statistics and convert them into series (e.g., \&quot;In 2000, there were 5,000 Swedes in Norway; in 2020, 50,000\&quot; → year/value pairs). - If &#x60;plot2table&#x60; &gt; 0, we analyze images of plots and extract their underlying datapoints.  Credits: - Base credits &#x3D; ceil(num_results / 10), minimum 1. - Paragraph extraction surcharge &#x3D; +1 credit when &#x60;paragraph_extraction&#x60; is true. - Plot2Table credits &#x3D; 1 per chart processed when &#x60;plot2table&#x60; &gt; 0. 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Qoery.QueriesApi();
let query = "query_example"; // String | Natural language query
let opts = {
  'numResults': 10, // Number | Number of top relevant pages to fetch and process
  'paragraphExtraction': false, // Boolean | Extract statistics from paragraph text and convert to structured series (year/value pairs)
  'plot2table': 0 // Number | Number of plot images to analyze and convert into raw datapoints
};
apiInstance.queryNlGet(query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| Natural language query | 
 **numResults** | **Number**| Number of top relevant pages to fetch and process | [optional] [default to 10]
 **paragraphExtraction** | **Boolean**| Extract statistics from paragraph text and convert to structured series (year/value pairs) | [optional] [default to false]
 **plot2table** | **Number**| Number of plot images to analyze and convert into raw datapoints | [optional] [default to 0]

### Return type

[**QueryNlGet200Response**](QueryNlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

