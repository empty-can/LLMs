

# ListAgentRuntimeEndpoints
<a name="API_ListAgentRuntimeEndpoints"></a>

Lists all endpoints for a specific Amazon Secure Agent.

## Request Syntax
<a name="API_ListAgentRuntimeEndpoints_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeId}}/runtime-endpoints/?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAgentRuntimeEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeId](#API_ListAgentRuntimeEndpoints_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListAgentRuntimeEndpoints-request-uri-agentRuntimeId"></a>
The unique identifier of the AgentCore Runtime to list endpoints for.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [maxResults](#API_ListAgentRuntimeEndpoints_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListAgentRuntimeEndpoints-request-uri-maxResults"></a>
The maximum number of results to return in the response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAgentRuntimeEndpoints_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListAgentRuntimeEndpoints-request-uri-nextToken"></a>
A token to retrieve the next page of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListAgentRuntimeEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAgentRuntimeEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "runtimeEndpoints": [ 
      { 
         "agentRuntimeArn": "string",
         "agentRuntimeEndpointArn": "string",
         "createdAt": "string",
         "description": "string",
         "id": "string",
         "lastUpdatedAt": "string",
         "liveVersion": "string",
         "name": "string",
         "status": "string",
         "targetVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAgentRuntimeEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAgentRuntimeEndpoints_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListAgentRuntimeEndpoints-response-nextToken"></a>
A token to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [runtimeEndpoints](#API_ListAgentRuntimeEndpoints_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListAgentRuntimeEndpoints-response-runtimeEndpoints"></a>
The list of AgentCore Runtime endpoints.  
Type: Array of [AgentRuntimeEndpoint](API_AgentRuntimeEndpoint.md) objects

## Errors
<a name="API_ListAgentRuntimeEndpoints_Errors"></a>

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
<a name="API_ListAgentRuntimeEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListAgentRuntimeEndpoints) 