

# ContainerConfiguration
<a name="API_ContainerConfiguration"></a>

Representation of a container configuration.

## Contents
<a name="API_ContainerConfiguration_Contents"></a>

 ** containerUri **   <a name="bedrockagentcorecontrol-Type-ContainerConfiguration-containerUri"></a>
The ECR URI of the container.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `(([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com(\.cn)?|public\.ecr\.aws)/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?::([^:@]{1,300}))?(?:@(.+))?`   
Required: Yes

## See Also
<a name="API_ContainerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ContainerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ContainerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ContainerConfiguration) 