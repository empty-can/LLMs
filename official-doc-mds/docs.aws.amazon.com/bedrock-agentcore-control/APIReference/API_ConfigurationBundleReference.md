

# ConfigurationBundleReference
<a name="API_ConfigurationBundleReference"></a>

A reference to a specific version of a configuration bundle.

## Contents
<a name="API_ConfigurationBundleReference_Contents"></a>

 ** bundleArn **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleReference-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** bundleVersion **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleReference-bundleVersion"></a>
The version of the configuration bundle.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## See Also
<a name="API_ConfigurationBundleReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConfigurationBundleReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConfigurationBundleReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConfigurationBundleReference) 