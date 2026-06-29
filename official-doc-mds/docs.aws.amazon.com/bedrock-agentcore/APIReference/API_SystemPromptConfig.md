

# SystemPromptConfig
<a name="API_SystemPromptConfig"></a>

The system prompt input, either as inline text or from a configuration bundle.

## Contents
<a name="API_SystemPromptConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBundle **   <a name="BedrockAgentCore-Type-SystemPromptConfig-configurationBundle"></a>
The system prompt sourced from a configuration bundle version.  
Type: [SystemPromptConfigurationBundle](API_SystemPromptConfigurationBundle.md) object  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-SystemPromptConfig-text"></a>
The system prompt text provided inline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Required: No

## See Also
<a name="API_SystemPromptConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SystemPromptConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SystemPromptConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SystemPromptConfig) 