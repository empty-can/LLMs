

# InvokeModelWithBidirectionalStreamOutput
<a name="API_runtime_InvokeModelWithBidirectionalStreamOutput"></a>

Output from the bidirectional stream that was used for model invocation.

## Contents
<a name="API_runtime_InvokeModelWithBidirectionalStreamOutput_Contents"></a>

 ** chunk **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-chunk"></a>
The speech chunk that was provided as output from the invocation step.  
Type: [BidirectionalOutputPayloadPart](API_runtime_BidirectionalOutputPayloadPart.md) object  
Required: No

 ** internalServerException **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-internalServerException"></a>
The request encountered an unknown internal error.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** modelStreamErrorException **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-modelStreamErrorException"></a>
The request encountered an error with the model stream.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** modelTimeoutException **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-modelTimeoutException"></a>
The connection was closed because a request was not received within the timeout period.  
Type: Exception  
HTTP Status Code: 408  
Required: No

 ** serviceUnavailableException **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-serviceUnavailableException"></a>
The request has failed due to a temporary failure of the server.  
Type: Exception  
HTTP Status Code: 503  
Required: No

 ** throttlingException **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-throttlingException"></a>
The request was denied due to request throttling.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="bedrock-Type-runtime_InvokeModelWithBidirectionalStreamOutput-validationException"></a>
The input fails to satisfy the constraints specified by an AWS service.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_runtime_InvokeModelWithBidirectionalStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/InvokeModelWithBidirectionalStreamOutput) 