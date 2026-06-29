

# ResponseStream
<a name="API_runtime_ResponseStream"></a>

Definition of content in the response stream.

## Contents
<a name="API_runtime_ResponseStream_Contents"></a>

 ** chunk **   <a name="bedrock-Type-runtime_ResponseStream-chunk"></a>
Content included in the response.  
Type: [PayloadPart](API_runtime_PayloadPart.md) object  
Required: No

 ** internalServerException **   <a name="bedrock-Type-runtime_ResponseStream-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** modelStreamErrorException **   <a name="bedrock-Type-runtime_ResponseStream-modelStreamErrorException"></a>
An error occurred while streaming the response. Retry your request.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** modelTimeoutException **   <a name="bedrock-Type-runtime_ResponseStream-modelTimeoutException"></a>
The request took too long to process. Processing time exceeded the model timeout length.  
Type: Exception  
HTTP Status Code: 408  
Required: No

 ** serviceUnavailableException **   <a name="bedrock-Type-runtime_ResponseStream-serviceUnavailableException"></a>
The service isn't available. Try again later.  
Type: Exception  
HTTP Status Code: 503  
Required: No

 ** throttlingException **   <a name="bedrock-Type-runtime_ResponseStream-throttlingException"></a>
Your request was throttled because of service-wide limitations. Resubmit your request later or in a different region. You can also purchase [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) to increase the rate or number of tokens you can process.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="bedrock-Type-runtime_ResponseStream-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_runtime_ResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ResponseStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ResponseStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ResponseStream) 