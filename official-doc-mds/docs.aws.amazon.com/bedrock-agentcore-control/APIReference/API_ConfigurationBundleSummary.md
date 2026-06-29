

# ConfigurationBundleSummary
<a name="API_ConfigurationBundleSummary"></a>

Summary information about a configuration bundle.

## Contents
<a name="API_ConfigurationBundleSummary_Contents"></a>

 ** bundleArn **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleSummary-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** bundleId **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleSummary-bundleId"></a>
The unique identifier of the configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** bundleName **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleSummary-bundleName"></a>
The name of the configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleSummary-createdAt"></a>
The timestamp when the configuration bundle was created.  
Type: Timestamp  
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleSummary-description"></a>
The description of the configuration bundle.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Pattern: `.+`   
Required: No

## See Also
<a name="API_ConfigurationBundleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConfigurationBundleSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConfigurationBundleSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConfigurationBundleSummary) 