

# GuardrailConfigurationWithArn
<a name="API_agent-runtime_GuardrailConfigurationWithArn"></a>

 The configuration details for the guardrail. 

## Contents
<a name="API_agent-runtime_GuardrailConfigurationWithArn_Contents"></a>

 ** guardrailIdentifier **   <a name="bedrock-Type-agent-runtime_GuardrailConfigurationWithArn-guardrailIdentifier"></a>
 The unique identifier for the guardrail.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: Yes

 ** guardrailVersion **   <a name="bedrock-Type-agent-runtime_GuardrailConfigurationWithArn-guardrailVersion"></a>
 The version of the guardrail.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))`   
Required: Yes

## See Also
<a name="API_agent-runtime_GuardrailConfigurationWithArn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GuardrailConfigurationWithArn) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GuardrailConfigurationWithArn) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GuardrailConfigurationWithArn) 