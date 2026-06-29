

# ListRegistries
<a name="API_ListRegistries"></a>

Lists all registries in the account. You can optionally filter results by status using the `status` parameter, or by authorizer type using the `authorizerType` parameter.

## Request Syntax
<a name="API_ListRegistries_RequestSyntax"></a>

```
GET /registries?authorizerType={{authorizerType}}&maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRegistries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authorizerType](#API_ListRegistries_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistries-request-uri-authorizerType"></a>
Filter registries by their authorizer type. Possible values are `CUSTOM_JWT` and `AWS_IAM`. For more information about authorizer types, see the `RegistryAuthorizerType` enum.  
Valid Values: `CUSTOM_JWT | AWS_IAM` 

 ** [maxResults](#API_ListRegistries_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistries-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListRegistries_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistries-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [status](#API_ListRegistries_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistries-request-uri-status"></a>
Filter registries by their current status. Possible values include `CREATING`, `READY`, `UPDATING`, `CREATE_FAILED`, `UPDATE_FAILED`, `DELETING`, and `DELETE_FAILED`.  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

## Request Body
<a name="API_ListRegistries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRegistries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "registries": [ 
      { 
         "authorizerType": "string",
         "createdAt": "string",
         "description": "string",
         "name": "string",
         "registryArn": "string",
         "registryId": "string",
         "status": "string",
         "statusReason": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRegistries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRegistries_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListRegistries-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [registries](#API_ListRegistries_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListRegistries-response-registries"></a>
The list of registry summaries. For details about the fields in each summary, see the `RegistrySummary` data type.  
Type: Array of [RegistrySummary](API_RegistrySummary.md) objects

## Errors
<a name="API_ListRegistries_Errors"></a>

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
<a name="API_ListRegistries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListRegistries) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListRegistries) 