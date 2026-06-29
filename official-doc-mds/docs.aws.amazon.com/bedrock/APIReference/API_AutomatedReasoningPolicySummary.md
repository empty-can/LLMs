

# AutomatedReasoningPolicySummary
<a name="API_AutomatedReasoningPolicySummary"></a>

Contains summary information about an Automated Reasoning policy, including metadata and timestamps.

## Contents
<a name="API_AutomatedReasoningPolicySummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-createdAt"></a>
The timestamp when the policy was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-name"></a>
The name of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+`   
Required: Yes

 ** policyArn **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-policyArn"></a>
The Amazon Resource Name (ARN) of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

 ** policyId **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-policyId"></a>
The unique identifier of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[a-z0-9]{12}`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-updatedAt"></a>
The timestamp when the policy was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-version"></a>
The version of the policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `([1-9][0-9]{0,11})`   
Required: Yes

 ** description **   <a name="bedrock-Type-AutomatedReasoningPolicySummary-description"></a>
The description of the policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicySummary) 