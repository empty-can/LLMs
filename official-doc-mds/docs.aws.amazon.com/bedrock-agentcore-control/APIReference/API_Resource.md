

# Resource
<a name="API_Resource"></a>

Represents a resource within the AgentCore Policy system. Resources are the targets of policy evaluation. Currently, only AgentCore Gateways are supported as resources for policy enforcement.

## Contents
<a name="API_Resource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arn **   <a name="bedrockagentcorecontrol-Type-Resource-arn"></a>
The Amazon Resource Name (ARN) of the resource. This globally unique identifier specifies the exact resource that policies will be evaluated against for access control decisions.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Resource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Resource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Resource) 