

# ConverseStreamMetadataEvent
<a name="API_runtime_ConverseStreamMetadataEvent"></a>

A conversation stream metadata event.

## Contents
<a name="API_runtime_ConverseStreamMetadataEvent_Contents"></a>

 ** metrics **   <a name="bedrock-Type-runtime_ConverseStreamMetadataEvent-metrics"></a>
The metrics for the conversation stream metadata event.  
Type: [ConverseStreamMetrics](API_runtime_ConverseStreamMetrics.md) object  
Required: Yes

 ** usage **   <a name="bedrock-Type-runtime_ConverseStreamMetadataEvent-usage"></a>
Usage information for the conversation stream event.  
Type: [TokenUsage](API_runtime_TokenUsage.md) object  
Required: Yes

 ** performanceConfig **   <a name="bedrock-Type-runtime_ConverseStreamMetadataEvent-performanceConfig"></a>
Model performance configuration metadata for the conversation stream event.  
Type: [PerformanceConfiguration](API_runtime_PerformanceConfiguration.md) object  
Required: No

 ** serviceTier **   <a name="bedrock-Type-runtime_ConverseStreamMetadataEvent-serviceTier"></a>
Specifies the processing tier configuration used for serving the request.  
Type: [ServiceTier](API_runtime_ServiceTier.md) object  
Required: No

 ** trace **   <a name="bedrock-Type-runtime_ConverseStreamMetadataEvent-trace"></a>
The trace object in the response from [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) that contains information about the guardrail behavior.  
Type: [ConverseStreamTrace](API_runtime_ConverseStreamTrace.md) object  
Required: No

## See Also
<a name="API_runtime_ConverseStreamMetadataEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ConverseStreamMetadataEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ConverseStreamMetadataEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ConverseStreamMetadataEvent) 