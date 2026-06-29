

# StartAsyncInvoke
<a name="API_runtime_StartAsyncInvoke"></a>

Starts an asynchronous invocation.

This operation requires permission for the `bedrock:InvokeModel` action.

**Important**  
To deny all inference access to resources that you specify in the modelId field, you need to deny access to the `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` actions. Doing this also denies access to the resource through the Converse API actions ([Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) and [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)). For more information see [Deny access for inference on specific models](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference). 

## Request Syntax
<a name="API_runtime_StartAsyncInvoke_RequestSyntax"></a>

```
POST /async-invoke HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "modelId": "{{string}}",
   "modelInput": {{JSON value}},
   "outputDataConfig": { ... },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_runtime_StartAsyncInvoke_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_runtime_StartAsyncInvoke_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_runtime_StartAsyncInvoke_RequestSyntax) **   <a name="bedrock-runtime_StartAsyncInvoke-request-clientRequestToken"></a>
Specify idempotency token to ensure that requests are not duplicated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[!-~]*`   
Required: No

 ** [modelId](#API_runtime_StartAsyncInvoke_RequestSyntax) **   <a name="bedrock-runtime_StartAsyncInvoke-request-modelId"></a>
The model to invoke.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z_\.\-/0-9:]+`   
Required: Yes

 ** [modelInput](#API_runtime_StartAsyncInvoke_RequestSyntax) **   <a name="bedrock-runtime_StartAsyncInvoke-request-modelInput"></a>
Input to send to the model.  
Type: JSON value  
Required: Yes

 ** [outputDataConfig](#API_runtime_StartAsyncInvoke_RequestSyntax) **   <a name="bedrock-runtime_StartAsyncInvoke-request-outputDataConfig"></a>
Where to store the output.  
Type: [AsyncInvokeOutputDataConfig](API_runtime_AsyncInvokeOutputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_runtime_StartAsyncInvoke_RequestSyntax) **   <a name="bedrock-runtime_StartAsyncInvoke-request-tags"></a>
Tags to apply to the invocation.  
Type: Array of [Tag](API_runtime_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_runtime_StartAsyncInvoke_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invocationArn": "string"
}
```

## Response Elements
<a name="API_runtime_StartAsyncInvoke_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invocationArn](#API_runtime_StartAsyncInvoke_ResponseSyntax) **   <a name="bedrock-runtime_StartAsyncInvoke-response-invocationArn"></a>
The ARN of the invocation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:async-invoke/[a-z0-9]{12}` 

## Errors
<a name="API_runtime_StartAsyncInvoke_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. For troubleshooting this error, see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource ARN was not found. For troubleshooting this error, see [ResourceNotFound](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found) in the Amazon Bedrock User Guide  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
Your request exceeds the service quota for your account. You can view your quotas at [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html). You can resubmit your request later.  
HTTP Status Code: 400

 ** ServiceUnavailableException **   
The service isn't currently available. For troubleshooting this error, see [ServiceUnavailable](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable) in the Amazon Bedrock User Guide  
HTTP Status Code: 503

 ** ThrottlingException **   
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide  
HTTP Status Code: 400

## See Also
<a name="API_runtime_StartAsyncInvoke_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/StartAsyncInvoke) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/StartAsyncInvoke) 