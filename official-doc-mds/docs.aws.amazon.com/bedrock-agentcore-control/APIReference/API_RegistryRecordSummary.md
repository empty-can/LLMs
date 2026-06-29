

# RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

Contains summary information about a registry record.

## Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** descriptorType **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-descriptorType"></a>
The descriptor type of the registry record. Possible values are `MCP`, `A2A`, `CUSTOM`, and `AGENT_SKILLS`.  
Type: String  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS`   
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-name"></a>
The name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordVersion **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-recordVersion"></a>
The version of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** registryArn **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-registryArn"></a>
The Amazon Resource Name (ARN) of the registry that contains the record.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-status"></a>
The current status of the registry record. Possible values include `CREATING`, `DRAFT`, `APPROVED`, `PENDING_APPROVAL`, `REJECTED`, `DEPRECATED`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED`.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-RegistryRecordSummary-description"></a>
The description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

## See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RegistryRecordSummary) 