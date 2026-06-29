

# BatchDeleteAdvancedPromptOptimizationJobItem
<a name="API_BatchDeleteAdvancedPromptOptimizationJobItem"></a>

Information about a successfully deleted job.

## Contents
<a name="API_BatchDeleteAdvancedPromptOptimizationJobItem_Contents"></a>

 ** jobIdentifier **   <a name="bedrock-Type-BatchDeleteAdvancedPromptOptimizationJobItem-jobIdentifier"></a>
The identifier of the deleted job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/)?[a-z0-9]{12})`   
Required: Yes

 ** jobStatus **   <a name="bedrock-Type-BatchDeleteAdvancedPromptOptimizationJobItem-jobStatus"></a>
The status of the deleted job.  
Type: String  
Valid Values: `InProgress | Completed | Failed | PartiallyCompleted | Stopping | Stopped | Deleting`   
Required: Yes

## See Also
<a name="API_BatchDeleteAdvancedPromptOptimizationJobItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJobItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJobItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJobItem) 