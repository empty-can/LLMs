

# ConfigurationBundleVersionSummary
<a name="API_ConfigurationBundleVersionSummary"></a>

Summary information about a configuration bundle version.

## Contents
<a name="API_ConfigurationBundleVersionSummary_Contents"></a>

 ** bundleArn **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleVersionSummary-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** bundleId **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleVersionSummary-bundleId"></a>
The unique identifier of the configuration bundle.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** versionCreatedAt **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleVersionSummary-versionCreatedAt"></a>
The timestamp when this version was created.  
Type: Timestamp  
Required: Yes

 ** versionId **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleVersionSummary-versionId"></a>
The version identifier of this configuration bundle version.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** lineageMetadata **   <a name="bedrockagentcorecontrol-Type-ConfigurationBundleVersionSummary-lineageMetadata"></a>
The version lineage metadata, including parent versions, branch name, and creation source.  
Type: [VersionLineageMetadata](API_VersionLineageMetadata.md) object  
Required: No

## See Also
<a name="API_ConfigurationBundleVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConfigurationBundleVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConfigurationBundleVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConfigurationBundleVersionSummary) 