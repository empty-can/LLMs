

# BatchDeleteAdvancedPromptOptimizationJobError
<a name="API_BatchDeleteAdvancedPromptOptimizationJobError"></a>

Information about an error deleting a job.

## Contents
<a name="API_BatchDeleteAdvancedPromptOptimizationJobError_Contents"></a>

 ** code **   <a name="bedrock-Type-BatchDeleteAdvancedPromptOptimizationJobError-code"></a>
The error code.  
Type: String  
Required: Yes

 ** jobIdentifier **   <a name="bedrock-Type-BatchDeleteAdvancedPromptOptimizationJobError-jobIdentifier"></a>
The identifier of the job that could not be deleted.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/)?[a-z0-9]{12})`   
Required: Yes

 ** message **   <a name="bedrock-Type-BatchDeleteAdvancedPromptOptimizationJobError-message"></a>
A message describing the error.  
Type: String  
Required: No

## See Also
<a name="API_BatchDeleteAdvancedPromptOptimizationJobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJobError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJobError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJobError) 