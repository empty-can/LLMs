

# BatchDeleteEvaluationJobError
<a name="API_BatchDeleteEvaluationJobError"></a>

A JSON array that provides the status of the evaluation jobs being deleted.

## Contents
<a name="API_BatchDeleteEvaluationJobError_Contents"></a>

 ** code **   <a name="bedrock-Type-BatchDeleteEvaluationJobError-code"></a>
A HTTP status code of the evaluation job being deleted.  
Type: String  
Required: Yes

 ** jobIdentifier **   <a name="bedrock-Type-BatchDeleteEvaluationJobError-jobIdentifier"></a>
The ARN of the evaluation job being deleted.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12})`   
Required: Yes

 ** message **   <a name="bedrock-Type-BatchDeleteEvaluationJobError-message"></a>
A status message about the evaluation job deletion.  
Type: String  
Required: No

## See Also
<a name="API_BatchDeleteEvaluationJobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/BatchDeleteEvaluationJobError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/BatchDeleteEvaluationJobError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/BatchDeleteEvaluationJobError) 