

# ListBrowsers
<a name="API_ListBrowsers"></a>

Lists all custom browsers in your account.

## Request Syntax
<a name="API_ListBrowsers_RequestSyntax"></a>

```
POST /browsers?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBrowsers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListBrowsers_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListBrowsers-request-uri-maxResults"></a>
The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListBrowsers_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListBrowsers-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [type](#API_ListBrowsers_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListBrowsers-request-uri-type"></a>
The type of browsers to list. If not specified, all browser types are returned.  
Valid Values: `SYSTEM | CUSTOM` 

## Request Body
<a name="API_ListBrowsers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBrowsers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserSummaries": [ 
      { 
         "browserArn": "string",
         "browserId": "string",
         "createdAt": "string",
         "description": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBrowsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserSummaries](#API_ListBrowsers_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListBrowsers-response-browserSummaries"></a>
The list of browser summaries.  
Type: Array of [BrowserSummary](API_BrowserSummary.md) objects

 ** [nextToken](#API_ListBrowsers_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListBrowsers-response-nextToken"></a>
A token to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListBrowsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListBrowsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListBrowsers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListBrowsers) 