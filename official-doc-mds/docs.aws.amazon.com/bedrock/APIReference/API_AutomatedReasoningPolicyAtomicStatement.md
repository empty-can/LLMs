

# AutomatedReasoningPolicyAtomicStatement
<a name="API_AutomatedReasoningPolicyAtomicStatement"></a>

Represents a single, indivisible statement extracted from a source document. Atomic statements are the fundamental units used to ground policy rules and variables to their source material.

## Contents
<a name="API_AutomatedReasoningPolicyAtomicStatement_Contents"></a>

 ** id **   <a name="bedrock-Type-AutomatedReasoningPolicyAtomicStatement-id"></a>
A unique identifier for this atomic statement within the fidelity report.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 8.  
Pattern: `[a-zA-Z0-9]*`   
Required: Yes

 ** location **   <a name="bedrock-Type-AutomatedReasoningPolicyAtomicStatement-location"></a>
Information about where this statement appears in the source document, including line numbers.  
Type: [AutomatedReasoningPolicyStatementLocation](API_AutomatedReasoningPolicyStatementLocation.md) object  
Required: Yes

 ** text **   <a name="bedrock-Type-AutomatedReasoningPolicyAtomicStatement-text"></a>
The actual text content of the atomic statement as extracted from the source document.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyAtomicStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAtomicStatement) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAtomicStatement) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAtomicStatement) 