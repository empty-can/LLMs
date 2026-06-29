

# AutomatedReasoningPolicyGeneratedTestCase
<a name="API_AutomatedReasoningPolicyGeneratedTestCase"></a>

Represents a generated test case, consisting of query content, guard content, and expected results.

## Contents
<a name="API_AutomatedReasoningPolicyGeneratedTestCase_Contents"></a>

 ** expectedAggregatedFindingsResult **   <a name="bedrock-Type-AutomatedReasoningPolicyGeneratedTestCase-expectedAggregatedFindingsResult"></a>
The expected results of the generated test case. Possible values include:  
+  `VALID` - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.
+  `INVALID` - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.
+  `SATISFIABLE` - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.
+  `IMPOSSIBLE` - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.
Type: String  
Valid Values: `VALID | INVALID | SATISFIABLE | IMPOSSIBLE | TRANSLATION_AMBIGUOUS | TOO_COMPLEX | NO_TRANSLATION`   
Required: Yes

 ** guardContent **   <a name="bedrock-Type-AutomatedReasoningPolicyGeneratedTestCase-guardContent"></a>
The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** queryContent **   <a name="bedrock-Type-AutomatedReasoningPolicyGeneratedTestCase-queryContent"></a>
The input query or prompt that generated the content. This provides context for the validation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyGeneratedTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyGeneratedTestCase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyGeneratedTestCase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyGeneratedTestCase) 