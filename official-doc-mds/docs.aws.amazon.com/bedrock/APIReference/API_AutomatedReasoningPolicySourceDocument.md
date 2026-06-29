

# AutomatedReasoningPolicySourceDocument
<a name="API_AutomatedReasoningPolicySourceDocument"></a>

Represents a source document that was processed during a build workflow. Contains the document content, metadata, and a hash for verification.

## Contents
<a name="API_AutomatedReasoningPolicySourceDocument_Contents"></a>

 ** document **   <a name="bedrock-Type-AutomatedReasoningPolicySourceDocument-document"></a>
The raw content of the source document as a binary blob.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 5000000.  
Required: Yes

 ** documentContentType **   <a name="bedrock-Type-AutomatedReasoningPolicySourceDocument-documentContentType"></a>
The MIME type of the document (e.g., application/pdf, text/plain).  
Type: String  
Valid Values: `pdf | txt`   
Required: Yes

 ** documentHash **   <a name="bedrock-Type-AutomatedReasoningPolicySourceDocument-documentHash"></a>
A SHA-256 hash of the document content, used for verification and integrity checking.  
Type: String  
Length Constraints: Fixed length of 64.  
Required: Yes

 ** documentName **   <a name="bedrock-Type-AutomatedReasoningPolicySourceDocument-documentName"></a>
The name of the source document for identification purposes.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

 ** documentDescription **   <a name="bedrock-Type-AutomatedReasoningPolicySourceDocument-documentDescription"></a>
An optional description providing context about the document's content and purpose.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4000.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicySourceDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicySourceDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicySourceDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicySourceDocument) 