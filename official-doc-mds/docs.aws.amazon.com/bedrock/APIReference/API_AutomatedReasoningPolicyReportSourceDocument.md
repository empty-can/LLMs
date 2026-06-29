

# AutomatedReasoningPolicyReportSourceDocument
<a name="API_AutomatedReasoningPolicyReportSourceDocument"></a>

Represents a source document that was analyzed during fidelity report generation, including the document's metadata and its content broken down into atomic statements.

## Contents
<a name="API_AutomatedReasoningPolicyReportSourceDocument_Contents"></a>

 ** atomicStatements **   <a name="bedrock-Type-AutomatedReasoningPolicyReportSourceDocument-atomicStatements"></a>
The list of atomic statements extracted from this document, representing the fundamental units of meaning used for grounding.  
Type: Array of [AutomatedReasoningPolicyAtomicStatement](API_AutomatedReasoningPolicyAtomicStatement.md) objects  
Required: Yes

 ** documentContent **   <a name="bedrock-Type-AutomatedReasoningPolicyReportSourceDocument-documentContent"></a>
The document's content organized into annotated chunks with line number information for precise referencing.  
Type: Array of [AutomatedReasoningPolicyAnnotatedChunk](API_AutomatedReasoningPolicyAnnotatedChunk.md) objects  
Required: Yes

 ** documentHash **   <a name="bedrock-Type-AutomatedReasoningPolicyReportSourceDocument-documentHash"></a>
A SHA-256 hash of the document content, used for verification and ensuring the document hasn't changed since analysis.  
Type: String  
Length Constraints: Fixed length of 64.  
Required: Yes

 ** documentId **   <a name="bedrock-Type-AutomatedReasoningPolicyReportSourceDocument-documentId"></a>
A unique identifier for this document within the fidelity report.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 8.  
Pattern: `[a-zA-Z0-9]*`   
Required: Yes

 ** documentName **   <a name="bedrock-Type-AutomatedReasoningPolicyReportSourceDocument-documentName"></a>
The name of the source document that was analyzed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyReportSourceDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyReportSourceDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyReportSourceDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyReportSourceDocument) 