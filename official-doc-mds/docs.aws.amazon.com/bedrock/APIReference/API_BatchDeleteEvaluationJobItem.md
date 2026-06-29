

# BatchDeleteEvaluationJobItem
<a name="API_BatchDeleteEvaluationJobItem"></a>

An evaluation job for deletion, and it’s current status.

## Contents
<a name="API_BatchDeleteEvaluationJobItem_Contents"></a>

 ** jobIdentifier **   <a name="bedrock-Type-BatchDeleteEvaluationJobItem-jobIdentifier"></a>
The Amazon Resource Name (ARN) of the evaluation job for deletion.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12})`   
Required: Yes

 ** jobStatus **   <a name="bedrock-Type-BatchDeleteEvaluationJobItem-jobStatus"></a>
The status of the evaluation job for deletion.  
Type: String  
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`   
Required: Yes

## See Also
<a name="API_BatchDeleteEvaluationJobItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/BatchDeleteEvaluationJobItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/BatchDeleteEvaluationJobItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/BatchDeleteEvaluationJobItem) 