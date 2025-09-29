# Qoery.QueriesApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryNlGet**](QueriesApi.md#queryNlGet) | **GET** /query/nl | Natural Language Query (query string)
[**queryNlPost**](QueriesApi.md#queryNlPost) | **POST** /query/nl | Natural Language Query
[**querySqlGet**](QueriesApi.md#querySqlGet) | **GET** /query/sql | SQL Query (query string)
[**querySqlPost**](QueriesApi.md#querySqlPost) | **POST** /query/sql | SQL Query



## queryNlGet

> QueryNlGet200Response queryNlGet(opts)

Natural Language Query (query string)

Submit a natural-language request using query parameters. This is a convenience alias of POST.

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
  'query': "query_example" // String | Natural language query
};
apiInstance.queryNlGet(opts, (error, data, response) => {
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
 **query** | **String**| Natural language query | [optional] 

### Return type

[**QueryNlGet200Response**](QueryNlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryNlPost

> QueryNlGet200Response queryNlPost(opts)

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

[**QueryNlGet200Response**](QueryNlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## querySqlGet

> QuerySqlGet200Response querySqlGet(opts)

SQL Query (query string)

Execute a read-only SELECT query using query parameters. This is a convenience alias of POST.

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
  'sqlQuery': "sqlQuery_example" // String | SQL query to execute (read-only)
};
apiInstance.querySqlGet(opts, (error, data, response) => {
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
 **sqlQuery** | **String**| SQL query to execute (read-only) | [optional] 

### Return type

[**QuerySqlGet200Response**](QuerySqlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## querySqlPost

> QuerySqlGet200Response querySqlPost(opts)

SQL Query

Execute a read-only SELECT query and receive the results as curated time series. This endpoint does not return SQL.

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
  'querySqlPostRequest': new Qoery.QuerySqlPostRequest() // QuerySqlPostRequest | Provide JSON body or use query parameter 'sql_query'. Body takes precedence.
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
 **querySqlPostRequest** | [**QuerySqlPostRequest**](QuerySqlPostRequest.md)| Provide JSON body or use query parameter &#39;sql_query&#39;. Body takes precedence. | [optional] 

### Return type

[**QuerySqlGet200Response**](QuerySqlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

