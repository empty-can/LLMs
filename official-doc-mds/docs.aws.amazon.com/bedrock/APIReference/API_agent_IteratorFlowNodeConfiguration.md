

# IteratorFlowNodeConfiguration
<a name="API_agent_IteratorFlowNodeConfiguration"></a>

Contains configurations for an iterator node in a flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.

The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.

## Contents
<a name="API_agent_IteratorFlowNodeConfiguration_Contents"></a>

The members of this exception structure are context-dependent.

## See Also
<a name="API_agent_IteratorFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/IteratorFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/IteratorFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/IteratorFlowNodeConfiguration) 