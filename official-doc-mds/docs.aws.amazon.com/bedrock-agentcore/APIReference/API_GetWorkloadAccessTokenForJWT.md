

# GetWorkloadAccessTokenForJWT
<a name="API_GetWorkloadAccessTokenForJWT"></a>

Obtains a workload access token for agentic workloads acting on behalf of a user, using a JWT token.

## Request Syntax
<a name="API_GetWorkloadAccessTokenForJWT_RequestSyntax"></a>

```
POST /identities/GetWorkloadAccessTokenForJWT HTTP/1.1
Content-type: application/json

{
   "userToken": "{{string}}",
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWorkloadAccessTokenForJWT_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWorkloadAccessTokenForJWT_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [userToken](#API_GetWorkloadAccessTokenForJWT_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForJWT-request-userToken"></a>
The OAuth 2.0 token issued by the user's identity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`   
Required: Yes

 ** [workloadName](#API_GetWorkloadAccessTokenForJWT_RequestSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForJWT-request-workloadName"></a>
The unique identifier for the registered workload.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: Yes

## Response Syntax
<a name="API_GetWorkloadAccessTokenForJWT_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workloadAccessToken": "string"
}
```

## Response Elements
<a name="API_GetWorkloadAccessTokenForJWT_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workloadAccessToken](#API_GetWorkloadAccessTokenForJWT_ResponseSyntax) **   <a name="BedrockAgentCore-GetWorkloadAccessTokenForJWT-response-workloadAccessToken"></a>
An opaque token representing the identity of both the workload and the user.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.

## Errors
<a name="API_GetWorkloadAccessTokenForJWT_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_GetWorkloadAccessTokenForJWT_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetWorkloadAccessTokenForJWT) 