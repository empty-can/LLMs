

# AccountEnforcedGuardrailInferenceInputConfiguration
<a name="API_AccountEnforcedGuardrailInferenceInputConfiguration"></a>

Account-level enforced guardrail input configuration.

## Contents
<a name="API_AccountEnforcedGuardrailInferenceInputConfiguration_Contents"></a>

 ** guardrailIdentifier **   <a name="bedrock-Type-AccountEnforcedGuardrailInferenceInputConfiguration-guardrailIdentifier"></a>
Identifier for the guardrail, could be the ID or the ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: Yes

 ** guardrailVersion **   <a name="bedrock-Type-AccountEnforcedGuardrailInferenceInputConfiguration-guardrailVersion"></a>
Numerical guardrail version.  
Type: String  
Pattern: `[1-9][0-9]{0,7}`   
Required: Yes

 ** modelEnforcement **   <a name="bedrock-Type-AccountEnforcedGuardrailInferenceInputConfiguration-modelEnforcement"></a>
Model-specific information for the enforced guardrail configuration. If not present, the configuration is enforced on all models  
Type: [ModelEnforcement](API_ModelEnforcement.md) object  
Required: No

 ** selectiveContentGuarding **   <a name="bedrock-Type-AccountEnforcedGuardrailInferenceInputConfiguration-selectiveContentGuarding"></a>
Selective content guarding controls for enforced guardrails.  
Type: [SelectiveContentGuarding](API_SelectiveContentGuarding.md) object  
Required: No

## See Also
<a name="API_AccountEnforcedGuardrailInferenceInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AccountEnforcedGuardrailInferenceInputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AccountEnforcedGuardrailInferenceInputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AccountEnforcedGuardrailInferenceInputConfiguration) 