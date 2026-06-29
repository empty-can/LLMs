

# AppliedGuardrailDetails
<a name="API_runtime_AppliedGuardrailDetails"></a>

Details about the specific guardrail that was applied during this assessment, including its identifier, version, ARN, origin, and ownership information.

## Contents
<a name="API_runtime_AppliedGuardrailDetails_Contents"></a>

 ** guardrailArn **   <a name="bedrock-Type-runtime_AppliedGuardrailDetails-guardrailArn"></a>
The ARN of the guardrail that was applied.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+)`   
Required: No

 ** guardrailId **   <a name="bedrock-Type-runtime_AppliedGuardrailDetails-guardrailId"></a>
The unique ID of the guardrail that was applied.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `([a-z0-9]+)`   
Required: No

 ** guardrailOrigin **   <a name="bedrock-Type-runtime_AppliedGuardrailDetails-guardrailOrigin"></a>
The origin of how the guardrail was applied. This can be either requested at the API level or enforced at the account or organization level as a default guardrail.  
Type: Array of strings  
Valid Values: `REQUEST | ACCOUNT_ENFORCED | ORGANIZATION_ENFORCED`   
Required: No

 ** guardrailOwnership **   <a name="bedrock-Type-runtime_AppliedGuardrailDetails-guardrailOwnership"></a>
The ownership type of the guardrail, indicating whether it is owned by the requesting account or is a cross-account guardrail shared from another AWS account.  
Type: String  
Valid Values: `SELF | CROSS_ACCOUNT`   
Required: No

 ** guardrailVersion **   <a name="bedrock-Type-runtime_AppliedGuardrailDetails-guardrailVersion"></a>
The version of the guardrail that was applied.  
Type: String  
Pattern: `(|([1-9][0-9]{0,7})|(DRAFT))`   
Required: No

## See Also
<a name="API_runtime_AppliedGuardrailDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/AppliedGuardrailDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/AppliedGuardrailDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/AppliedGuardrailDetails) 