

# InlineCodeFlowNodeConfiguration
<a name="API_agent_InlineCodeFlowNodeConfiguration"></a>

Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.

## Contents
<a name="API_agent_InlineCodeFlowNodeConfiguration_Contents"></a>

 ** code **   <a name="bedrock-Type-agent_InlineCodeFlowNodeConfiguration-code"></a>
The code that's executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.  
The code must be valid in the programming `language` that you specify.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 5000000.  
Required: Yes

 ** language **   <a name="bedrock-Type-agent_InlineCodeFlowNodeConfiguration-language"></a>
The programming language used by your inline code node.  
The code must be valid in the programming `language` that you specify. Currently, only Python 3 (`Python_3`) is supported.  
Type: String  
Valid Values: `Python_3`   
Required: Yes

## See Also
<a name="API_agent_InlineCodeFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/InlineCodeFlowNodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/InlineCodeFlowNodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/InlineCodeFlowNodeConfiguration) 