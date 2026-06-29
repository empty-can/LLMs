

# RegistrySummary
<a name="API_RegistrySummary"></a>

Contains summary information about a registry.

## Contents
<a name="API_RegistrySummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-createdAt"></a>
The timestamp when the registry was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-name"></a>
The name of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** registryArn **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-registryArn"></a>
The Amazon Resource Name (ARN) of the registry.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** registryId **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-registryId"></a>
The unique identifier of the registry.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-status"></a>
The current status of the registry. Possible values include `CREATING`, `READY`, `UPDATING`, `CREATE_FAILED`, `UPDATE_FAILED`, `DELETING`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-updatedAt"></a>
The timestamp when the registry was last updated.  
Type: Timestamp  
Required: Yes

 ** authorizerType **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-authorizerType"></a>
The type of authorizer used by the registry. This controls the authorization method for the Search and Invoke APIs used by consumers.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-description"></a>
The description of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** statusReason **   <a name="bedrockagentcorecontrol-Type-RegistrySummary-statusReason"></a>
The reason for the current status, typically set when the status is a failure state.  
Type: String  
Required: No

## See Also
<a name="API_RegistrySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RegistrySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RegistrySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RegistrySummary) 