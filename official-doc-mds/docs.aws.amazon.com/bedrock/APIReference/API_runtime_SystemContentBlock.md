

# SystemContentBlock
<a name="API_runtime_SystemContentBlock"></a>

Contains configurations for instructions to provide the model for how to handle input. To learn more, see [Using the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html).

## Contents
<a name="API_runtime_SystemContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cachePoint **   <a name="bedrock-Type-runtime_SystemContentBlock-cachePoint"></a>
CachePoint to include in the system prompt.  
Type: [CachePointBlock](API_runtime_CachePointBlock.md) object  
Required: No

 ** guardContent **   <a name="bedrock-Type-runtime_SystemContentBlock-guardContent"></a>
A content block to assess with the guardrail. Use with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.   
For more information, see [Use a guardrail with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-converse-api.html).  
Type: [GuardrailConverseContentBlock](API_runtime_GuardrailConverseContentBlock.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** text **   <a name="bedrock-Type-runtime_SystemContentBlock-text"></a>
A system prompt for the model.   
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_runtime_SystemContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/SystemContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/SystemContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/SystemContentBlock) 