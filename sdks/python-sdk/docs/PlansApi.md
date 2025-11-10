# qoery.PlansApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_plans**](PlansApi.md#list_plans) | **GET** /v0/plans | List subscription plans and endpoint limits


# **list_plans**
> ListPlans200Response list_plans()

List subscription plans and endpoint limits

Returns all available subscription plans with pricing metadata,
monthly limits per endpoint, and other plan features.

**Plan Features:**
- Each plan includes different monthly quotas per endpoint
- Limits reset on the 1st of each month
- Plans can be upgraded/downgraded at any time
- Annual billing offers discounts compared to monthly billing


### Example


```python
import qoery
from qoery.models.list_plans200_response import ListPlans200Response
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)


# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.PlansApi(api_client)

    try:
        # List subscription plans and endpoint limits
        api_response = api_instance.list_plans()
        print("The response of PlansApi->list_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->list_plans: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListPlans200Response**](ListPlans200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plans and limits |  -  |
**500** | Failed to load plans from database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

