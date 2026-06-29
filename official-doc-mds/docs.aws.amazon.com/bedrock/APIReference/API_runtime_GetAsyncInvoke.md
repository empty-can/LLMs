

# GetAsyncInvoke
<a name="API_runtime_GetAsyncInvoke"></a>

Retrieve information about an asynchronous invocation.

## Request Syntax
<a name="API_runtime_GetAsyncInvoke_RequestSyntax"></a>

```
GET /async-invoke/{{invocationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_runtime_GetAsyncInvoke_RequestParameters"></a>

The request uses the following URI parameters.

 ** [invocationArn](#API_runtime_GetAsyncInvoke_RequestSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-request-uri-invocationArn"></a>
The invocation's ARN.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:async-invoke/[a-z0-9]{12}`   
Required: Yes

## Request Body
<a name="API_runtime_GetAsyncInvoke_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_runtime_GetAsyncInvoke_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientRequestToken": "string",
   "endTime": "string",
   "failureMessage": "string",
   "invocationArn": "string",
   "lastModifiedTime": "string",
   "modelArn": "string",
   "outputDataConfig": { ... },
   "status": "string",
   "submitTime": "string"
}
```

## Response Elements
<a name="API_runtime_GetAsyncInvoke_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientRequestToken](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-clientRequestToken"></a>
The invocation's idempotency token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[!-~]*` 

 ** [endTime](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-endTime"></a>
When the invocation ended.  
Type: Timestamp

 ** [failureMessage](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-failureMessage"></a>
An error message.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [invocationArn](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-invocationArn"></a>
The invocation's ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:async-invoke/[a-z0-9]{12}` 

 ** [lastModifiedTime](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-lastModifiedTime"></a>
The invocation's last modified time.  
Type: Timestamp

 ** [modelArn](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-modelArn"></a>
The invocation's model ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:[a-z0-9\-]+:bedrock:[a-z0-9\-]*:[0-9]*:(provisioned-model|foundation-model)/.+` 

 ** [outputDataConfig](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-outputDataConfig"></a>
Output data settings.  
Type: [AsyncInvokeOutputDataConfig](API_runtime_AsyncInvokeOutputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-status"></a>
The invocation's status.  
Type: String  
Valid Values: `InProgress | Completed | Failed` 

 ** [submitTime](#API_runtime_GetAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_GetAsyncInvoke-response-submitTime"></a>
When the invocation request was submitted.  
Type: Timestamp

## Errors
<a name="API_runtime_GetAsyncInvoke_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. For troubleshooting this error, see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide  
HTTP Status Code: 500

 ** ThrottlingException **   
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide  
HTTP Status Code: 400

## See Also
<a name="API_runtime_GetAsyncInvoke_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/GetAsyncInvoke) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GetAsyncInvoke) 