

# AutomatedReasoningCheckRule
<a name="API_AutomatedReasoningCheckRule"></a>

References a specific automated reasoning policy rule that was applied during evaluation.

## Contents
<a name="API_AutomatedReasoningCheckRule_Contents"></a>

 ** id **   <a name="bedrock-Type-AutomatedReasoningCheckRule-id"></a>
The unique identifier of the automated reasoning rule.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: No

 ** policyVersionArn **   <a name="bedrock-Type-AutomatedReasoningCheckRule-policyVersionArn"></a>
The ARN of the automated reasoning policy version that contains this rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: No

## See Also
<a name="API_AutomatedReasoningCheckRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckRule) 