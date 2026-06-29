

# RetrievalResultLocation
<a name="API_agent-runtime_RetrievalResultLocation"></a>

Contains information about the data source location.

This data type is used in the following API operations:
+  [Retrieve response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_ResponseSyntax) – in the `location` field
+  [RetrieveAndGenerate response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax) – in the `location` field
+  [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) – in the `location` field

## Contents
<a name="API_agent-runtime_RetrievalResultLocation_Contents"></a>

 ** type **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-type"></a>
The type of data source location.  
Type: String  
Valid Values: `S3 | WEB | CONFLUENCE | SALESFORCE | SHAREPOINT | CUSTOM | KENDRA | SQL | ONEDRIVE | GOOGLEDRIVE`   
Required: Yes

 ** confluenceLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-confluenceLocation"></a>
The Confluence data source location.  
Type: [RetrievalResultConfluenceLocation](API_agent-runtime_RetrievalResultConfluenceLocation.md) object  
Required: No

 ** customDocumentLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-customDocumentLocation"></a>
Specifies the location of a document in a custom data source.  
Type: [RetrievalResultCustomDocumentLocation](API_agent-runtime_RetrievalResultCustomDocumentLocation.md) object  
Required: No

 ** googleDriveLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-googleDriveLocation"></a>
The Google Drive data source location.  
Type: [RetrievalResultGoogleDriveLocation](API_agent-runtime_RetrievalResultGoogleDriveLocation.md) object  
Required: No

 ** kendraDocumentLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-kendraDocumentLocation"></a>
The location of a document in Amazon Kendra.  
Type: [RetrievalResultKendraDocumentLocation](API_agent-runtime_RetrievalResultKendraDocumentLocation.md) object  
Required: No

 ** oneDriveLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-oneDriveLocation"></a>
The Microsoft OneDrive data source location.  
Type: [RetrievalResultOneDriveLocation](API_agent-runtime_RetrievalResultOneDriveLocation.md) object  
Required: No

 ** s3Location **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-s3Location"></a>
The S3 data source location.  
Type: [RetrievalResultS3Location](API_agent-runtime_RetrievalResultS3Location.md) object  
Required: No

 ** salesforceLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-salesforceLocation"></a>
The Salesforce data source location.  
Type: [RetrievalResultSalesforceLocation](API_agent-runtime_RetrievalResultSalesforceLocation.md) object  
Required: No

 ** sharePointLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-sharePointLocation"></a>
The SharePoint data source location.  
Type: [RetrievalResultSharePointLocation](API_agent-runtime_RetrievalResultSharePointLocation.md) object  
Required: No

 ** sqlLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-sqlLocation"></a>
Specifies information about the SQL query used to retrieve the result.  
Type: [RetrievalResultSqlLocation](API_agent-runtime_RetrievalResultSqlLocation.md) object  
Required: No

 ** webLocation **   <a name="bedrock-Type-agent-runtime_RetrievalResultLocation-webLocation"></a>
The web URL/URLs data source location.  
Type: [RetrievalResultWebLocation](API_agent-runtime_RetrievalResultWebLocation.md) object  
Required: No

## See Also
<a name="API_agent-runtime_RetrievalResultLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrievalResultLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrievalResultLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrievalResultLocation) 