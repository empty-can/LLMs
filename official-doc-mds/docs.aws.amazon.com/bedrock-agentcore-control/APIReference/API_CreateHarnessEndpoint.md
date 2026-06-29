

# CreateHarnessEndpoint
<a name="API_CreateHarnessEndpoint"></a>

Operation to create a harness endpoint.

## Request Syntax
<a name="API_CreateHarnessEndpoint_RequestSyntax"></a>

```
POST /harnesses/{{harnessId}}/endpoints HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "endpointName": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "targetVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateHarnessEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [harnessId](#API_CreateHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-request-uri-harnessId"></a>
The ID of the harness to create an endpoint for.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_CreateHarnessEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-request-description"></a>
A description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** [endpointName](#API_CreateHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-request-endpointName"></a>
The name of the endpoint. Must start with a letter and contain only alphanumeric characters and underscores.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [tags](#API_CreateHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-request-tags"></a>
Tags to apply to the endpoint resource.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [targetVersion](#API_CreateHarnessEndpoint_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-request-targetVersion"></a>
The harness version that the endpoint points to and serves invocations from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: No

## Response Syntax
<a name="API_CreateHarnessEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "endpoint": { 
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
}
```

## Response Elements
<a name="API_CreateHarnessEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_CreateHarnessEndpoint_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateHarnessEndpoint-response-endpoint"></a>
The endpoint that was created.  
Type: [HarnessEndpoint](API_HarnessEndpoint.md) object

## Errors
<a name="API_CreateHarnessEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateHarnessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateHarnessEndpoint) 