

# KnowledgeBaseDocumentDetail
<a name="API_agent_KnowledgeBaseDocumentDetail"></a>

Contains the details for a document that was ingested or deleted.

## Contents
<a name="API_agent_KnowledgeBaseDocumentDetail_Contents"></a>

 ** dataSourceId **   <a name="bedrock-Type-agent_KnowledgeBaseDocumentDetail-dataSourceId"></a>
The identifier of the data source connected to the knowledge base that the document was ingested into or deleted from.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** identifier **   <a name="bedrock-Type-agent_KnowledgeBaseDocumentDetail-identifier"></a>
Contains information that identifies the document.  
Type: [DocumentIdentifier](API_agent_DocumentIdentifier.md) object  
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_KnowledgeBaseDocumentDetail-knowledgeBaseId"></a>
The identifier of the knowledge base that the document was ingested into or deleted from.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** status **   <a name="bedrock-Type-agent_KnowledgeBaseDocumentDetail-status"></a>
The ingestion status of the document. The following statuses are possible:  
+ STARTING – You submitted the ingestion job containing the document.
+ PENDING – The document is waiting to be ingested.
+ IN\_PROGRESS – The document is being ingested.
+ INDEXED – The document was successfully indexed.
+ PARTIALLY\_INDEXED – The document was partially indexed.
+ METADATA\_PARTIALLY\_INDEXED – You submitted metadata for an existing document and it was partially indexed.
+ METADATA\_UPDATE\_FAILED – You submitted a metadata update for an existing document but it failed.
+ FAILED – The document failed to be ingested.
+ NOT\_FOUND – The document wasn't found.
+ IGNORED – The document was ignored during ingestion.
+ DELETING – You submitted the delete job containing the document.
+ DELETE\_IN\_PROGRESS – The document is being deleted.
Type: String  
Valid Values: `INDEXED | PARTIALLY_INDEXED | PENDING | FAILED | METADATA_PARTIALLY_INDEXED | METADATA_UPDATE_FAILED | IGNORED | NOT_FOUND | STARTING | IN_PROGRESS | DELETING | DELETE_IN_PROGRESS`   
Required: Yes

 ** statusReason **   <a name="bedrock-Type-agent_KnowledgeBaseDocumentDetail-statusReason"></a>
The reason for the status. Appears alongside the status `IGNORED`.  
Type: String  
Required: No

 ** updatedAt **   <a name="bedrock-Type-agent_KnowledgeBaseDocumentDetail-updatedAt"></a>
The date and time at which the document was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_agent_KnowledgeBaseDocumentDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/KnowledgeBaseDocumentDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/KnowledgeBaseDocumentDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/KnowledgeBaseDocumentDetail) 