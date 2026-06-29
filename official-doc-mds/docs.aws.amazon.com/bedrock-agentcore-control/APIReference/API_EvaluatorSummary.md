

# EvaluatorSummary
<a name="API_EvaluatorSummary"></a>

 The summary information about an evaluator, including basic metadata and status information. 

## Contents
<a name="API_EvaluatorSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-createdAt"></a>
 The timestamp when the evaluator was created.   
Type: Timestamp  
Required: Yes

 ** evaluatorArn **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-evaluatorArn"></a>
 The Amazon Resource Name (ARN) of the evaluator.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/Builtin.[a-zA-Z0-9_-]+`   
Required: Yes

 ** evaluatorId **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-evaluatorId"></a>
 The unique identifier of the evaluator.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** evaluatorName **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-evaluatorName"></a>
 The name of the evaluator.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9_]{0,47})`   
Required: Yes

 ** evaluatorType **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-evaluatorType"></a>
 The type of evaluator, indicating whether it is a built-in evaluator provided by the service or a custom evaluator created by the user.   
Type: String  
Valid Values: `Builtin | Custom | CustomCode`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-status"></a>
 The current status of the evaluator.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-updatedAt"></a>
 The timestamp when the evaluator was last updated.   
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-description"></a>
 The description of the evaluator.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** kmsKeyArn **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-kmsKeyArn"></a>
 The Amazon Resource Name (ARN) of the customer managed AWS KMS key used to encrypt the evaluator's sensitive data. This field is only present for evaluators encrypted with a customer managed key.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** level **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-level"></a>
 The evaluation level (`TOOL_CALL`, `TRACE`, or `SESSION`) that determines the scope of evaluation.   
Type: String  
Valid Values: `TOOL_CALL | TRACE | SESSION`   
Required: No

 ** lockedForModification **   <a name="bedrockagentcorecontrol-Type-EvaluatorSummary-lockedForModification"></a>
 Whether the evaluator is locked for modification due to being referenced by active online evaluation configurations.   
Type: Boolean  
Required: No

## See Also
<a name="API_EvaluatorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EvaluatorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EvaluatorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EvaluatorSummary) 