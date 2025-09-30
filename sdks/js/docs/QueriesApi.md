# Qoery.QueriesApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryNlPost**](QueriesApi.md#queryNlPost) | **POST** /query/nl | Natural Language Query
[**querySqlPost**](QueriesApi.md#querySqlPost) | **POST** /query/sql | SQL Query



## queryNlPost

> QueryNlPost200Response queryNlPost(opts)

Natural Language Query

Submit a natural-language request and get back a curated time series response. The response also includes the generated SQL so you can switch to the SQL endpoint for faster/cheaper repeated queries.

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
let opts = {
  'queryNlPostRequest': new Qoery.QueryNlPostRequest() // QueryNlPostRequest | Provide JSON body or use query parameter 'query'. Body takes precedence.
};
apiInstance.queryNlPost(opts, (error, data, response) => {
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
 **queryNlPostRequest** | [**QueryNlPostRequest**](QueryNlPostRequest.md)| Provide JSON body or use query parameter &#39;query&#39;. Body takes precedence. | [optional] 

### Return type

[**QueryNlPost200Response**](QueryNlPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## querySqlPost

> QuerySqlPost200Response querySqlPost(opts)

SQL Query

Execute a read-only SELECT query and receive the results as curated time series. The response includes the executed SQL query and optional metadata.

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
let opts = {
  'querySqlPostRequest': new Qoery.QuerySqlPostRequest() // QuerySqlPostRequest | Provide JSON body with 'query' or 'sql_query' field, or use query parameters. Body takes precedence.
};
apiInstance.querySqlPost(opts, (error, data, response) => {
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
 **querySqlPostRequest** | [**QuerySqlPostRequest**](QuerySqlPostRequest.md)| Provide JSON body with &#39;query&#39; or &#39;sql_query&#39; field, or use query parameters. Body takes precedence. | [optional] 

### Return type

[**QuerySqlPost200Response**](QuerySqlPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

