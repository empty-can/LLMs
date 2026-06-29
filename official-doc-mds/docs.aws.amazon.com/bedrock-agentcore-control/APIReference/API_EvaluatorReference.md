

# EvaluatorReference
<a name="API_EvaluatorReference"></a>

 The reference to an evaluator used in online evaluation configurations, containing the evaluator identifier. 

## Contents
<a name="API_EvaluatorReference_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** evaluatorId **   <a name="bedrockagentcorecontrol-Type-EvaluatorReference-evaluatorId"></a>
 The unique identifier of the evaluator. Can reference builtin evaluators (e.g., Builtin.Helpfulness) or custom evaluators.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: No

## See Also
<a name="API_EvaluatorReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EvaluatorReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EvaluatorReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EvaluatorReference) 