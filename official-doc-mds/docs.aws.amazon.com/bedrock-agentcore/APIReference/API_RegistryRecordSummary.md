

# RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

 Summary information about a registry record.

## Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-createdAt"></a>
 The date and time when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** descriptors **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-descriptors"></a>
 The descriptor configurations for this registry record.  
Type: [Descriptors](API_Descriptors.md) object  
Required: Yes

 ** descriptorType **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-descriptorType"></a>
 The type of descriptor associated with this registry record.  
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS`   
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-name"></a>
 The name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-recordArn"></a>
 The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-recordId"></a>
 The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** registryArn **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-registryArn"></a>
 The Amazon Resource Name (ARN) of the registry that this record belongs to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-status"></a>
 The current status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-updatedAt"></a>
 The date and time when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-version"></a>
 The version of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-RegistryRecordSummary-description"></a>
 A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

## See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RegistryRecordSummary) 