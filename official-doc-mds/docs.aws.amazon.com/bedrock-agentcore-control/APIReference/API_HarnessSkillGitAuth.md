

# HarnessSkillGitAuth
<a name="API_HarnessSkillGitAuth"></a>

Authentication configuration for accessing a private git repository.

## Contents
<a name="API_HarnessSkillGitAuth_Contents"></a>

 ** credentialArn **   <a name="bedrockagentcorecontrol-Type-HarnessSkillGitAuth-credentialArn"></a>
The ARN of the credential in AgentCore Identity containing the password or personal access token.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`   
Required: Yes

 ** username **   <a name="bedrockagentcorecontrol-Type-HarnessSkillGitAuth-username"></a>
Username for authentication. Defaults to 'oauth2' if not specified.  
Type: String  
Required: No

## See Also
<a name="API_HarnessSkillGitAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessSkillGitAuth) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessSkillGitAuth) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessSkillGitAuth) 