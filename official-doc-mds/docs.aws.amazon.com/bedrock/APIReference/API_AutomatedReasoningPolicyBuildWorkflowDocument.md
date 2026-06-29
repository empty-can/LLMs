

# AutomatedReasoningPolicyBuildWorkflowDocument
<a name="API_AutomatedReasoningPolicyBuildWorkflowDocument"></a>

Represents a source document used in the policy build workflow, containing the content and metadata needed for policy generation.

## Contents
<a name="API_AutomatedReasoningPolicyBuildWorkflowDocument_Contents"></a>

 ** document **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowDocument-document"></a>
The actual content of the source document that will be analyzed to extract policy rules and concepts.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 5000000.  
Required: Yes

 ** documentContentType **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowDocument-documentContentType"></a>
The MIME type of the document content (e.g., text/plain, application/pdf, text/markdown).  
Type: String  
Valid Values: `pdf | txt`   
Required: Yes

 ** documentName **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowDocument-documentName"></a>
A descriptive name for the document that helps identify its purpose and content.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

 ** documentDescription **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowDocument-documentDescription"></a>
A detailed description of the document's content and how it should be used in the policy generation process.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4000.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyBuildWorkflowDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowDocument) 