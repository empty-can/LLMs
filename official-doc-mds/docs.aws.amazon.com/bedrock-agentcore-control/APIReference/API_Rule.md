

# Rule
<a name="API_Rule"></a>

 The evaluation rule that defines sampling configuration, filtering criteria, and session detection settings for online evaluation. 

## Contents
<a name="API_Rule_Contents"></a>

 ** samplingConfig **   <a name="bedrockagentcorecontrol-Type-Rule-samplingConfig"></a>
 The sampling configuration that determines what percentage of agent traces to evaluate.   
Type: [SamplingConfig](API_SamplingConfig.md) object  
Required: Yes

 ** filters **   <a name="bedrockagentcorecontrol-Type-Rule-filters"></a>
 The list of filters that determine which agent traces should be included in the evaluation based on trace properties.   
Type: Array of [Filter](API_Filter.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

 ** sessionConfig **   <a name="bedrockagentcorecontrol-Type-Rule-sessionConfig"></a>
 The session configuration that defines timeout settings for detecting when agent sessions are complete and ready for evaluation.   
Type: [SessionConfig](API_SessionConfig.md) object  
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Rule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Rule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Rule) 