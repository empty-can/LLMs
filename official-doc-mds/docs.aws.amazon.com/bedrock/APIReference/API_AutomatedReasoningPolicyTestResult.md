

# AutomatedReasoningPolicyTestResult
<a name="API_AutomatedReasoningPolicyTestResult"></a>

Contains the results of testing an Automated Reasoning policy against various scenarios and validation checks.

## Contents
<a name="API_AutomatedReasoningPolicyTestResult_Contents"></a>

 ** policyArn **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy that was tested.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

 ** testCase **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-testCase"></a>
The test case that was executed, including the input content, expected results, and configuration parameters used during validation.  
Type: [AutomatedReasoningPolicyTestCase](API_AutomatedReasoningPolicyTestCase.md) object  
Required: Yes

 ** testRunStatus **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-testRunStatus"></a>
The overall status of the test run (e.g., COMPLETED, FAILED, IN\_PROGRESS).  
Type: String  
Valid Values: `NOT_STARTED | SCHEDULED | IN_PROGRESS | COMPLETED | FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-updatedAt"></a>
The timestamp when the test results were last updated.  
Type: Timestamp  
Required: Yes

 ** aggregatedTestFindingsResult **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-aggregatedTestFindingsResult"></a>
A summary of all test findings, aggregated to provide an overall assessment of policy quality and correctness.  
Type: String  
Valid Values: `VALID | INVALID | SATISFIABLE | IMPOSSIBLE | TRANSLATION_AMBIGUOUS | TOO_COMPLEX | NO_TRANSLATION`   
Required: No

 ** testFindings **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-testFindings"></a>
Detailed findings from the test run, including any issues, violations, or unexpected behaviors discovered.  
Type: Array of [AutomatedReasoningCheckFinding](API_AutomatedReasoningCheckFinding.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 20 items.  
Required: No

 ** testRunResult **   <a name="bedrock-Type-AutomatedReasoningPolicyTestResult-testRunResult"></a>
The overall result of the test run, indicating whether the policy passed or failed validation.  
Type: String  
Valid Values: `PASSED | FAILED`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyTestResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyTestResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyTestResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyTestResult) 