

# AutomatedReasoningCheckSatisfiableFinding
<a name="API_AutomatedReasoningCheckSatisfiableFinding"></a>

Indicates that the claims could be either true or false depending on additional assumptions not provided in the input.

## Contents
<a name="API_AutomatedReasoningCheckSatisfiableFinding_Contents"></a>

 ** claimsFalseScenario **   <a name="bedrock-Type-AutomatedReasoningCheckSatisfiableFinding-claimsFalseScenario"></a>
An example scenario demonstrating how the claims could be logically false.  
Type: [AutomatedReasoningCheckScenario](API_AutomatedReasoningCheckScenario.md) object  
Required: No

 ** claimsTrueScenario **   <a name="bedrock-Type-AutomatedReasoningCheckSatisfiableFinding-claimsTrueScenario"></a>
An example scenario demonstrating how the claims could be logically true.  
Type: [AutomatedReasoningCheckScenario](API_AutomatedReasoningCheckScenario.md) object  
Required: No

 ** logicWarning **   <a name="bedrock-Type-AutomatedReasoningCheckSatisfiableFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.  
Type: [AutomatedReasoningCheckLogicWarning](API_AutomatedReasoningCheckLogicWarning.md) object  
Required: No

 ** translation **   <a name="bedrock-Type-AutomatedReasoningCheckSatisfiableFinding-translation"></a>
The logical translation of the input that this finding evaluates.  
Type: [AutomatedReasoningCheckTranslation](API_AutomatedReasoningCheckTranslation.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningCheckSatisfiableFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckSatisfiableFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckSatisfiableFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckSatisfiableFinding) 