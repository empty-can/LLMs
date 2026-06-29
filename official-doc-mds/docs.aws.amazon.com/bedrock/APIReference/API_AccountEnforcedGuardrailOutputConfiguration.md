

# AccountEnforcedGuardrailOutputConfiguration
<a name="API_AccountEnforcedGuardrailOutputConfiguration"></a>

Account enforced guardrail output configuration.

## Contents
<a name="API_AccountEnforcedGuardrailOutputConfiguration_Contents"></a>

 ** configId **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-configId"></a>
Unique ID for the account enforced configuration.  
Type: String  
Pattern: `[a-z0-9]+`   
Required: No

 ** createdAt **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-createdAt"></a>
Timestamp.  
Type: Timestamp  
Required: No

 ** createdBy **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-createdBy"></a>
The ARN of the role used to update the configuration.  
Type: String  
Required: No

 ** guardrailArn **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-guardrailArn"></a>
ARN representation for the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+`   
Required: No

 ** guardrailId **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-guardrailId"></a>
Unique ID for the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** guardrailVersion **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-guardrailVersion"></a>
Numerical guardrail version.  
Type: String  
Pattern: `[1-9][0-9]{0,7}`   
Required: No

 ** inputTags **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-inputTags"></a>
 *This member has been deprecated.*   
Whether to honor or ignore input tags at runtime.  
Type: String  
Valid Values: `HONOR | IGNORE`   
Required: No

 ** modelEnforcement **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-modelEnforcement"></a>
Model-specific information for the enforced guardrail configuration.  
Type: [ModelEnforcement](API_ModelEnforcement.md) object  
Required: No

 ** owner **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-owner"></a>
Configuration owner type.  
Type: String  
Valid Values: `ACCOUNT`   
Required: No

 ** selectiveContentGuarding **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-selectiveContentGuarding"></a>
Selective content guarding controls for enforced guardrails.  
Type: [SelectiveContentGuarding](API_SelectiveContentGuarding.md) object  
Required: No

 ** updatedAt **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-updatedAt"></a>
Timestamp.  
Type: Timestamp  
Required: No

 ** updatedBy **   <a name="bedrock-Type-AccountEnforcedGuardrailOutputConfiguration-updatedBy"></a>
The ARN of the role used to update the configuration.  
Type: String  
Required: No

## See Also
<a name="API_AccountEnforcedGuardrailOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AccountEnforcedGuardrailOutputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AccountEnforcedGuardrailOutputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AccountEnforcedGuardrailOutputConfiguration) 