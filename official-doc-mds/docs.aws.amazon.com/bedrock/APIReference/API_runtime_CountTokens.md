

# CountTokens
<a name="API_runtime_CountTokens"></a>

Returns the token count for a given inference request. This operation helps you estimate token usage before sending requests to foundation models by returning the token count that would be used if the same input were sent to the model in an inference request.

Token counting is model-specific because different models use different tokenization strategies. The token count returned by this operation will match the token count that would be charged if the same input were sent to the model in an `InvokeModel` or `Converse` request.

You can use this operation to:
+ Estimate costs before sending inference requests.
+ Optimize prompts to fit within token limits.
+ Plan for token usage in your applications.

This operation accepts the same input formats as `InvokeModel` and `Converse`, allowing you to count tokens for both raw text inputs and structured conversation formats.

The following operations are related to `CountTokens`:
+  [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) - Sends inference requests to foundation models
+  [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) - Sends conversation-based inference requests to foundation models

## Request Syntax
<a name="API_runtime_CountTokens_RequestSyntax"></a>

```
POST /model/{{modelId}}/count-tokens HTTP/1.1
Content-type: application/json

{
   "input": { ... }
}
```

## URI Request Parameters
<a name="API_runtime_CountTokens_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelId](#API_runtime_CountTokens_RequestSyntax) **   <a name="bedrock-runtime_CountTokens-request-uri-modelId"></a>
The unique identifier or ARN of the foundation model to use for token counting. Each model processes tokens differently, so the token count is specific to the model you specify.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z_\.\-/0-9:]+`   
Required: Yes

## Request Body
<a name="API_runtime_CountTokens_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [input](#API_runtime_CountTokens_RequestSyntax) **   <a name="bedrock-runtime_CountTokens-request-input"></a>
The input for which to count tokens. The structure of this parameter depends on whether you're counting tokens for an `InvokeModel` or `Converse` request:  
+ For `InvokeModel` requests, provide the request body in the `invokeModel` field
+ For `Converse` requests, provide the messages and system content in the `converse` field
The input format must be compatible with the model specified in the `modelId` parameter.  
Type: [CountTokensInput](API_runtime_CountTokensInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_runtime_CountTokens_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "inputTokens": number
}
```

## Response Elements
<a name="API_runtime_CountTokens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [inputTokens](#API_runtime_CountTokens_ResponseSyntax) **   <a name="bedrock-runtime_CountTokens-response-inputTokens"></a>
The number of tokens in the provided input according to the specified model's tokenization rules. This count represents the number of input tokens that would be processed if the same input were sent to the model in an inference request. Use this value to estimate costs and ensure your inputs stay within model token limits.  
Type: Integer

## Errors
<a name="API_runtime_CountTokens_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. For troubleshooting this error, see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource ARN was not found. For troubleshooting this error, see [ResourceNotFound](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found) in the Amazon Bedrock User Guide  
HTTP Status Code: 404

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
<a name="API_runtime_CountTokens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/CountTokens) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CountTokens) 