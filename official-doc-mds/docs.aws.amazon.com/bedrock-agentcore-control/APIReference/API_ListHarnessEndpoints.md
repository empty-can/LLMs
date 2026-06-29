

# ListHarnessEndpoints
<a name="API_ListHarnessEndpoints"></a>

Operation to list the endpoints of a harness.

## Request Syntax
<a name="API_ListHarnessEndpoints_RequestSyntax"></a>

```
GET /harnesses/{{harnessId}}/endpoints?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHarnessEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [harnessId](#API_ListHarnessEndpoints_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListHarnessEndpoints-request-uri-harnessId"></a>
The ID of the harness whose endpoints are listed.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [maxResults](#API_ListHarnessEndpoints_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListHarnessEndpoints-request-uri-maxResults"></a>
The maximum number of results to return in a single call.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListHarnessEndpoints_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListHarnessEndpoints-request-uri-nextToken"></a>
The token for the next set of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListHarnessEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHarnessEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpoints": [ 
      { 
         "arn": "string",
         "createdAt": "string",
         "description": "string",
         "endpointName": "string",
         "failureReason": "string",
         "harnessId": "string",
         "harnessName": "string",
         "liveVersion": "string",
         "status": "string",
         "targetVersion": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListHarnessEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoints](#API_ListHarnessEndpoints_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListHarnessEndpoints-response-endpoints"></a>
The list of harness endpoints.  
Type: Array of [HarnessEndpoint](API_HarnessEndpoint.md) objects

 ** [nextToken](#API_ListHarnessEndpoints_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListHarnessEndpoints-response-nextToken"></a>
The token for the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListHarnessEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListHarnessEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListHarnessEndpoints) 