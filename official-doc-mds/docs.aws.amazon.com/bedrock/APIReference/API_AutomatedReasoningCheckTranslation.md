

# AutomatedReasoningCheckTranslation
<a name="API_AutomatedReasoningCheckTranslation"></a>

Contains the logical translation of natural language input into formal logical statements, including premises, claims, and confidence scores.

## Contents
<a name="API_AutomatedReasoningCheckTranslation_Contents"></a>

 ** claims **   <a name="bedrock-Type-AutomatedReasoningCheckTranslation-claims"></a>
The logical statements that are being validated against the premises and policy rules.  
Type: Array of [AutomatedReasoningLogicStatement](API_AutomatedReasoningLogicStatement.md) objects  
Required: Yes

 ** confidence **   <a name="bedrock-Type-AutomatedReasoningCheckTranslation-confidence"></a>
A confidence score between 0 and 1 indicating how certain the system is about the logical translation.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: Yes

 ** premises **   <a name="bedrock-Type-AutomatedReasoningCheckTranslation-premises"></a>
The logical statements that serve as the foundation or assumptions for the claims.  
Type: Array of [AutomatedReasoningLogicStatement](API_AutomatedReasoningLogicStatement.md) objects  
Required: No

 ** untranslatedClaims **   <a name="bedrock-Type-AutomatedReasoningCheckTranslation-untranslatedClaims"></a>
References to portions of the original input text that correspond to the claims but could not be fully translated.  
Type: Array of [AutomatedReasoningCheckInputTextReference](API_AutomatedReasoningCheckInputTextReference.md) objects  
Required: No

 ** untranslatedPremises **   <a name="bedrock-Type-AutomatedReasoningCheckTranslation-untranslatedPremises"></a>
References to portions of the original input text that correspond to the premises but could not be fully translated.  
Type: Array of [AutomatedReasoningCheckInputTextReference](API_AutomatedReasoningCheckInputTextReference.md) objects  
Required: No

## See Also
<a name="API_AutomatedReasoningCheckTranslation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckTranslation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckTranslation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckTranslation) 