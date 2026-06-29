

# LlmExtractionConfig
<a name="API_LlmExtractionConfig"></a>

Model-based metadata extraction configuration.

## Contents
<a name="API_LlmExtractionConfig_Contents"></a>

 ** definition **   <a name="bedrockagentcorecontrol-Type-LlmExtractionConfig-definition"></a>
Description of what this metadata field represents.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

 ** llmExtractionInstruction **   <a name="bedrockagentcorecontrol-Type-LlmExtractionConfig-llmExtractionInstruction"></a>
Instructions for extraction. Supports built-in operators like LATEST\_VALUE or custom natural-language instructions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: No

 ** validation **   <a name="bedrockagentcorecontrol-Type-LlmExtractionConfig-validation"></a>
Validation rules to constrain extracted values.  
Type: [Validation](API_Validation.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_LlmExtractionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LlmExtractionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LlmExtractionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LlmExtractionConfig) 