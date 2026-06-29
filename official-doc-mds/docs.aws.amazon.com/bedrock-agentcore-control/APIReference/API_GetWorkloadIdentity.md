

# GetWorkloadIdentity
<a name="API_GetWorkloadIdentity"></a>

Retrieves information about a workload identity.

## Request Syntax
<a name="API_GetWorkloadIdentity_RequestSyntax"></a>

```
POST /identities/GetWorkloadIdentity HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWorkloadIdentity_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWorkloadIdentity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_GetWorkloadIdentity_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetWorkloadIdentity-request-name"></a>
The name of the workload identity to retrieve.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: Yes

## Response Syntax
<a name="API_GetWorkloadIdentity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowedResourceOauth2ReturnUrls": [ "string" ],
   "createdTime": number,
   "lastUpdatedTime": number,
   "name": "string",
   "workloadIdentityArn": "string"
}
```

## Response Elements
<a name="API_GetWorkloadIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowedResourceOauth2ReturnUrls](#API_GetWorkloadIdentity_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetWorkloadIdentity-response-allowedResourceOauth2ReturnUrls"></a>
The list of allowed OAuth2 return URLs for resources associated with this workload identity.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\w+:(\/?\/?)[^\s]+` 

 ** [createdTime](#API_GetWorkloadIdentity_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetWorkloadIdentity-response-createdTime"></a>
The timestamp when the workload identity was created.  
Type: Timestamp

 ** [lastUpdatedTime](#API_GetWorkloadIdentity_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetWorkloadIdentity-response-lastUpdatedTime"></a>
The timestamp when the workload identity was last updated.  
Type: Timestamp

 ** [name](#API_GetWorkloadIdentity_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetWorkloadIdentity-response-name"></a>
The name of the workload identity.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+` 

 ** [workloadIdentityArn](#API_GetWorkloadIdentity_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetWorkloadIdentity-response-workloadIdentityArn"></a>
The Amazon Resource Name (ARN) of the workload identity.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetWorkloadIdentity_Errors"></a>

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

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetWorkloadIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetWorkloadIdentity) 