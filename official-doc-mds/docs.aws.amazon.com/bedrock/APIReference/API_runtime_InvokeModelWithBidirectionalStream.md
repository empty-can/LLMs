

# InvokeModelWithBidirectionalStream
<a name="API_runtime_InvokeModelWithBidirectionalStream"></a>

Invoke the specified Amazon Bedrock model to run inference using the bidirectional stream. The response is returned in a stream that remains open for 8 minutes. A single session can contain multiple prompts and responses from the model. The prompts to the model are provided as audio files and the model's responses are spoken back to the user and transcribed.

It is possible for users to interrupt the model's response with a new prompt, which will halt the response speech. The model will retain contextual awareness of the conversation while pivoting to respond to the new prompt.

This operation requires permission for the `bedrock:InvokeModel` action.

Note that to log `InvokeModelWithBidirectionalStream` API calls in CloudTrail, you need to configure advanced event selectors to record data events for the `AWS::Bedrock::Model` resource type and `AWS:Bedrock::AsyncInvoke`. To learn more, see [Monitor Amazon Bedrock API calls using CloudTrail](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html).

**Important**  
To deny all inference access to resources that you specify in the modelId field, you need to deny access to the `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` actions. Doing this also denies access to the resource through the Converse API actions ([Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) and [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)). For more information see [Deny access for inference on specific models](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference). 

For more information, see [Using the Amazon Nova Sonic Speech-to-Speech model](https://docs.aws.amazon.com/nova/latest/userguide/speech.html).

## Request Syntax
<a name="API_runtime_InvokeModelWithBidirectionalStream_RequestSyntax"></a>

```
POST /model/{{modelId}}/invoke-with-bidirectional-stream HTTP/1.1
Content-type: application/json

{
   "chunk": { 
      "bytes": {{blob}}
   }
}
```

## URI Request Parameters
<a name="API_runtime_InvokeModelWithBidirectionalStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelId](#API_runtime_InvokeModelWithBidirectionalStream_RequestSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-request-uri-modelId"></a>
The model ID or ARN of the model ID to use. Currently, only `amazon.nova-sonic-v1:0` is supported.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:imported-model/[a-z0-9]{12})|([0-9]{12}:provisioned-model/[a-z0-9]{12})|([0-9]{12}:custom-model-deployment/[a-z0-9]{12})|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)|([a-zA-Z0-9-:.]+)$|(^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?))$|(^arn:aws:sagemaker:[a-z0-9-]+:[0-9]{12}:endpoint/[a-zA-Z0-9-]+$)|(^arn:aws(-[^:]+)?:bedrock:([0-9a-z-]{1,20}):([0-9]{12}):(default-)?prompt-router/[a-zA-Z0-9-:.]+$)`   
Required: Yes

## Request Body
<a name="API_runtime_InvokeModelWithBidirectionalStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [chunk](#API_runtime_InvokeModelWithBidirectionalStream_RequestSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-request-chunk"></a>
The audio chunk that is used as input for the invocation step.  
Type: [BidirectionalInputPayloadPart](API_runtime_BidirectionalInputPayloadPart.md) object  
Required: No

## Response Syntax
<a name="API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "chunk": { 
      "bytes": blob
   },
   "internalServerException": { 
   },
   "modelStreamErrorException": { 
   },
   "modelTimeoutException": { 
   },
   "serviceUnavailableException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_runtime_InvokeModelWithBidirectionalStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [chunk](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-chunk"></a>
The speech chunk that was provided as output from the invocation step.  
Type: [BidirectionalOutputPayloadPart](API_runtime_BidirectionalOutputPayloadPart.md) object

 ** [internalServerException](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-internalServerException"></a>
The request encountered an unknown internal error.  
Type: Exception  
HTTP Status Code: 500

 ** [modelStreamErrorException](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-modelStreamErrorException"></a>
The request encountered an error with the model stream.  
Type: Exception  
HTTP Status Code: 424

 ** [modelTimeoutException](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-modelTimeoutException"></a>
The connection was closed because a request was not received within the timeout period.  
Type: Exception  
HTTP Status Code: 408

 ** [serviceUnavailableException](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-serviceUnavailableException"></a>
The request has failed due to a temporary failure of the server.  
Type: Exception  
HTTP Status Code: 503

 ** [throttlingException](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-throttlingException"></a>
The request was denied due to request throttling.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_runtime_InvokeModelWithBidirectionalStream_ResponseSyntax) **   <a name="bedrock-runtime_InvokeModelWithBidirectionalStream-response-validationException"></a>
The input fails to satisfy the constraints specified by an AWS service.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_runtime_InvokeModelWithBidirectionalStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. For troubleshooting this error, see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide  
HTTP Status Code: 500

 ** ModelErrorException **   
The request failed due to an error while processing the model.    
 ** originalStatusCode **   
The original status code.  
 ** resourceName **   
The resource name.
HTTP Status Code: 424

 ** ModelNotReadyException **   
The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools* reference guide.  
HTTP Status Code: 429

 ** ModelStreamErrorException **   
An error occurred while streaming the response. Retry your request.    
 ** originalMessage **   
The original message.  
 ** originalStatusCode **   
The original status code.
HTTP Status Code: 424

 ** ModelTimeoutException **   
The request took too long to process. Processing time exceeded the model timeout length.  
HTTP Status Code: 408

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
<a name="API_runtime_InvokeModelWithBidirectionalStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStream) 