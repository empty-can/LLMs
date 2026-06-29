

# ModelImportJobSummary
<a name="API_ModelImportJobSummary"></a>

Information about the import job.

## Contents
<a name="API_ModelImportJobSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-ModelImportJobSummary-creationTime"></a>
The time import job was created.  
Type: Timestamp  
Required: Yes

 ** jobArn **   <a name="bedrock-Type-ModelImportJobSummary-jobArn"></a>
The Amazon Resource Name (ARN) of the import job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12}`   
Required: Yes

 ** jobName **   <a name="bedrock-Type-ModelImportJobSummary-jobName"></a>
The name of the import job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*`   
Required: Yes

 ** status **   <a name="bedrock-Type-ModelImportJobSummary-status"></a>
The status of the imported job.   
Type: String  
Valid Values: `InProgress | Completed | Failed`   
Required: Yes

 ** endTime **   <a name="bedrock-Type-ModelImportJobSummary-endTime"></a>
The time when import job ended.  
Type: Timestamp  
Required: No

 ** importedModelArn **   <a name="bedrock-Type-ModelImportJobSummary-importedModelArn"></a>
The Amazon resource Name (ARN) of the imported model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12}`   
Required: No

 ** importedModelName **   <a name="bedrock-Type-ModelImportJobSummary-importedModelName"></a>
The name of the imported model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+`   
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-ModelImportJobSummary-lastModifiedTime"></a>
The time when the import job was last modified.  
Type: Timestamp  
Required: No

## See Also
<a name="API_ModelImportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelImportJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelImportJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelImportJobSummary) 