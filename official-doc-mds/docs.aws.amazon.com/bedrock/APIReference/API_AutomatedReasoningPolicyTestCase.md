

# AutomatedReasoningPolicyTestCase
<a name="API_AutomatedReasoningPolicyTestCase"></a>

Represents a test for validating an Automated Reasoning policy. tests contain sample inputs and expected outcomes to verify policy behavior.

## Contents
<a name="API_AutomatedReasoningPolicyTestCase_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-createdAt"></a>
The timestamp when the test was created.  
Type: Timestamp  
Required: Yes

 ** guardContent **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-guardContent"></a>
The output content to be validated by the policy, typically representing a foundation model response.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** testCaseId **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-testCaseId"></a>
The unique identifier of the test.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `[0-9A-Z]{12}`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-updatedAt"></a>
The timestamp when the test was last updated.  
Type: Timestamp  
Required: Yes

 ** confidenceThreshold **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-confidenceThreshold"></a>
The minimum confidence level for logic validation. Content meeting this threshold is considered high-confidence and can be validated.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** expectedAggregatedFindingsResult **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-expectedAggregatedFindingsResult"></a>
The expected result of the Automated Reasoning check for this test.  
Type: String  
Valid Values: `VALID | INVALID | SATISFIABLE | IMPOSSIBLE | TRANSLATION_AMBIGUOUS | TOO_COMPLEX | NO_TRANSLATION`   
Required: No

 ** queryContent **   <a name="bedrock-Type-AutomatedReasoningPolicyTestCase-queryContent"></a>
The input query or prompt that generated the content. This provides context for the validation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyTestCase) 