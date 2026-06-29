

# FlowCondition
<a name="API_agent_FlowCondition"></a>

Defines a condition in the condition node.

## Contents
<a name="API_agent_FlowCondition_Contents"></a>

 ** name **   <a name="bedrock-Type-agent_FlowCondition-name"></a>
A name for the condition that you can reference.  
Type: String  
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}`   
Required: Yes

 ** expression **   <a name="bedrock-Type-agent_FlowCondition-expression"></a>
Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

## See Also
<a name="API_agent_FlowCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/FlowCondition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/FlowCondition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/FlowCondition) 