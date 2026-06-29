

# ConverseStreamOutput
<a name="API_runtime_ConverseStreamOutput"></a>

The messages output stream

## Contents
<a name="API_runtime_ConverseStreamOutput_Contents"></a>

 ** contentBlockDelta **   <a name="bedrock-Type-runtime_ConverseStreamOutput-contentBlockDelta"></a>
The messages output content block delta.  
Type: [ContentBlockDeltaEvent](API_runtime_ContentBlockDeltaEvent.md) object  
Required: No

 ** contentBlockStart **   <a name="bedrock-Type-runtime_ConverseStreamOutput-contentBlockStart"></a>
Start information for a content block.  
Type: [ContentBlockStartEvent](API_runtime_ContentBlockStartEvent.md) object  
Required: No

 ** contentBlockStop **   <a name="bedrock-Type-runtime_ConverseStreamOutput-contentBlockStop"></a>
Stop information for a content block.  
Type: [ContentBlockStopEvent](API_runtime_ContentBlockStopEvent.md) object  
Required: No

 ** internalServerException **   <a name="bedrock-Type-runtime_ConverseStreamOutput-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** messageStart **   <a name="bedrock-Type-runtime_ConverseStreamOutput-messageStart"></a>
Message start information.  
Type: [MessageStartEvent](API_runtime_MessageStartEvent.md) object  
Required: No

 ** messageStop **   <a name="bedrock-Type-runtime_ConverseStreamOutput-messageStop"></a>
Message stop information.  
Type: [MessageStopEvent](API_runtime_MessageStopEvent.md) object  
Required: No

 ** metadata **   <a name="bedrock-Type-runtime_ConverseStreamOutput-metadata"></a>
Metadata for the converse output stream.  
Type: [ConverseStreamMetadataEvent](API_runtime_ConverseStreamMetadataEvent.md) object  
Required: No

 ** modelStreamErrorException **   <a name="bedrock-Type-runtime_ConverseStreamOutput-modelStreamErrorException"></a>
A streaming error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** serviceUnavailableException **   <a name="bedrock-Type-runtime_ConverseStreamOutput-serviceUnavailableException"></a>
The service isn't currently available. For troubleshooting this error, see [ServiceUnavailable](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable) in the Amazon Bedrock User Guide  
Type: Exception  
HTTP Status Code: 503  
Required: No

 ** throttlingException **   <a name="bedrock-Type-runtime_ConverseStreamOutput-throttlingException"></a>
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="bedrock-Type-runtime_ConverseStreamOutput-validationException"></a>
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_runtime_ConverseStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ConverseStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ConverseStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ConverseStreamOutput) 