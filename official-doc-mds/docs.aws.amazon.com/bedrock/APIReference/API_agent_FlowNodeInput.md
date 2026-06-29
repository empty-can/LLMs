

# FlowNodeInput
<a name="API_agent_FlowNodeInput"></a>

Contains configurations for an input in an Amazon Bedrock Flows node.

## Contents
<a name="API_agent_FlowNodeInput_Contents"></a>

 ** expression **   <a name="bedrock-Type-agent_FlowNodeInput-expression"></a>
An expression that formats the input for the node. For an explanation of how to create expressions, see [Expressions in Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** name **   <a name="bedrock-Type-agent_FlowNodeInput-name"></a>
Specifies a name for the input that you can reference.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent_FlowNodeInput-type"></a>
Specifies the data type of the input. If the input doesn't match this type at runtime, a validation error will be thrown.  
Type: String  
Valid Values: `String | Number | Boolean | Object | Array`   
Required: Yes

 ** category **   <a name="bedrock-Type-agent_FlowNodeInput-category"></a>
Specifies how input data flows between iterations in a DoWhile loop.  
+  `LoopCondition` - Controls whether the loop continues by evaluating condition expressions against the input data. Use this category to define the condition that determines if the loop should continue. 
+  `ReturnValueToLoopStart` - Defines data to pass back to the start of the loop's next iteration. Use this category for variables that you want to update for each loop iteration.
+  `ExitLoop` - Defines the value that's available once the loop ends. Use this category to expose loop results to nodes outside the loop.
Type: String  
Valid Values: `LoopCondition | ReturnValueToLoopStart | ExitLoop`   
Required: No

## See Also
<a name="API_agent_FlowNodeInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowNodeInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowNodeInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowNodeInput) 