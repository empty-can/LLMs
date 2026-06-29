

# AutomatedReasoningCheckFinding
<a name="API_AutomatedReasoningCheckFinding"></a>

Represents the result of an Automated Reasoning validation check, indicating whether the content is logically valid, invalid, or falls into other categories based on the policy rules.

## Contents
<a name="API_AutomatedReasoningCheckFinding_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** impossible **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-impossible"></a>
Indicates that Automated Reasoning cannot make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.  
Type: [AutomatedReasoningCheckImpossibleFinding](API_AutomatedReasoningCheckImpossibleFinding.md) object  
Required: No

 ** invalid **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-invalid"></a>
Indicates that the claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exist different claims that are consistent with the premises and Automated Reasoning policy.  
Type: [AutomatedReasoningCheckInvalidFinding](API_AutomatedReasoningCheckInvalidFinding.md) object  
Required: No

 ** noTranslations **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-noTranslations"></a>
Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input.  
Type: [AutomatedReasoningCheckNoTranslationsFinding](API_AutomatedReasoningCheckNoTranslationsFinding.md) object  
Required: No

 ** satisfiable **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-satisfiable"></a>
Indicates that the claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.  
Type: [AutomatedReasoningCheckSatisfiableFinding](API_AutomatedReasoningCheckSatisfiableFinding.md) object  
Required: No

 ** tooComplex **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-tooComplex"></a>
Indicates that the input contains too much information for Automated Reasoning to process within its latency limits.  
Type: [AutomatedReasoningCheckTooComplexFinding](API_AutomatedReasoningCheckTooComplexFinding.md) object  
Required: No

 ** translationAmbiguous **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-translationAmbiguous"></a>
Indicates that an ambiguity was detected in the translation, making it unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.  
Type: [AutomatedReasoningCheckTranslationAmbiguousFinding](API_AutomatedReasoningCheckTranslationAmbiguousFinding.md) object  
Required: No

 ** valid **   <a name="bedrock-Type-AutomatedReasoningCheckFinding-valid"></a>
Indicates that the claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false.  
Type: [AutomatedReasoningCheckValidFinding](API_AutomatedReasoningCheckValidFinding.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningCheckFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckFinding) 