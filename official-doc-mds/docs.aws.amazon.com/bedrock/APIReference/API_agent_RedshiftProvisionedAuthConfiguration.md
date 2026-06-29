

# RedshiftProvisionedAuthConfiguration
<a name="API_agent_RedshiftProvisionedAuthConfiguration"></a>

Contains configurations for authentication to an Amazon Redshift provisioned data warehouse. Specify the type of authentication to use in the `type` field and include the corresponding field. If you specify IAM authentication, you don't need to include another field.

## Contents
<a name="API_agent_RedshiftProvisionedAuthConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_RedshiftProvisionedAuthConfiguration-type"></a>
The type of authentication to use.  
Type: String  
Valid Values: `IAM | USERNAME_PASSWORD | USERNAME`   
Required: Yes

 ** databaseUser **   <a name="bedrock-Type-agent_RedshiftProvisionedAuthConfiguration-databaseUser"></a>
The database username for authentication to an Amazon Redshift provisioned data warehouse.  
Type: String  
Required: No

 ** usernamePasswordSecretArn **   <a name="bedrock-Type-agent_RedshiftProvisionedAuthConfiguration-usernamePasswordSecretArn"></a>
The ARN of an Secrets Manager secret for authentication.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}`   
Required: No

## See Also
<a name="API_agent_RedshiftProvisionedAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftProvisionedAuthConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftProvisionedAuthConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftProvisionedAuthConfiguration) 